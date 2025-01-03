from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from .models import BlogCategory, Blog, BlogComment
from .forms import PubBlogForm
from django.db.models import Q

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, "index.html", context={"blogs": blogs})


def blog_detail(request, blog_id):
    try:
        # pk是主键id
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        blog = None
    return render(request, "blog_detail.html", context={"blog": blog})


# @login_required(login_url=reverse_lazy("zlauth:login"))
# @login_required(login_url='auth/login')
@login_required() #跳转地址配置在了settings的LOGIN_URL里
@require_http_methods(["GET", "POST"])
def pub_blog(request):
    if request.method == "GET":
        categories = BlogCategory.objects.all()
        return render(request, "pub_blog.html", context={"categories": categories})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            category_id = form.cleaned_data.get("category")
            blog = Blog.objects.create(title=title, content=content, category_id=category_id, author=request.user)
            return JsonResponse({"code": 200, "msg": "博客发布成功", "data":{"blog_id": blog.id}})
        else:
            print(form.errors)
            return JsonResponse({"code": 400, "msg": f"参数错误：{form.errors}"})


@require_POST
@login_required()
def pub_comment(request):
    blog_id = request.POST.get("blog_id")
    content = request.POST.get("content")
    BlogComment.objects.create(blog_id=blog_id, content=content, author=request.user)
    # 重新加载博客详情页
    return redirect(reverse("blog:blog_detail", kwargs={"blog_id": blog_id}))


@require_GET
def search_blog(request):
    # /search?q=xxx
    q = request.GET.get('q')
    # 从博客的标题和内容中查找含有q关键字的博客
    blogs = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'index.html', context={"blogs": blogs})