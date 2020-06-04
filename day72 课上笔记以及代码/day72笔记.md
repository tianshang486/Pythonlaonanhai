

~~~
request.is_ajax()  判断请求是否是ajax请求

~~~



q查询

~~~
search_field = request.GET.get('search_field')  #选择查询的字段,name
    kw = request.GET.get('kw')  #查询关键字  #思宇
    if kw:
        # customer_list = models.Customer.objects.filter(Q(qq__contains=kw)|Q(name__contains=kw))
        # customer_list = models.Customer.objects.filter(**{search_field:kw,search_field2:kw2})  #name__contain=kw,qq__contain=kw2
        q_obj = Q()
        # q_obj.connector = 'or' # 指定q条件查询的连接符   Q(name=kw)|Q(qq=kw2)
        q_obj.children.append((search_field, kw))
        # q_obj.children.append((search_field2, kw2))
        # Q(name=kw)&Q(qq=kw2)
        customer_list = models.Customer.objects.filter(q_obj)  
~~~













