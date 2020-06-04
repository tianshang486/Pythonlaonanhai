from django.shortcuts import render
from app01 import models

# Create your views here.
def index(request):
    # 创建记录方式1
    # student_obj = models.Student(
    #     name='dazhaung',
    #     age=23,
    # )
    # student_obj.save()
    # 创建记录方式2
    # new_obj = models.Student.objects.create(name='xiaozhuang2',age=6)
    # print(new_obj)  #Student object --  model对象
    # print(new_obj.name)
    # print(new_obj.age)
    #
    # 创建方式3 批量创建
    # objs_list = []
    # for i in range(100,3000000):
    #     obj = models.Student(
    #         name='xiangxixxx',
    #         age = 10,
    #     )
    #     objs_list.append(obj)
    #
    # models.Student.objects.bulk_create(objs_list)
    #
    # 创建方法4 update_or_create 有就更新,没有就创建
    # models.Student.objects.update_or_create(
    #     id=1,
    #     defaults={
    #         'age':38,
    #     }
    # )



    # 简单查询
    # 查询所有的数据  .all方法 返回的是queryset集合
    # all_objs = models.Student.objects.all()
    # #<QuerySet [<Student: Student object>, <Student: Student object>, <Student: Student object>]> -- 类似于列表  --  queryset集合
    # # for i in all_objs:
    # #     print(i.name)
    # print(all_objs)
    #
    # 条件查询  .filter方法,返回的也是queryset集合,查询不到内容,不会 报错,返回一个<QuerySet []>空的queryset
    # objs = models.Student.objects.filter(id=2)  #找id为2的那条记录
    # print(objs) #<QuerySet [<Student: xiaozhuang>]>
    # objs = models.Student.objects.filter(name='dazhaung')
    # print(objs) #<QuerySet [<Student: dazhaung>]>
    #
    # 条件查询 get方法,返回的是model对象,而且get方法有且必须只有1个结果
    # obj = models.Student.objects.get(id=3)  #找id为3的那条记录
    # print(obj)  #xiaozhuang2

    # obj = models.Student.objects.get(name='红旭妹妹')
    # obj = models.Student.objects.get(name='红旭妹妹2')
    # print(obj) #报错1:数据查询结果多于一个: get() returned more than one Student -- it returned 2!
    # print(obj) #报错2:没有查到任何内容:Student matching query does not exist.


    # 删除  delete  queryset 和model对象都可以调用
    # models.Student.objects.get(id=3).delete()  #model对象来调用的delete方法
    # models.Student.objects.filter(name='红旭妹妹').delete() #
    # models.Student.objects.all().delete() #删除所有

    # 更新 update方法 model对象不能调用更新方法 报错信息'Student' object has no attribute 'update'
    # 只能queryset调用,如果
    # models.Student.objects.get(name='红旭妹妹').update(age=38)
    # models.Student.objects.filter(name='红旭妹妹').update(age=38)



    # models.Student.objects.filter(id=7,name='大壮哥哥',age=78).update(
    #     name='大壮禅师',
    #     age=78
    # )
    #打伞形式传参
    # models.Student.objects.filter(**{'id':7,'name':'大壮禅师'}).update(age=100)

    # exclude(**kwargs): 排除,objects控制器和queryset集合都可以调用,返回结果是queryset类型
    # query = models.Student.objects.exclude(id=1)
    # print(query)
    # query = models.Student.objects.filter(age=38).exclude(id=6)
    # print(query)

    # order_by排序
    # query = models.Student.objects.all().order_by('age','-id')
    # print(query)
    # query = models.Student.objects.all().order_by('id').reverse()
    # print(query)

    # query = models.Student.objects.all().filter(id=7)
    # print(query)
    # num = models.Student.objects.all().count()
    # print(num)
    # obj = models.Student.objects.all().last()  #model对象
    # print(obj)

    # obj = models.Student.objects.filter(name='红旭妹妹3').exists()


    # print(obj)

    # query = models.Student.objects.filter(age=38) #<QuerySet [<Student: ddd>, <Student: 红旭妹妹>, <Student: 红旭妹妹2>]>
    # print(query)

    # query = models.Student.objects.filter(age=38).values_list('name','age')
    # print(query) #<QuerySet [(1, 'ddd', 38), (6, '红旭妹妹', 38), (29, '红旭妹妹2', 38)]>
    # query = models.Student.objects.filter(age=38).values('name','age')
    # print(query)

    #<QuerySet [{'id': 1, 'name': 'ddd', 'age': 38}, {'id': 6, 'name': '红旭妹妹', 'age': 38}, {'id': 29, 'name': '红旭妹妹2', 'age': 38}]>

    # query = models.Student.objects.filter().distinct()
    # print(query)
    # query = models.Student.objects.all().values('age').distinct()
    # print(query)

    # query = models.Student.objects.filter(id__gte=7)
    # query = models.Student.objects.filter(id__lte=7)
    # print(query)
    # query = models.Student.objects.filter(id__in=[6,8,10])
    # print(query)

    # query = models.Student.objects.filter(age__range=[18,100])
    # query = models.Student.objects.filter(name__contains='妹妹') #字段为字符串类型的
    # query = models.Student.objects.filter(name__icontains='xiang') #字段为字符串类型的
    # query = models.Student.objects.filter(name__iendswith='妹妹') #字段为字符串类型的
    # print(query)

    import datetime
    current_date = datetime.datetime.now()
    # print(current_date) #2019-07-19 12:19:26.385654

    # models.Brithday.objects.create(name='B哥',date=current_date)
    # models.Brithday.objects.create(name='得港10',date='2000-12-08')


    query = models.Brithday.objects.filter(date__year='2000',date__month='12',date__day__gte='08')

    print(query)

    l1 = [11,22]

    return render(request,'index.html',{'l1':l1})



