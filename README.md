# ctyun DNS管理后台

>v2.0,引入restframework框架，通过restfull格式API，大大简化了后端的逻辑处理过程。几行代码即可替代上个版本大量逻辑处理。
####简介
    我们的内网解析是基于bind实现的，众所周知，bind对解析的修改是通过修改一个个zone文件实现的，把所有记录都放在文件里，然后对文件的增删改查时是很不方便也很不安全的，于是做了这么一个将说有解析记录放置在数据库中，再将数据库中记录导入到zone文件，然后rndc reload（前端触发）这样一个web实现的DNS管理后台。

####demo

    (小型云主机，请勿大量测试)
    http://test.dns.ctyun.org:8000/dns/
    username: taoge
    password: qwer1234
    
![demo](https://github.com/xiaotaoliu/ctyun/blob/master/statics/dns/images/demo.png)

