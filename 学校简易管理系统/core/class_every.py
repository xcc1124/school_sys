#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
from core import path
from conf import setting
from core import logger
from view import admin as admin_1
from core import dirs_handle
from core import new_id
import pickle,datetime,os,re

def school_all_name():
    school_all_obj = school.look()
    school_all_name = []
    for i in school_all_obj:
        school_all_name.append(i.name)
    return school_all_name
def teacher_all_name(school_obj):
    teacher_all_obj=teacher.look(school_obj)
    teacher_all_name=[]
    for i in teacher_all_obj:
        teacher_all_name.append(i.name)
    return teacher_all_name
def class_all_name(school_obj):
    class_all_obj=class_num.look(school_obj)
    class_all_name=[]
    for i in class_all_obj:
        class_all_name.append(i.name)
    return class_all_name
def subject_all_name(school_obj):
    subject_all_obj=subject.look(school_obj)
    subject_all_name=[]
    for i in subject_all_obj:
        subject_all_name.append(i.name)
    return subject_all_name
def student_all_name(school_obj,class_obj):
    student_all_obj=student.look(school_obj,class_obj)
    student_all_name=[]
    for i in student_all_obj:
        student_all_name.append(i.name)
    return student_all_name

def school_all_show():
    if school_all_name()!=[]:
        num=0
        for i in school_all_name():
            num+=1
            print('\033[1;33m%s\033[0m' % i, end='  ')
            if num%5==0:
                print()
        print('')
    else:
        print('\033[1;31m学校数据库为空\033[0m')
def teacher_all_show(school_obj):
    if teacher_all_name(school_obj)!=[]:
        num=0
        for i in teacher_all_name(school_obj):
            num+=1
            print('\033[1;33m%s\033[0m' % i, end='  ')
            if num%10 ==0:
                print()
        print('')
    else:
        print('\033[1;31m教师数据库为空\033[0m')
def class_all_show(school_obj):
    if class_all_name(school_obj)!=[]:
        num=0
        for i in class_all_name(school_obj):
            num+=1
            print('\033[1;33m%s\033[0m' % i, end='  ')
            if num%10== 0:
                print()
        print('')
    else:
        print('\033[1;31m班级数据库为空\033[0m')
def subject_all_show(school_obj):
    if subject_all_name(school_obj)!=[]:
        num=0
        for i in subject_all_name(school_obj):
            num+=1
            print('\033[1;33m%s\033[0m' % i, end='  ')
            if num%10==0:
                print()
        print('')
    else:
        print('\033[1;31m科目数据库为空\033[0m')
def student_all_show(school_obj,class_obj):
    if student_all_name(school_obj,class_obj)!=[]:
        num=0
        for i in student_all_name(school_obj,class_obj):
            num+=1
            print('\033[1;33m%s,%s\033[0m' % i, end='  ')
            if num%10== 0:
                print()
        print('')
    else:
        print('\033[1;31m此班级学生数据库为空\033[0m')
class admin:
    def __init__(self,username,password):
        self.username=username
        self.password=password

#***************************************管理员对学校的操作
    def add_school(self):
        school.add_s(self.username)
    @staticmethod
    def see_school():
        school.see_s()
    @staticmethod
    def update_school():
        school.update_s()
    @staticmethod
    def del_school():
        school.del_s()



#***************************************管理员对讲师的操作
    def add_teacher(self,school_obj):
        teacher.add_t(self.username,school_obj)
    @staticmethod
    def see_teacher(school_obj):
        teacher.see_t(school_obj)
    @staticmethod
    def update_teacher(school_obj):
        teacher.update_t(school_obj)
    @staticmethod
    def del_teacher(school_obj):
        teacher.del_t(school_obj)



#***************************************管理员对班级的操作
    @staticmethod
    def see_class(school_obj):
        class_num.see_c(school_obj)
    def add_class(self,school_obj): #存对象
        class_num.add_c(self.username,school_obj)
    @staticmethod
    def update_class(school_obj):
        class_num.update_c(school_obj)
    @staticmethod
    def del_class(school_obj):
        class_num.del_c(school_obj)
#*****************管理员对科目的操作
    @staticmethod
    def see_subject(school_obj):
        subject.see_su(school_obj)
    def add_subject(self,school_obj):
        subject.add_su(self.username,school_obj)
    @staticmethod
    def update_subject(school_obj):
        subject.update_su(school_obj)
    @staticmethod
    def del_subject(school_obj):
        subject.del_su(school_obj)

    @staticmethod
    def see_student(school_obj,class_obj):
        student.see_stu(school_obj,class_obj)

    def add_student(self, school_obj,class_obj):
        student.add_stu(self.username, school_obj,class_obj)

    @staticmethod
    def update_student(school_obj,class_obj):
        student.update_stu(school_obj,class_obj)

    @staticmethod
    def del_student(school_obj,class_obj):
        student.del_stu(school_obj,class_obj)

class school:
    def __init__(self,name,address,set_account):#学校的名称，地址，创建时间和创建人员
        self.id=new_id.new_id()
        self.name=name
        self.address=address
        self.set_account=set_account
        self.set_time=datetime.datetime.now()
        self.class_num_=0
        self.teacher_num=0
        self.subject_num=0
        self.student_num=0
        self.num=0      #记录班号,只自增不减
        self.student_id=0#记录学好,只自增不减
    def hold(self):                 #单个学校对象保存入pickle文件
        school_catalog_path=path.db_path(setting.db_type[3])
        dirs_handle.new_folder(school_catalog_path,self.id)
        pickle.dump(self,open(os.path.join(self.id,self.id),'wb'))
        dirs_handle.new_folder(os.path.join(school_catalog_path,self.id),'class')
        dirs_handle.new_folder(os.path.join(school_catalog_path,self.id), 'subject')
        dirs_handle.new_folder(os.path.join(school_catalog_path,self.id), 'teacher')
        dirs_handle.new_folder(os.path.join(school_catalog_path,self.id), 'student')
        logger.log('%s保存成功'%self.name,setting.log_type['admin'][1],admin_1.state['admin_data']['id'])
    @staticmethod
    def add_s(username):
        print('     \033[1;36m请输入相关信息\033[0m')
        name = input('\033[1;34m学校名称:\033[0m')
        school_name=school_all_name()
        if name!='':
            if name.isspace() != True:
                if name not in school_name:
                    address = input('\033[1;34m学校地址:\033[0m')
                    if address.isspace()==True or address=='':
                        print('\033[0;31m不能全是空字符\033[0m')
                    else:
                        obj = school(name, address,username)
                        obj.hold()
                else:
                    print('\033[0;31m此学校已存在\033[0m')
            else:
                print('\033[0;31m不能全是空字符\033[0m')
        else:
            print('\033[0;31m不要瞎回车\033[0m')
    @staticmethod
    def look():
        school_obj = []
        school_catalog_path = path.db_path(setting.db_type[3])
        try:
            for i in os.listdir(school_catalog_path):
                dirs_handle.update_path(os.path.join(school_catalog_path,i))
                obj = pickle.load(open(i, 'rb'))
                school_obj.append(obj)
        except Exception:
            pass
        return school_obj
    @staticmethod
    def look_once(name):
        school_obj = None
        for obj in school.look():
            if obj.name == name:
                school_obj = obj
                break
        return school_obj
    @staticmethod
    def show_once(obj):
        s = '''\033[1;33m
        name:%s
        address:%s
        set_name:%s
        set_time:%s
        class_num_:%s
        subject_num:%s
        teacher_num:%s
        student_num:%s
        \033[0m''' % (obj.name, obj.address,obj.set_account,obj.set_time, obj.class_num_,obj.subject_num,obj.teacher_num,obj.student_num)
        print(s)
    @staticmethod
    def see_s():
        school_all_show()
        if school.look()!=[]:
            name=input('\033[1;34m请输入需要查询的学校:\033[0m')
            school_obj=school.look_once(name)
            if school_obj!=None:
                school.show_once(school_obj)
            else:print('\033[1;35m此学校不存在\033[0m')
    @staticmethod
    def update_s():
        school_data=school.look()
        if school_data!=[]:
            school_all_show()
            name = input('\033[1;34m输入需要修改的学校的名称:')
            if name in school_all_name():
                obj=school.look_once(name)
                school.show_once(obj)
                while True:
                    choice=input('\033[1;34m输入需要修改的选项(q=退出):\033[0m')
                    if choice=='set_name'or choice=='set_time' or choice=='class_num_'or choice=='subject_num'or choice=='teacher_num' or choice=='id'or choice=='student_num'or choice=='num'or choice=='student_id':
                        print('\033[1;31m此选项为默认值不可修改\033[0m')
                        continue
                    if choice=='q':
                        break
                    if hasattr(obj,choice)==False:      #判断choice是否在内容项内
                        print('\033[1;31m输入选项不存在\033[0m')
                        continue
                    content = input('\033[1;34m需要修改成什么:\033[0m')
                    if content.isspace()==True or content=='':
                        print('\033[0;31m不能全是空字符\033[0m')
                        continue
                    if getattr(obj,choice)==content:
                        print('\033[1;35m并没有修改内容\033[0m')
                        continue
                    setattr(obj,choice,content)
                    if choice == 'name':
                        if content in school_all_name():
                            print('\033[1;35m新的学校已存在\033[0m')
                            continue
                    school_catalog_path = path.db_path(setting.db_type[3])
                    dirs_handle.update_path(school_catalog_path)
                    pickle.dump(obj, open(os.path.join(obj.id, obj.id), 'wb'))
                    logger.log('%s修改成功' % choice, setting.log_type['admin'][1],admin_1.state['admin_data']['id'])
            else:print('\033[1;35m此学校不存在\033[0m')
        else:print('\033[1;31m学校数据为空\033[0m')
    @staticmethod
    def del_s():
        school_all_show()
        school_data=school_all_name()
        name=input('\033[1;34m输入需要删除的学校的名称:')
        if school_data!= []:
            if name in school_data:
                obj=school.look_once(name)
                school.show_once(obj)
                choice=input('\033[0;31m1.删除')
                if choice=='1':
                    dirs_handle.del_folder(path.db_path(setting.db_type[3]),obj.id)
                    logger.log('%s删除成功'%choice,setting.log_type['admin'][1],admin_1.state['admin_data']['id'])
                else:
                    pass
            else:print('\033[1;31m学校不存在\033[0m')
        else:print('\033[1;31m数据为空\033[0m')

class class_num:
    def __init__(self,name,max_p,subject_n,boss,id_,username): #定义一个班号和班级最大容纳人数,所属学校,教学科目
        self.name=name      #
        self.max_p=max_p  #最大人数
        self.subject_n=subject_n  #用列表接收
        self.now_stu_p=0     #初始化学生人数
        self.boss=boss     #班主任
        self.id=new_id.new_id()     #数据关联唯一标识
        self.id_=id_#班号
        self.set_name=username
        self.set_time=datetime.datetime.now()
    @staticmethod
    def look(school_obj):
        class_path=setting.every_path('class',school_obj)
        class_obj = []        #初始化一个列表对象用来存储某学校所有班级对象
        try:                             #读取班级对象，若是没有班级对象则输出空列表
            for item in os.listdir(class_path):
                obj=pickle.load(open(os.path.join(class_path,item),'rb'))
                class_obj.append(obj)
        except Exception:
            pass
        finally:
            return class_obj      #输出的是一个班级对象列表
    @staticmethod
    def look_once(name,school_obj):#某个班级的目录地址
        if class_num.look(school_obj) != []:
            for i in class_num.look(school_obj):
                if i.name == name:
                    break
            return i
    @staticmethod
    def see_c(school_obj):
        if class_num.look(school_obj)==[]:
            print('\033[0;31m班级数据库为空\033[0m')
        else:
            class_all_show(school_obj)
            name=input('\033[1;34m检索的班级名字:\033[0m')
            if name not in class_all_name(school_obj):
                print('\033[0;31m此班级不存在\033[0m')
            else:
                class_obj=class_num.look_once(name,school_obj)
                class_num.show_once(class_obj)
    @staticmethod
    def show_once(class_obj):
        show='''
        \033[1;33m
                name:%s
                id_:%s
                subject_n:%s
                now_stu_p:%s
                max_p:%s
                boss:%s
                set_name:%s
                set_time:%s
                \033[0m
                '''%(class_obj.name,class_obj.id_,class_obj.subject_n,class_obj.now_stu_p,class_obj.max_p,class_obj.boss,class_obj.set_name,class_obj.set_time)
        print(show)
    @staticmethod
    def add_c(username,school_obj):
        if teacher.look(school_obj)==[]:
            print('\033[0;31m请先录入至少一名老师\033[0m')
        else:
            not_boss=[]
            for i in teacher.look(school_obj):
                if i.boss==None:
                    not_boss.append(i.name)
            if not_boss==[]:
                print('\033[0;31m至少要有一名老师没有充当班主任\033[0m')
            else:
                print('     \033[1;36m请输入相关信息\033[0m')
                class_name=input('\033[1;34m班级名称:\033[0m')
                class_all_=class_all_name(school_obj)
                if class_name in class_all_:
                    print('\033[0;31m此班名已存在\033[0m')
                else:
                    while True:
                        max_p=input('\033[1;34m最大人数(max<=100):\033[0m')
                        try:
                            max_p=int(max_p)
                        except ValueError:
                            print('\033[1;31m请输入数字\033[0m')
                            continue
                        else:
                            if max_p>100 and max_p<=0:
                                print('\033[1;31m班级容量异常\033[0m')
                                continue
                            else:
                                break
                    if subject.look(school_obj)==[]:
                        print('\033[0;31m科目数据为空,请录入科目信息再修改班级信息\033[0m')
                        subject_n=[]
                    else:
                        subject_all_show(school_obj)
                        subject_n=[]      #初始化一个列表用于接收科目信息
                        while True:
                            subject_inp=input('\033[1;34m科目(上述列表中,q=退出):\033[0m')
                            if subject_inp=='q':
                                break
                            if subject_inp not in subject_all_name(school_obj):
                                print('\033[0;31m本学校没有此门科目\033[0m')
                            else:
                                subject_n.append(subject_inp)
                    if subject_n==[]:
                        print('\033[0;31m没有录入科目,请过后修改录入科目\033[0m')
                    while True:
                        print('\033[0;35m以下是我校未充当班主任的老师\033[0m')
                        for i in not_boss:
                            print('\033[1;36m%s\033[0m'%i,end='  ')
                        print()
                        boss=input('\033[1;34m班主任:\033[0m')
                        if boss not in not_boss:
                            print('\033[0;31m请输入未充当班主任老师的名字\033[0m')
                            continue
                        else:
                            break
                    school_obj.class_num_+=1
                    school_obj.num+=1
                    class_id_=school_obj.num
                    class_obj=class_num(class_name,max_p,subject_n,boss,class_id_,username) #创建班级对象
                    #保存数据
                    class_path=setting.every_path('class',school_obj)
                    school_path=os.path.dirname(class_path)
                    teacher_path=setting.every_path('teacher',school_obj)
                    teacher_boss_obj=teacher.look_once(boss,school_obj)
                    teacher_boss_obj.boss=class_name
                    pickle.dump(class_obj,open(os.path.join(class_path,class_obj.id),'wb'))
                    pickle.dump(school_obj,open(os.path.join(school_path,school_obj.id),'wb'))
                    pickle.dump(teacher_boss_obj,open(os.path.join(teacher_path,teacher_boss_obj.id),'wb'))
                    logger.log('班级%s保存成功' % class_obj.id_, setting.log_type['admin'][1],admin_1.state['admin_data']['id'])

    @staticmethod
    def update_c(school_obj):
        teacher_path=setting.every_path('teacher',school_obj)
        class_path=setting.every_path('class',school_obj)
        if class_num.look(school_obj)==[]:
            print('\033[0;31m班级数据库为空\033[0m')
        else:
            class_all_show(school_obj)
            name=input('\033[1;34m修改的班级名:\033[0m')
            if name not in class_all_name(school_obj):
                print('\033[0;31m此班级不存在\033[0m')
            else:
                class_obj=class_num.look_once(name,school_obj)
                class_num.show_once(class_obj)
                while True:
                    choice=input('\033[1;34m修改的选项(q=退出):\033[0m')
                    if choice=='q':
                        break
                    if choice=='set_name' or choice=='set_time' or choice=='now_stu_p'or choice=='id'or choice=='id_':
                        print('\033[0;31m此选项为默认选项,不可修改\033[0m')
                        continue
                    if choice=='name':
                        content = input('\033[1;34m内容:\033[0m')
                        if content==class_obj.name:
                            print('\033[0;31m并没有修改内容\033[0m')
                            continue
                        if content in class_all_name(school_obj):
                            print('\033[0;31m此班名已存在\033[0m')
                            continue
                        class_obj.name=content
                        teacher_obj=teacher.look_once(class_obj.boss)
                        teacher_obj.boss=content
                        pickle.dump(teacher_obj,open(os.path.join(teacher_path,teacher_obj.id),'wb'))
                    elif choice=='boss':
                        not_boss = []
                        for i in teacher.look(school_obj):
                            if i.boss == None:
                                not_boss.append(i.name)
                        if not_boss == []:
                            print('\033[0;31m没有可以充当班主任的老师了\033[0m')
                            continue
                        print('\033[0;35m以下是我校未充当班主任的老师\033[0m')
                        for i in not_boss:
                            print('\033[1;36m%s\033[0m' % i, end='  ')
                        print()
                        boss = input('\033[1;34m班主任:\033[0m')
                        if boss in not_boss:
                            new_boss_obj=teacher.look_once(boss,school_obj)
                            new_boss_obj.boss=class_obj.name
                            old_boss_obj=teacher.look_once(class_obj.boss,school_obj)
                            old_boss_obj.boss=None
                            class_obj.boss=boss
                            #********************老师数据修改
                            pickle.dump(old_boss_obj,open(os.path.join(teacher_path,old_boss_obj.id),'wb'))
                            pickle.dump(new_boss_obj,open(os.path.join(teacher_path,new_boss_obj.id),'wb'))
                    elif choice=='max_p':
                        try:
                            max_p=int(input('\033[1;34m最大人数:\033[0m'))
                        except ValueError:
                            print('\033[0;31m请输入数字\033[0m')
                            continue
                        if max_p>0 and max_p<=100:
                            class_obj.max_p=max_p
                        else:
                            print('\033[0;31m班级容量异常\033[0m')
                            continue
                    elif choice=='subject_n':
                        subject_n=class_obj.subject_n
                        print('\033[1;33m此学校科目:\033[0m',end='')
                        subject_all_show(school_obj)
                        print('\033[1;33m班级已存在:%s\033[0m'%class_obj.subject_n)
                        while True:
                            subject=input('\033[1;34m科目名(已存在=删除,未存在=增加,q=退出):\033[0m')
                            if subject=='q':
                                break
                            if subject in subject_n:
                                subject_n.remove(subject)
                                print('\033[0;31m此科目已删除\033[0m')
                            elif subject not in subject_all_name(school_obj):
                                print('\033[0;31m此科目不存在\033[0m')
                                continue
                            else:
                                subject_n.append(subject)
                                continue
                        class_obj.subject_n=subject_n
                pickle.dump(class_obj,open(os.path.join(class_path,class_obj.id),'wb'))
                logger.log('班级%s修改成功' % class_obj.name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])

    @staticmethod
    def del_c(school_obj):
        class_all_show(school_obj)
        class_path=setting.every_path('class',school_obj)
        teacher_path=setting.every_path('teacher',school_obj)
        school_path=os.path.dirname(class_path)
        if class_num.look(school_obj)==[]:
            pass
        else:
            name=input('\033[1;34m班名:\033[0m')
            if name not in class_all_name(school_obj):
                print('\033[0;31m此班名不存在\033[0m')
            else:
                class_obj=class_num.look_once(name,school_obj)
                class_num.show_once(class_obj)
                choice=input('\033[1;31m1.删除\033[0m')
                if choice=='1':
                    school_obj.class_num_-=1
                    teacher_obj=teacher.look_once(class_obj.boss,school_obj)
                    teacher_obj.boss=None
                    pickle.dump(teacher_obj,open(os.path.join(teacher_path,teacher_obj.id)))
                    pickle.dump(school_obj,open(os.path.join(school_path,school_obj.id),'wb'))
                    os.remove(os.path.join(class_path,class_obj.id))
                    logger.log('班级%s删除成功' % class_obj.name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])
                else:
                    pass

class subject:
    def __init__(self,name,set_name):
        self.id=new_id.new_id()
        self.name=name
        self.set_name=set_name
        self.set_time=datetime.datetime.now()
    @staticmethod
    def add_su(username,school_obj):
        subject_path = setting.every_path('subject', school_obj)
        school_path=os.path.dirname(subject_path)
        print('     \033[1;36m请输入相关信息\033[0m')
        name=input('\033[1;34m科目名:\033[0m')
        if name==''or name.isspace()==True:
            print('\033[0;31m不能全为空字符\033[0m')
        else:
            if name in subject_all_name(school_obj):
                print('\033[0;31m此科目已存在\033[0m')
            else:
                subject_obj=subject(name,username)
                school_obj.subject_num+=1
                pickle.dump(subject_obj,open(os.path.join(subject_path,subject_obj.id),'wb'))
                pickle.dump(school_obj,open(os.path.join(school_path,school_obj.id),'wb'))
                logger.log('科目%s保存成功' % name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])
    @staticmethod
    def see_su(school_obj):
        if subject.look(school_obj)==[]:
            print('\033[0;31m科目数据库为空\033[0m')
        else:
            subject_all_show(school_obj)
            subject_name=input('\033[1;34m检索的科目名:\033[0m')
            if subject_name not in subject_all_name(school_obj):
                print('\033[0;31m此科目不存在\033[0m')
            else:
                subject.show_once(subject_name,school_obj)
    @staticmethod
    def show_once(subject_name,school_obj):
        subject_obj=subject.look_once(subject_name,school_obj)
        show='''\033[1;33m
                name:%s
                set_name:%s
                set_time:%s
                \033[0m''' %(subject_obj.name,subject_obj.set_name,subject_obj.set_time)
        print(show)
    @staticmethod
    def class_use(subject_name,school_obj):
        class_all=class_num.look(school_obj)#[]
        class_use_=[]#记录使用此科目的班级对象
        if class_all!=[]:
            for i in class_all:
                if i.subject_n!=[]:
                    for j in i.subject_n:
                        if j==subject_name:
                            class_use_.append(i)
        return class_use_
    @staticmethod
    def update_su(school_obj):
        if subject.look(school_obj)==[]:
            print('\033[0;31m科目数据库为空\033[0m')
        else:
            subject_all_show(school_obj)
            subject_path=setting.every_path('subject',school_obj)
            subject_name=input('\033[1;34m修改的科目名:\033[0m')
            if subject_name not in subject_all_name(school_obj):
                print('\033[0;31m此科目不存在\033[0m')
            else:
                subject.show_once(subject_name,school_obj)
                subject_obj=subject.look_once(subject_name,school_obj)
                while True:
                    choice=input('\033[1;34m修改的选项(q=退出):\033[0m')
                    if choice=='q':
                        break
                    if choice=='id' or choice=='set_name' or choice=='set_time':
                        print('\033[0;31m此选项为默认选项\033[0m')
                        continue
                    if hasattr(subject_obj,choice)==False:
                        print('\033[0;31m此选项不存在\033[0m')
                        continue
                    content=input('\033[1;34m修改成什么:\033[0m')
                    if content==''or content.isspace()==True:
                        print('\033[0;31m不能全为空\033[0m')
                        continue
                    if getattr(subject_obj,choice)==content:
                        print('\033[0;31m并没有更改内容\033[0m')
                        continue
                    if choice=='name':
                        if content in subject_all_name(school_obj):
                            print('\033[0;31m此科目名已存在\033[0m')
                            continue
                        if subject.class_use(subject_obj.name, school_obj) != []:
                            for i in subject.class_use(subject_obj.name, school_obj):
                                i.subject_n.remove(subject_obj.name)
                                i.subject_n.append(content)
                                pickle.dump(i, open(os.path.join(setting.every_path('class', school_obj), i.id), 'wb'))
                    setattr(subject_obj,choice,content)
                    pickle.dump(subject_obj,open(os.path.join(subject_path,subject_obj.id),'wb'))
                    logger.log('科目%s修改成功' % subject_obj.name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])
    @staticmethod
    def del_su(school_obj):
        if subject.look(school_obj) == []:
            print('\033[0;31m科目数据库为空\033[0m')
        else:
            subject_all_show(school_obj)
            subject_path = setting.every_path('subject', school_obj)
            school_path=os.path.dirname(subject_path)
            subject_name = input('\033[1;34m删除的科目名:\033[0m')
            if subject_name not in subject_all_name(school_obj):
                print('\033[0;31m此科目不存在\033[0m')
            else:
                subject_obj=subject.look_once(subject_name,school_obj)
                subject.show_once(subject_name,school_obj)
                choice=input('\033[0;31m1.删除\033[0m')
                if choice=='1':
                    if subject.class_use(subject_name,school_obj)!=[]:
                        for i in subject.class_use(subject_name,school_obj):
                            i.subject_n.remove(subject_name)
                            pickle.dump(i,open(os.path.join(setting.every_path('class',school_obj),i.id),'wb')) #把班级的删除的科目删除
                    school_obj.subject_num-=1
                    pickle.dump(school_obj,open(os.path.join(school_path,school_obj.id),'wb'))
                    os.remove(os.path.join(subject_path,subject_obj.id))
                    logger.log('科目%s删除成功' % subject_obj.name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])
                else:
                    pass
    @staticmethod
    def look(school_obj): #返回一个科目数据,如果数据不存在就返回[]并且创建一个文件保存[]
        subject_path=setting.every_path('subject',school_obj)
        subject_all_obj=[]
        try:
            for i in os.listdir(subject_path):
                subject_obj=pickle.load(open(os.path.join(subject_path,i),'rb'))
                subject_all_obj.append(subject_obj)
        except Exception:
            pass
        return subject_all_obj
    @staticmethod
    def look_once(name,school_obj):
        if name in subject_all_name(school_obj):
            for i in subject.look(school_obj):
                if i.name==name:
                    break
            return i
class student:
    def __init__(self,name,student_id,age,sex,phone,address,class_name,username):
        self.name=name
        self.id=new_id.new_id()
        self.student_id=student_id
        self.age=age
        self.sex=sex
        self.phone=phone
        self.address=address
        self.class_name=class_name
        self.set_name=username
        self.set_time=datetime.datetime.now()
    @staticmethod
    def add_stu(username,school_obj,class_obj):
        student_path=setting.every_path('student',school_obj)
        class_path=setting.every_path('class',school_obj)
        school_path=os.path.dirname(student_path)
        while True:
            student_name=input('\033[1;34m姓名(q,enter=退出):\033[0m') #不判断
            if student_name=='q'or student_name.isspace()==True or student_name=='':
                break
            while True:
                student_age=input('\033[1;34m年龄:\033[0m')
                if re.findall('^\d*',student_age)!=[]:
                    if len(re.findall('^\d*',student_age)[0])==len(student_age):
                        break
                else:
                    print('\033[1;31m请输入纯数字\033[0m')
            while True:
                student_sex=input('\033[1;34m性别(男or女):\033[0m')
                if student_sex=='男' or student_sex=='女':
                    break
                else:
                    print('\033[1;31m请输入男或女\033[0m')
                    continue
            while True:
                phone=input('\033[1;34m手机(11位纯数字):\033[0m')
                if re.findall('^\d{11}',phone)!=[] and len(phone)==11:
                    break
                else:
                    print('\033[1;31m请输入11位数字:\033[0m')
                    continue
            address=input('\033[1;34m地址:\033[0m')
            school_obj.student_id+=1
            school_obj.student_num+=1
            class_obj.now_stu_p+=1
            student_obj=student(student_name,school_obj.student_id,student_age,student_sex,phone,address,class_obj.name,username)
            pickle.dump(school_obj,open(os.path.join(school_path,school_obj.id),'wb'))
            pickle.dump(student_obj,open(os.path.join(student_path,student_obj.id),'wb'))
            pickle.dump(class_obj,open(os.path.join(class_path,class_obj.id),'wb'))
            logger.log('学员%s保存成功' % student_obj.name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])
    @staticmethod
    def update_stu(school_obj,class_obj):
        student_obj=student.see_stu(school_obj,class_obj)
        if student_obj!=None:
            student_path=setting.every_path('student',school_obj)
            while True:
                choice=input('\033[1;34m需要修改的选项(q=退出):\033[0m')
                if choice=='q':
                    break
                if choice=='id' or choice=='student_id' or choice=='set_name' or choice=='set_set_time'or choice=='class_name':
                    print('\033[1;31m此选项为默认选项\033[0m')
                    continue
                if hasattr(student_obj,choice)==False:
                    print('\033[1;31m选项不存在\033[0m')
                    continue
                content=input('\033[1;34m内容:\033[0m')
                if getattr(student_obj,choice)==content:
                    print('\033[1;31m并没有修改内容\033[0m')
                    continue
                setattr(student_obj,choice,content)
                pickle.dump(student_obj,open(os.path.join(student_path,student_obj.id),'wb'))
                logger.log('学员%s修改成功' % student_obj.name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])
        else:
            pass
    @staticmethod
    def see_stu(school_obj,class_obj):#用学号查找
        student_all_show(school_obj,class_obj)
        student_id=input('\033[1;34m学号:\033[0m')
        try:
            student_id=int(student_id)
        except ValueError:
            print('\033[1;31m学号为纯数字\033[0m')
        else:
            student_obj=student.look_once(school_obj,student_id)
            if student_obj==None:
                print('\033[1;31m此人不存在\033[0m')
            else:
                student.show_once(student_obj)
                return student_obj
    @staticmethod
    def del_stu(school_obj,class_obj):
        student_obj=student.see_stu(school_obj,class_obj)
        if student_obj!=None:
            choice=input('\033[1;31m1.删除\033[0m')
            if choice=='1':
                class_name=student_obj.class_name
                class_obj=class_num.look_once(class_name,school_obj)
                class_path=setting.every_path('class',school_obj)
                student_path=setting.every_path('student',school_obj)
                school_path=os.path.dirname(class_path)
                class_obj.now_stu_p-=1
                school_obj.student_num-=1
                pickle.dump(class_obj,open(os.path.join(class_path,class_obj.id),'wb'))
                pickle.dump(school_obj,open(os.path.join(school_path,school_obj.id),'wb'))
                os.remove(os.path.join(student_path,student_obj.id))
                logger.log('学生%s删除成功' % student_obj.name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])
            else:
                pass
        else:
            pass

    @staticmethod
    def look(school_obj,class_obj):
        student_path=setting.every_path('student',school_obj)
        student_all_obj=[]
        try:
            for item in os.listdir(student_path):
                student_obj=pickle.load(open(os.path.join(student_path,item),'rb'))
                if student_obj.class_name==class_obj.name:
                    student_all_obj.append(student_obj)
        except Exception:
            pass
        return student_all_obj
    @staticmethod
    def look_once(school_obj,student_id):
        student_path=setting.every_path('student',school_obj)
        try:
            for item in os.listdir(student_path):
                student_obj=pickle.load(open(os.path.join(student_path,item),'rb'))
                if student_obj.student_id==student_id:
                    return student_obj
        except Exception:
            pass
    @staticmethod
    def show_once(student_obj):
        show='''\033[1;33m
        name:%s
        student_id:%s
        sex:%s
        age:%s
        phone:%s
        address:%s
        class_name:%s
        set_name:%s
        set_time:%s\033[0m
        '''%(student_obj.name,student_obj.student_id,student_obj.sex,student_obj.age,student_obj.phone,student_obj.address,student_obj.class_name,student_obj.set_name,student_obj.set_time)
        print(show)
class teacher:       #加一个内部变量存储老师是否为某班班主任，不是班主任则返回False,并且老师的全部值保存为列表中嵌套字典的操作，方便操作
    def __init__(self,name,sex,id_card,hobby,set_name,phone):
        self.id=new_id.new_id()  #讲师的员工号
        self.name=name
        self.hobby=hobby
        self.sex=sex
        self.id_card=id_card
        self.boss=None
        self.set_name=set_name
        self.set_time=datetime.datetime.now()
        self.phone=phone
    @staticmethod
    def add_t(username,school_obj):
        teacher_path=setting.every_path('teacher',school_obj)
        print('     \033[1;36m请输入相关信息\033[0m')
        while True:
            name = input('\033[1;34m教师名称:\033[0m')
            teacher_name = teacher_all_name(school_obj)
            if name!='':
                if name.isspace()!=True:
                    if name not in teacher_name:
                        break
                    else:
                        print('\033[0;31m教师姓名已存在\033[0m')
                else:
                    print('\033[0;31m不能全为空格\033[0m')
            else:
                print('\033[0;31m不要瞎回车\033[0m')
        while True:
            sex=input('\033[1;34m性别(男or女):\033[0m')
            if sex=='男'or sex=='女':
                break
            else:
                print('\033[0;31m仅能输入男或女\033[0m')
        while True:
            id_card=input('\033[1;34m身份证号码(18位纯数字):\033[0m')
            if re.findall('^\d{18}',id_card)!=[] and len(id_card)==18:
                break
            else:
                print('\033[0;31m请输入18位纯数字\033[0m')
        while True:
            phone=input('\033[1;34m手机号码(11位纯数字):\033[0m')
            if re.findall('^\d{11}', phone) != [] and len(phone) == 11:
                break
            else:
                print('\033[0;31m请输入11位纯数字\033[0m')
        hobby=input('\033[1;34m兴趣爱好:\033[0m')
        if hobby=='' or hobby.isspace()==True:
            hobby=='无'
        obj=teacher(name,sex,id_card,hobby,username,phone)
        pickle.dump(obj,open(os.path.join(teacher_path,obj.id),'wb'))
        school_obj.teacher_num+=1                   #学校对象中的老师个数自加1
        pickle.dump(school_obj, open(os.path.join(os.path.dirname(teacher_path),school_obj.id), 'wb'))
        logger.log('教师%s保存成功' % name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])
    @staticmethod
    def look(school_obj):#返回教师对象列表
        teacher_path=setting.every_path('teacher',school_obj)
        teacher_all_obj=[]
        dirs_handle.update_path(teacher_path)
        try:
            for i in os.listdir(teacher_path):
                obj = pickle.load(open(i, 'rb'))
                teacher_all_obj.append(obj)
        except Exception:
            pass
        return teacher_all_obj
    @staticmethod
    def look_once(name,school_obj):
        if teacher.look(school_obj)!=[]:
            for i in teacher.look(school_obj):
                if i.name==name:
                    break
            return i
    @staticmethod
    def show_once(teacher_name,school_obj):
        teacher_obj = teacher.look_once(teacher_name, school_obj)
        s = '''\033[1;33m
                name:%s
                sex:%s
                id_card:%s
                phone:%s
                hobby:%s
                boss:%s
                set_name:%s
                set_time:%s
                \033[0m''' % (teacher_obj.name, teacher_obj.sex,teacher_obj.id_card,teacher_obj.phone,teacher_obj.hobby, teacher_obj.boss, teacher_obj.set_name,teacher_obj.set_time)
        print(s)
    @staticmethod
    def see_t(school_obj):
        if teacher.look(school_obj)!=[]:
            teacher_all_show(school_obj)
            teacher_name=input('\033[1;34m查询的教师名称:\033[0m')
            if teacher_name in teacher_all_name(school_obj):
                teacher.show_once(teacher_name,school_obj)
            else:
                print('\033[0;31m所输入的教师数据为空\033[0m')
        else:
            print('\033[0;31m教师数据库为空\033[0m')
    @staticmethod
    def update_t(school_obj):
        if teacher.look(school_obj) != []:
            teacher_all_show(school_obj)
            teacher_name = input('\033[1;34m需要修改的教师名称:\033[0m')
            if teacher_name in teacher_all_name(school_obj):
                teacher.show_once(teacher_name, school_obj)
                teacher_obj=teacher.look_once(teacher_name,school_obj)
                while True:
                    choice = input('\033[1;34m输入需要修改的选项(q=退出):\033[0m')
                    if choice == 'q':
                        break
                    if choice=='set_time' or choice=='boss' or choice=='set_name' or choice=='id':
                        print('\033[1;31m此选项为默认选项不可修改\033[0m')
                        continue
                    if hasattr(teacher_obj, choice) == False:  # 判断choice是否在内容项内
                        print('\033[1;31m输入选项不存在\033[0m')
                        continue
                    content = input('\033[1;34m需要修改成什么:\033[0m')
                    if content.isspace() == True or content == '':
                        print('\033[0;31m不能全是空字符\033[0m')
                        continue
                    if choice=='sex':
                        if content!='男' and content!='女':
                            print('\033[0;31m性别只能是男or女\033[0m')
                            continue
                    if getattr(teacher_obj, choice) == content:
                        print('\033[1;35m并没有修改内容\033[0m')
                        continue
                    if choice == 'name':
                        if content in teacher_all_name(school_obj):
                            print('\033[1;35m教师名已存在\033[0m')
                            continue
                        if teacher_obj.boss!=None:
                            class_obj=class_num.look_once(teacher_obj.boss,school_obj)
                            class_obj.boss=content
                            pickle.dump(class_obj,open(os.path.join(setting.every_path('class',school_obj),class_obj.id),'wb'))
                            continue
                    if choice=='id_card':
                        if re.findall('^\d{18}',content)!=[] and len(content)==18:
                            break
                        else:
                            print('\033[0;31m请输入18位纯数字\033[0m')
                            continue
                    if choice=='phone':
                        if re.findall('^\d{11}',content)!=[] and len(content)==11:
                            break
                        else:
                            print('\033[0;31m请输入11位纯数字\033[0m')
                            continue
                    setattr(teacher_obj, choice, content)
                teacher_path = setting.every_path('teacher',school_obj)
                pickle.dump(teacher_obj, open(os.path.join(teacher_path, teacher_obj.id), 'wb'))
                logger.log('教师%s修改成功' % teacher_obj.name, setting.log_type['admin'][1],admin_1.state['admin_data']['id'])
            else:
                print('\033[0;31m所输入教师名不存在\033[0m')
        else:
            print('\033[0;31m教师数据库为空\033[0m')
    @staticmethod
    def del_t(school_obj):
        if teacher.look(school_obj)!=[]:
            teacher_all_show(school_obj)
            teacher_name=input('\033[1;34m需要删除的教师姓名\033[0m')
            if teacher_name in teacher_all_name(school_obj):
                teacher.show_once(teacher_name,school_obj)
                choice=input('\033[0;31m1.删除\033[0m')
                if choice=='1':
                    teacher_obj=teacher.look_once(teacher_name,school_obj)
                    if teacher_obj.boss!=None:
                        class_obj = class_num.look_once(teacher_obj.boss, school_obj)
                        class_obj.boss=None
                    pickle.dump(class_obj,open(os.path.join(setting.every_path('class', school_obj), class_obj.id), 'wb'))
                    teacher_path=os.path.join(setting.every_path('teacher',school_obj),teacher_obj.id)
                    os.remove(teacher_path)
                    school_obj.teacher_num-=1
                    pickle.dump(school_obj, open(os.path.join(os.path.dirname(os.path.dirname(teacher_path)),school_obj.id), 'wb'))
                    logger.log('教师%s删除成功' % teacher_name, setting.log_type['admin'][1], admin_1.state['admin_data']['id'])
                else:
                    pass
            else:
                print('\033[1;31m此教师不存在\033[0m')
        else:
            print('\033[1;31m教师数据库为空\033[0m')





