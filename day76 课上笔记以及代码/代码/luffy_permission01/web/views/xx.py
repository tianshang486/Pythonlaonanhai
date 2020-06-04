data = [{
	'permissions__pk': 1,
	'permissions__url': '/customer/list/',
	'permissions__title': '客户展示',
	'permissions__menus__pk': 1,
	'permissions__menus__title': '客户管理',
	'permissions__menus__icon': 'fa-grav'
}, {
	'permissions__pk': 2,
	'permissions__url': '/customer/add/',
	'permissions__title': '添加客户',
	'permissions__menus__pk': None,
	'permissions__menus__title': None,
	'permissions__menus__icon': None
}, {
	'permissions__pk': 3,
	'permissions__url': '/customer/edit/(?P<cid>\\d+)/',
	'permissions__title': '编辑客户',
	'permissions__menus__pk': None,
	'permissions__menus__title': None,
	'permissions__menus__icon': None
}, {
	'permissions__pk': 9,
	'permissions__url': '/nashui/list/',
	'permissions__title': '纳税管理',
	'permissions__menus__pk': 2,
	'permissions__menus__title': '财务管理',
	'permissions__menus__icon': 'fa-rmb'
}, {
	'permissions__pk': 5,
	'permissions__url': '/payment/list/',
	'permissions__title': '缴费展示',
	'permissions__menus__pk': 2,
	'permissions__menus__title': '财务管理',
	'permissions__menus__icon': 'fa-rmb'
}, {
	'permissions__pk': 6,
	'permissions__url': '/payment/add/',
	'permissions__title': '添加缴费',
	'permissions__menus__pk': None,
	'permissions__menus__title': None,
	'permissions__menus__icon': None
}, {
	'permissions__pk': 7,
	'permissions__url': '/payment/edit/(?P<pid>\\d+)/',
	'permissions__title': '修改缴费',
	'permissions__menus__pk': None,
	'permissions__menus__title': None,
	'permissions__menus__icon': None
}]

# '''
# {
#
#         一级菜单的id-2 :{
#             'title':'财务管理',
#             'icon':'fa-xxx',
#             'children':[
#                 {'url':'/payment/list/','title':'缴费展示' }   # 缴费展示
#                 {'url':'/nashui/list/','title':'纳税展示' }   # 纳税展示
#             ]
#         } ,
#         1 :{
#             'title':'销售管理',
#             'icon':'fa-xxx',
#             'children':[
#                 {'url':'/customer/list/','title':'客户展示' }   # 客户展示
#
#             ]
#         }
#     }
#
# '''
menu_dict = {}
for i in data:
    if i.get('permissions__menus__pk'):

        if i.get('permissions__menus__pk') in menu_dict:
            menu_dict[i.get('permissions__menus__pk')]['children'].append(
                {
                    'url':i.get('permissions__url'),
                    'title':i.get('permissions__title')
                }
            )
        else:
            menu_dict[i.get('permissions__menus__pk')] = {
                'title':i.get('permissions__menus__title'),
                'icon':i.get('permissions__menus__icon'),
                'children':[
                    {'url':i.get('permissions__url'),'title':i.get('permissions__title')}

                ]
            }

print(menu_dict)
        # {
        #     1：
        #     2：{}
        # }

















