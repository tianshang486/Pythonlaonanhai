
from django.conf import settings

def init_permission(request,user_obj):
    request.session['is_login'] = True  # 用来记录是否登录了

    # 登录成功，将权限信息注入到session中
    permission_list = user_obj.roles.values(

        'permissions__pk',
        'permissions__url',
        'permissions__title',
        'permissions__parent_id',
        # 'permissions__title',
        'permissions__menus__pk',
        'permissions__menus__weight',
        'permissions__menus__title',
        'permissions__menus__icon',

    ).distinct()
    print(permission_list)

    menu_list = []  # 菜单栏权限  [{},]
    '''
    {
        一级菜单的id
        2 :{
            'title':'财务管理',
            'icon':'fa-xxx',
            'children':[
                {'url':'/payment/list/','title':'缴费展示' }   # 缴费展示
                {'url':'/nashui/list/','title':'纳税展示' }   # 纳税展示 
            ]
        } ,
        1 :{
            'title':'销售管理',
            'icon':'fa-xxx',
            'children':[
                {'url':'/customer/list/','title':'客户展示' }   # 客户展示

            ]
        }   
    }
    
    '''

    menu_dict = {}
    for i in permission_list:
        if i.get('permissions__menus__pk'):

            if i.get('permissions__menus__pk') in menu_dict:
                menu_dict[i.get('permissions__menus__pk')]['children'].append(

                    {
                        'url': i.get('permissions__url'),
                        'title': i.get('permissions__title'),
                        'id': i.get('permissions__pk')
                    }
                )
            else:
                menu_dict[i.get('permissions__menus__pk')] = {
                    'title': i.get('permissions__menus__title'),
                    'icon': i.get('permissions__menus__icon'),
                    'weight': i.get('permissions__menus__weight'),
                    'children': [
                        {'url': i.get('permissions__url'), 'title': i.get('permissions__title'),'id': i.get('permissions__pk')}

                    ]
                }

    # for permission in permission_list:
    #
    #     is_menu = permission.get('permissions__is_menu')
    #     if is_menu:
    #         menu_list.append(permission)
    # print('menu_list>>>', menu_list)


    # 注入认证权限url

    permission_dict = {}
    for permission in permission_list:
        permission_dict[permission.get('permissions__pk')]=permission
    print('>>>>', permission_dict)
    request.session[settings.PERMISSION_KEY] = permission_dict

    # 注入菜单展示的url
    request.session[settings.MENU_KEY] = menu_dict



