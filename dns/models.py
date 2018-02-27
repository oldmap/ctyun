from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=u'类型')

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=u'域名')

    def __str__(self):
        return self.name


class Record(models.Model):
    host = models.CharField(max_length=255, verbose_name=u'主机记录')
    domain = models.ForeignKey("Domain", on_delete='CASCADE', related_name='d_records', verbose_name=u"域名")
    type = models.ForeignKey("Type", on_delete='CASCADE', related_name='t_records',  verbose_name=u'记录类型')
    value = models.CharField(max_length=255, verbose_name=u'记录值')
    priority = models.IntegerField(default=5, verbose_name=u'优先级')

    def __str__(self):
        return "%s -> %s" % (self.host, self.value)

    class Meta:
        unique_together = ('host', 'domain', 'type', 'value', 'priority')

