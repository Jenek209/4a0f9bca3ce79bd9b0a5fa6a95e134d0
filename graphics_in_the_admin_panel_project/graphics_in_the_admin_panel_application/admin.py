from django.contrib import admin
from .models import Function

import django.contrib.auth.admin
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    fields = ['function', 't', 'dt']
    list_display = ('function', 'image_tag', 't', 'dt', 'date')
    


