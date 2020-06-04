from django.db import models

# Create your models here.

class Menu(models.Model):
    """
    一级菜单表
    """
    title = models.CharField(max_length=12)

    """
        id    title
        1     销售管理
        2     财务管理
    
    """
    icon = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.title

class Permission(models.Model):

    url = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    menus = models.ForeignKey('Menu',null=True,blank=True)
    """
     id   url   title            menus
     1    x     客户展示          2
     2    xx    添加客户          None
     3          删除客户          None
     4          缴费展示          1 
     5          缴费编辑          None
     6          纳税管理          1
     
    
    """
    # is_menu = models.BooleanField(default=False)
    # icon = models.CharField(max_length=16,null=True,blank=True)

    def __str__(self):
        return self.title

class Userinfo(models.Model):

    name = models.CharField(max_length=12)
    password = models.CharField(max_length=32)
    roles = models.ManyToManyField(to='Role')
    def __str__(self):
        return self.name
class Role(models.Model):
    name = models.CharField(max_length=12)
    permissions = models.ManyToManyField(to='Permission')
    def __str__(self):
        return self.name









