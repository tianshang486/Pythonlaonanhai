# os模块:计算一个文件夹下所有文件的大小.这个文件夹下面还有文件夹,不能用walk
# import os
# def dir_size(path):
#     size = 0
#     name_lst = os.listdir(path)
#     for name in name_lst:
#         abs_path = os.path.join(path,name)
#         if os.path.isfile(abs_path):
#             size += os.path.getsize(abs_path)
#         else:
#             ret = dir_size(abs_path)
#             size += ret
#     return size
#
# path = 'D:\python_22'
# ret = dir_size('D:\python_22\day03')

# 堆栈计算方式 能够不用递归只用循环

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
# def menu_func(menu):
#     flag= True
#     while flag:
#         for name in menu:
#             print(name)
#         key = input('>>>').strip()  # 北京
#         if menu.get(key):
#             dic = menu[key]
#             flag = menu_func(dic)    # menu_func(menu['北京'])
#         elif key.upper() == 'B':   # back回退   quit退出
#             return True
#         elif key.upper() == 'Q':
#             return False
#
# menu_func(menu)
# print('wahaha')

def menu_func(menu):
    while True:
        for name in menu:
            print(name)
        key = input('>>>').strip()  # 北京
        if menu.get(key):
            dic = menu[key]
            flag = menu_func(dic)    # menu_func(menu['北京'])
            if not flag: return False
        elif key.upper() == 'B': return True
        elif key.upper() == 'Q': return False

menu_func(menu)