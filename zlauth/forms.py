from django import forms
from django.contrib.auth import get_user_model
from .models import CaptchaModel

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, error_messages={
        'required': '请传入用户名！',
        "max_length": "用户名长度在2~20之间！",
        "min_length":"用户名长度在2~20之间！"
    })
    email = forms.EmailField(error_messages={"required":"请传入邮箱","invalid":"请传入一个正确的邮箱"})
    captcha = forms.CharField(max_length=4, min_length=4, error_messages={})
    password = forms.CharField(max_length=20, min_length=6, error_messages={})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exist = User.objects.filter(email=email).exists()
        if exist:
            raise forms.ValidationError("邮箱已经被注册！")
        return email

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        email = self.cleaned_data.get('email')

        captcha_model = CaptchaModel.objects.filter(email=email, captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError("验证码和邮箱不匹配！")

        #删除缓存的captcha记录
        captcha_model.delete()
        return captcha


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={"required": "请传入邮箱", "invalid": "请传入一个正确的邮箱"})
    password = forms.CharField(max_length=20, min_length=6, error_messages={})
    remember = forms.IntegerField(required=False)