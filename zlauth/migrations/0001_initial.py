# Generated by Django 5.0.3 on 2024-12-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptchaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('captcah', models.CharField(max_length=4)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
