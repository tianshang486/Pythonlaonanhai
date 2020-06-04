from django.contrib import admin
from rbac import models
# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id','url','title','menus']
    list_editable = ['menus',]

admin.site.register(models.Userinfo)
admin.site.register(models.Role)
admin.site.register(models.Menu)
admin.site.register(models.Permission,PermissionAdmin)





