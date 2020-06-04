import re
from collections import OrderedDict

from django.conf import settings
from django import template

register = template.Library()

@register.inclusion_tag('menu.html')
def menu(request):
    # menu_list = request.session.get(settings.MENU_KEY)
    menu_dict = request.session.get(settings.MENU_KEY)
    path = request.path
    keys = sorted(menu_dict, key=lambda x: menu_dict[x]['weight'], reverse=True)
    print(keys)

    order_dict = OrderedDict()

    for key in keys:  # ['1', '2']
        order_dict[key] = menu_dict[key]

    for key,value in order_dict.items():
        value['class'] = 'hidden'
        for i in value['children']:
            # if re.match(i['url'],path):

            if request.current_id == i.get('id'):
                value['class'] = ''
                i['class'] = 'active'

    print(order_dict)
    # print(menu_dict)

    # for i in menu_dict:
    #     # print(path,i['permissions__url'])
    #     if path == i['permissions__url']:
    #         i['class'] = 'active'

    return {'order_dict':order_dict}







