# -*- coding: utf-8 -*-
import os
from django.core.mail import send_mail
#无法使用Django环境，需要通过os模块对环境变量进行设置,然后单独运行send_mail.py文件
os.environ['DJANGO_SETTINGS_MODULE'] = 'myBlog.settings'
if __name__ == '__main__':
    send_mail(
        '主题测试邮件',
        '测试内容邮件',
        '396286670@qq.com',
        ['oracledbmaster@163.com'],
    )