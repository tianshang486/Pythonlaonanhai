from django.shortcuts import render,HttpResponse,redirect
from rbac import models
from django.db.models import Q
from django import forms

# Create your views here.


def role_list(request):
    all_roles = models.Role.objects.all()
    return render(request,'rbac/role_list.html',{'all_roles':all_roles})


class RoleForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = '__all__'
        exclude = ['permissions',]
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }



def role_add_edit(request,rid=None):

    role_obj = models.Role.objects.filter(pk=rid).first()
    if request.method == 'GET':
        form_obj = RoleForm(instance=role_obj)

        return render(request,'rbac/form.html',{'form_obj':form_obj})
    else:
        form_obj = RoleForm(request.POST,instance=role_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('role_list')
        else:
            return render(request, 'rbac/form.html', {'form_obj': form_obj})

def role_del(request,rid):
    models.Role.objects.filter(pk=rid).delete()
    return redirect('role_list')


def menu_list(request):
    mid = request.GET.get('mid')

    all_menus = models.Menu.objects.all()
    if mid:
        all_permissions = models.Permission.objects.filter(Q(menus_id=mid)|Q(parent__menus_id=mid)).values('id','url','title','menus__title','menus_id','parent_id','parent__title','url_name')
    else:
        all_permissions = models.Permission.objects.all().values('id','url','title','menus_id','parent_id','menus__title','parent__title','url_name')
    # print(all_permissions)
    '''
        {
            pid:{
                'url':xx,
                'children':[
                    {'url'}
                ]
            },
            pid:{
                'url':xx,
                'children':[
                    {'url'}
                ]
            }
        }
    
    '''
    permission_dict = {}
    for i in all_permissions:
        if i.get('menus_id'):
            permission_dict[i['id']] = i
            i['children'] = []
    for k in all_permissions:
        pid = k.get('parent_id')
        if pid:
            permission_dict[pid]['children'].append(k)

    print('permission_dict',permission_dict)


    return render(request,'rbac/menu_list.html',{'all_menus':all_menus,'permission_dict':permission_dict.values(),'mid':mid})


from rbac.icon_data import icon_list
from django.utils.safestring import mark_safe

class MenuForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = '__all__'
        # exclude = ['permissions',]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'weight':forms.TextInput(attrs={'class':'form-control'}),
            'icon':forms.RadioSelect(choices=[[i[0],mark_safe(i[1])] for i in icon_list]),
        }



def menu_add_edit(request,mid=None):

    menu_obj = models.Menu.objects.filter(pk=mid).first()
    if request.method == 'GET':
        form_obj = MenuForm(instance=menu_obj)
        return render(request,'rbac/form.html',{'form_obj':form_obj})
    else:
        form_obj = MenuForm(request.POST,instance=menu_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('menu_list')
        else:
            return render(request, 'rbac/form.html', {'form_obj': form_obj})

#删除菜单
def menu_del(request,mid):
    models.Menu.objects.filter(pk=mid).delete()
    return redirect('menu_list')







