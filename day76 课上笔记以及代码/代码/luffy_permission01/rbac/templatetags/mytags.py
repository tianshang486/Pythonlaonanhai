from django.conf import settings
from django import template
register = template.Library()

@register.inclusion_tag('menu.html')
def menu(request):
    # menu_list = request.session.get(settings.MENU_KEY)
    menu_dict = request.session.get(settings.MENU_KEY)
    print(menu_dict)
    path = request.path
    # for i in menu_dict:
    #     # print(path,i['permissions__url'])
    #     if path == i['permissions__url']:
    #         i['class'] = 'active'

    return {'menu_dict':menu_dict}







