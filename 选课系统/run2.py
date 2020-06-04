import sys
import pickle
USERINFO = r'D:\python_22\ѡ��ϵͳ\userinfo'
STUINFO = r'D:\python_22\ѡ��ϵͳ\stuinfo'

class Course(object):

    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period

class Student(object):
    opt_lst = [('�鿴�γ�', 'show_courses'),('ѡ��γ�','choose_course'),
               ('�鿴��ѡ�γ�', 'show_selected'), ('�˳�', 'exit')]
    def __init__(self,name):
        self.name = name
        self.courses = []

    def show_courses(self):
        pass
    def choose_course(self):
        pass
    def show_selected(self):
        pass
    def exit(self):
        pass

    @staticmethod
    def init(ret):
        with open(STUINFO,'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.name == ret[0]:
                        return obj
                except EOFError:
                    print('û�����ѧ��,�����˲���˼��Ĵ���!')
                    break
                
class Manager(object):
    opt_lst = [('�����γ�','create_course'),('����ѧ��','create_student'),
               ('�鿴�γ�','show_courses'),('�鿴ѧ��','show_students'),
               ('�鿴ѧ������ѡ�γ�','show_stu_course'),('�˳�','exit')]
    def __init__(self,name):
        self.name = name
    def create_course(self):
        pass
    def create_student(self):
        usr = input('username :')
        stu = Student(usr)
        with open(USERINFO,mode = 'a',encoding='utf-8') as f:
            f.write('%s|123456|Student\n'%(usr))
        with open(STUINFO,mode = 'ab') as f:
            pickle.dump(stu,f)
        print('%sѧ�������ɹ�'%stu.name)

    def show_courses(self):
        pass
    def show_students(self):
        pass
    def show_stu_course(self):
        pass
    def exit(self):
        pass

    @classmethod
    def init(cls,ret):
        obj = cls(ret[0])
        return obj

# �û� �����û��� ���� �ж��û��Ƿ�Ϸ��������ɶ?
def login():
    '''

    :return: ��¼�ɹ�:�û���,���
              ��¼ʧ��:False
    '''
    username = input('username :')
    password = input('password :')
    with open(USERINFO,encoding='utf-8') as f:
        for line in f:
            usr,pwd,ident = line.strip().split('|')
            if usr == username and password == pwd:
                return usr,ident
        else:
            return False

ret = login()
if ret:
    print('��¼�ɹ�,%s,��ӭʹ��ѡ��ϵͳ'%ret[0])
    cls = getattr(sys.modules[__name__],ret[1])
    obj = cls.init(ret)
    for index,opt in enumerate(cls.opt_lst,1):
        print(index,opt[0])
    num = int(input('��Ҫѡ��Ĳ��� :').strip())
    if hasattr(obj,cls.opt_lst[num-1][1]):
        getattr(obj,cls.opt_lst[num-1][1])()
else:
    print('��¼ʧ��')


# ����ѧ��
    # ���û������û��� ����
    # ʵ����һ������
    # ���û��� ���� д��userinfo
    # ��ѧ������д��stuinfo�ļ���
