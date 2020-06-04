#外部文件使用django的models,需要配置django环境
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singletablehw.settings")
    import django
    django.setup()

    from app01 import models
    import datetime
    obj_list = []
    for i in range(1,10):
        obj = models.Book(
            title='葵花宝典第%s式'%i,
            price=20 + i,
            pub_date='198%s-11-11 00:00:00'%i,
            # pub_date=datetime.datetime.now(),

            publish= '吴老板出版社' if i < 5 else '太白出版社',

        )
        obj_list.append(obj)

    models.Book.objects.bulk_create(obj_list)






