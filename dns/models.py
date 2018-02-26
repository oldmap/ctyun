from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=u'域名')

    def __str__(self):
        return self.name


class Record(models.Model):
    host = models.CharField(max_length=255, verbose_name=u'主机记录')
    domain = models.ForeignKey("Domain", related_name='records', on_delete='CASCADE', verbose_name=u"域名")
    type_choices = (
        ('0', 'A'),
        ('1', 'CNAME'),
        ('2', 'MX'),
        ('3', 'NS'),
        ('4', 'AAAA'),
        ('5', 'URL显性'),
        ('6', 'URL隐性'),
        ('7', 'SRV记录'),
    )
    type = models.CharField(choices=type_choices, max_length=2, verbose_name=u'记录类型')
    value = models.CharField(max_length=255, verbose_name=u'记录值')
    priority = models.IntegerField(default=5, verbose_name=u'优先级')

    def __str__(self):
        return "%s -> %s" % (self.host, self.value)

    class Meta:
        unique_together = ('host', 'domain', 'type', 'value', 'priority')

