from django.contrib import admin
from dns import models


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'domain', 'type', 'value', 'priority')


class DomainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(models.Domain, DomainAdmin)
admin.site.register(models.Record, RecordAdmin)

