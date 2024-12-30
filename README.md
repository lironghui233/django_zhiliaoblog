# 知了博客系统

一个基于Django开发的前后端不分离博客系统，支持用户注册、登录、发布博客、评论等功能。

## 技术栈

### 后端
- Python 3.10
- Django 5.0.3
- MySQL (数据库)

### 前端
- Bootstrap 5 (UI框架)
- jQuery 3.7.1
- wangEditor (富文本编辑器)
- highlight.js (代码高亮)

## 主要功能

### 用户系统
- ✅ 用户注册（支持邮箱验证）
- ✅ 用户登录（支持记住登录状态）
- ✅ 用户退出

### 博客功能
- ✅ 博客发布（支持富文本编辑）
- ✅ 博客列表展示
- ✅ 博客详情页
- ✅ 博客分类
- ✅ 博客评论
- ✅ 博客搜索

## 项目结构 

django_zhiliaoblog/

├── blog/ # 博客应用

├── zlauth/ # 用户认证应用

├── static/ # 静态文件

│ ├── bootstrap5/ # Bootstrap样式

│ ├── css/ # 自定义样式

│ ├── js/ # JavaScript文件

│ ├── wangeditor/ # 富文本编辑器

│ └── highlight/ # 代码高亮

├── templates/ # 模板文件

├── manage.py # Django管理脚本

└── requirements.txt # 项目依赖

## 安装和运行

1. 克隆项目

   ```bash
   git clone <project-url>
   cd django_zhiliaoblog
   ```

2. 创建虚拟环境

   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   ```

3. 安装依赖

   ```bash
   pip install -r requirements.txt
   ```

4. 配置数据库
- 创建MySQL数据库
- 配置db.cnf文件

```ini
[client]
database = your_database_name
user = your_database_user
password = your_database_password
default-character-set = utf8mb4
```

5. 配置邮箱（用于验证码发送）
    在settings.py中配置以下内容：

  ```python
  EMAIL_HOST = 'smtp.qq.com'
  EMAIL_PORT = 587
  EMAIL_HOST_USER = 'your_email@qq.com'
  EMAIL_HOST_PASSWORD = 'your_email_password'
  ```

6. 运行数据库迁移

   ```bash
   python manage.py migrate
   ```

7. 启动开发服务器

   ```
   python manage.py runserver
   ```

## 使用说明

1. 注册账号：访问 `/auth/register` 进行注册
2. 登录：访问 `/auth/login` 进行登录
3. 发布博客：登录后点击"发布博客"按钮
4. 查看博客：在首页可以查看所有博客列表
5. 搜索博客：使用顶部搜索框搜索博客

## 安装依赖
```
# Web框架
Django==5.0.3

# 数据库
mysqlclient==2.2.4

# 邮件发送
django-smtp-ssl==1.0

# 开发工具
django-debug-toolbar==4.3.0

# 其他依赖
Pillow==10.2.0  # 图片处理
python-dotenv==1.0.1  # 环境变量管理
```



