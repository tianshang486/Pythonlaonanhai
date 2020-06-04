from django.contrib import admin
from rbac import models
# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id','url','title']

admin.site.register(models.Userinfo)
admin.site.register(models.Role)
admin.site.register(models.Permission,PermissionAdmin)





