#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
from core import enroll
from conf import setting
from core import class_every
from core import main
state={
    'admin_data':None,
    'on_state':False
}
def admin():
    while True:
        if state['on_state']==False:
            state['admin_data']=enroll.input_on(setting.db_type[0],setting.log_type['admin'][0])
        if state['admin_data']!=None:
            state['on_state']=True
            input('\033[1;34m回车键继续...\033[0m')
            show='''
    \033[1;35m
       管理员操作v1.0
       欢迎您,管理员%s
    \033[0m\033[1;32m
        1.学校管理(已实现)
        2.班级管理(已实现)
        3.讲师管理(已实现)
        4.学科管理(已实现)
        5.课程管理(懒得弄了,实现思路见readme)
        6.学员管理(已实现)
        7.返回上一级
        8.退出\033[0m
        '''%state['admin_data']['username']
            print(show)
            dic={
                '1':school_ad,
                '2':class_ad,
                '3':teacher_ad,
                '4':subject_ad,
                '5':course_ad,
                '6':student_ad,
                '7':main.main,
                '8':quit
            }
            choice=input('\033[1;34m请输入你的选择:\033[0m')
            if choice in dic:
                dic[choice]()
            else:
                print('\033[1;31mError\033[0m')

def school_ad():
    obj = class_every.admin(state['admin_data']['username'], state['admin_data']['password'])
    while True:
        input('\033[1;34m回车键继续...\033[0m')
        show_choice = '''
        \033[1;35m学校管理v1.0\033[0m\033[1;32m
        1.查看学校
        2.增加学校
        3.修改学校
        4.删除学校
        5.返回上一级
        6.退出
        
\033[1;31m
FBIwarning:如果学校名称已存在,请输入相近似的名称
           检索算法只能索引出最开始输入的数据\033[0m
        \033[0m
                '''
        print(show_choice)
        dic = {
            '1': obj.see_school,
            '2': obj.add_school,
            '3': obj.update_school,
            '4': obj.del_school,
            '5': admin,
            '6':quit
        }
        choice = input('\033[1;34m请输入你的选择:\033[0m')
        if choice in dic:
            dic[choice]()
        else:
            print('\033[1;31m操作数不存在\033[0m')


def class_ad():
    obj = class_every.admin(state['admin_data']['username'], state['admin_data']['password'])
    school_all_name=class_every.school_all_name()    #获取学校对象列表
    if school_all_name!=[]:
        class_every.school_all_show()  # 显示学校名称便于检索
        school = input('\033[1;34m学校名称:\033[0m')
        if school in school_all_name:
            school_obj = class_every.school.look_once(school)
            while True:
                not_boss_class=[]
                for i in class_every.class_num.look(school_obj):
                    if i.boss==None:
                        not_boss_class.append(i.name)
                if not_boss_class!=[]:
                    print('\033[1;31mWARNING:%s没有班主任\033[0m'%not_boss_class)
                input('\033[1;34m回车键继续...\033[0m')
                show = '''
 \033[1;35m 
            (%s)班级操作v1.0\033[0m\033[1;32m
                1.查看班级
                2.增加班级
                3.修改班级
                4.删除班级
                5.返回上一级
                6.退出
\033[1;31m
FBIwarning:如果班级名称已存在,请输入相近似的名称
           检索算法只能索引出最开始输入的数据\033[0m
                \033[0m
                 '''%school_obj.name
                print(show)
                dic = {
                    '1': obj.see_class,
                    '2': obj.add_class,
                    '3': obj.update_class,
                    '4': obj.del_class,
                    '5': admin,
                    '6': quit
                }
                choice = input('\033[1;34m请输入你的选择:\033[0m')
                if choice in dic:
                    if choice=='5'or choice=='6':
                        dic[choice]()
                    else:
                        dic[choice](school_obj)
                else:
                    print('\033[1;31m操作数不存在\033[0m')
        else:
            print('\033[1;31m输入的学校不存在\033[0m')
    else:
        print('\033[1;31m至少要录入一个学校\033[0m')

def teacher_ad():
    obj = class_every.admin(state['admin_data']['username'], state['admin_data']['password'])
    school_all_name = class_every.school_all_name()  # 获取学校名字列表
    if school_all_name != []:
        class_every.school_all_show()  # 显示学校名称便于检索
        school = input('\033[1;34m学校名称:\033[0m')
        if school in school_all_name:
            school_obj = class_every.school.look_once(school)
            while True:
                input('\033[1;34m回车键继续...\033[0m')
                show = '''
     \033[1;35m 
                (%s)教师操作v1.0\033[0m\033[1;32m
                    1.查看教师
                    2.增加教师
                    3.修改教师
                    4.删除教师
                    5.返回上一级
                    6.退出
                    
\033[1;31m
FBIwarning:如果教师名称已存在,请输入相近似的名称
           检索算法只能索引出最开始输入的数据\033[0m
                    \033[0m
                     '''%school_obj.name
                print(show)
                dic = {
                    '1': obj.see_teacher,
                    '2': obj.add_teacher,
                    '3': obj.update_teacher,
                    '4': obj.del_teacher,
                    '5': admin,
                    '6': quit
                }
                choice = input('\033[1;34m请输入你的选择:\033[0m')
                if choice in dic:
                    if choice != '5' and choice!='6':
                        dic[choice](school_obj)
                    else:
                        dic[choice]()
                else:
                    print('\033[1;31m操作数不存在\033[0m')
        else:
            print('\033[1;31m输入的学校不存在\033[0m')
    else:
        print('\033[1;31m至少要录入一个学校\033[0m')

def subject_ad():
    obj = class_every.admin(state['admin_data']['username'], state['admin_data']['password'])
    school_all_obj = class_every.school.look()
    if school_all_obj!=[]:
        class_every.school_all_show()
        school=input('\033[1;34m学校名称:\033[0m')
        if school in class_every.school_all_name():
            school_obj = class_every.school.look_once(school)
            while True:
                input('\033[1;34m回车键继续...\033[0m')
                show='''\033[0m\033[1;32m
    (%s)学科操作v1.0
        1.查看学科
        2.增加学科
        3.修改学科
        4.删除学科
        5.返回上一级
        6.退出
        
\033[1;31m
FBIwarning:如果学科名称已存在,请输入相近似的名称
           检索算法只能索引出最开始输入的数据\033[0m
        \033[0m
                
                '''%(school_obj.name)
                print(show)
                dic={
                    '1':obj.see_subject,
                    '2':obj.add_subject,
                    '3':obj.update_subject,
                    '4':obj.del_subject,
                    '5':admin,
                    '6':quit
                }
                choice=input('\033[1;34m请输入你的选择:\033[0m')
                if choice in dic:
                    if choice=='5' or choice=='6':
                        dic[choice]()
                    else:
                        dic[choice](school_obj)
                else:
                    print('\033[1;31m操作数不存在\033[0m')
        else:
            print('\033[1;31m所输入的学校不存在\033[0m')
    else:
        print('\033[1;31m至少要录入一个学校\033[0m')

def student_ad():
    obj = class_every.admin(state['admin_data']['username'], state['admin_data']['password'])
    school_all_name = class_every.school_all_name()  # 获取学校对象列表
    if school_all_name != []:
        class_every.school_all_show()  # 显示学校名称便于检索
        school = input('\033[1;34m学校名称:\033[0m')
        if school in school_all_name:
            school_obj = class_every.school.look_once(school)
            class_every.class_all_show(school_obj)
            if class_every.class_all_name(school_obj)==[]:
                print('\033[1;31m至少录入一个班级\033[0m')
            else:
                class_name=input('\033[1;34m班级名称:\033[0m')
                if class_name not in class_every.class_all_name(school_obj):
                    print('\033[1;31m输入的班级不存在\033[0m')
                else:
                    while True:
                        class_obj=class_every.class_num.look_once(class_name,school_obj)
                        input('\033[1;34m回车键继续...\033[0m')
                        show = '''
 \033[1;35m 
            (%s)学员操作v1.0\033[0m\033[1;32m
                1.查看学员
                2.增加学员
                3.修改学员
                4.删除学员
                5.返回上一级
                6.退出
\033[1;31m
FBIwarning:如果班级名称已存在,请输入相近似的名称
           检索算法只能索引出最开始输入的数据\033[0m
                            \033[0m
                             ''' % class_obj.name
                        print(show)
                        dic = {
                            '1': obj.see_student,
                            '2': obj.add_student,
                            '3': obj.update_student,
                            '4': obj.del_student,
                            '5': admin,
                            '6': quit
                        }
                        choice = input('\033[1;34m请输入你的选择:\033[0m')
                        if choice in dic:
                            if choice == '5' or choice == '6':
                                dic[choice]()
                            else:
                                dic[choice](school_obj,class_obj)
                        else:
                            print('\033[1;31m操作数不存在\033[0m')
        else:
            print('\033[1;31m输入的学校不存在\033[0m')
    else:
        print('\033[1;31m至少要录入一个学校\033[0m')
def course_ad():
    pass