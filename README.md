# ctyun DNS管理后台

>    v2.0,引入restframework框架，通过restfull格式API，大大简化了后端的逻辑处理过程。几行代码即可替代上个版本大量逻辑处理。

### 简介
>    我们的内网解析是基于bind实现的，众所周知，bind对解析的修改是通过修改一个个zone文件实现的，把所有记录都放在文件里，然后对文件的增删改查时是很不方便也很不安全的，于是做了这么一个将说有解析记录放置在数据库中，再将数据库中记录导入到zone文件，然后rndc reload（前端触发）这样一个web实现的DNS管理后台。

### demo

    (小型云主机，请勿大量测试)
    http://test.dns.ctyun.org:8000/dns/
    username: taoge
    password: qwer1234
    
![demo](https://github.com/xiaotaoliu/ctyun/blob/master/statics/dns/images/demo.png)

### 环境准备
已编译安装好的python3环境（pip pyvenv），我的是python3.6.5(刚更新的)

### 数据库准备
    mysql> create database ctyun default character set utf8;
    mysql> grant all on ctyun.* to ctyun@'%' identified by 'ctyun';

### 克隆代码
    git clone https://github.com/xiaotaoliu/ctyun.git
    
### 创建并激活虚拟环境(可选)
    cd ctyun
    /usr/local/python3.6.5/bin/pyvenv venv
    source venv/bin/activate
    
### 安装依赖包
    pip install -r requirement.txt

### 数据库迁移
    python manage.py makemigrations
    python manage.py migrate

### 创建超级管理员用户
    (venv) [tomcat@GLB_10_96 ctyun]$ python manage.py createsuperuser
    Username (leave blank to use 'tomcat'): admin
    Email address:       
    Password: 
    Password (again): 
    Superuser created successfully.

### 测试运行
    python manage.py runserver 0.0.0.0:8888

### 登陆管理后台：
用户名密码就是刚刚创建的用户名和密码
    
    # 将常用的解析记录类型添加进去:   如A CNAME MX等
    http://172.20.10.96:8888/admin/dns/type/
    
    # 将你要管理的域名添加进去:如 aabb.com  google.com等
    http://172.20.10.96:8888/admin/dns/domain/
    
### 剩下的就可以在前天操作了：
    http://172.20.10.96:8888/


