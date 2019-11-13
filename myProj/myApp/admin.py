from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CrontabAdmin(admin.ModelAdmin):

    list_display = ('titre', 'status', 'date_add', 'date_upd')
    list_filter = ('status','date_add','date_upd',)
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    ordering = ['titre',]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Crontab, CrontabAdmin)
