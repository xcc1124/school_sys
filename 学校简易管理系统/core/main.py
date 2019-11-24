#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
from view import admin
from view import student
from view import teacher
def main():
    while True:
        show='''
     \033[1;35m       登录模块v1.0\033[0m\033[1;32m        
        1.管理员(基本实现)
        2.讲师(未实现)
        3.学生(未实现)
        4.退出
\033[1;31m
FBIwarning:请不要自行删除或更改数据,
           否则可能会出现程序报错\033[0m
           \033[0m
            '''
        dic={
            '1':admin.admin,
            '2':teacher.teacher,
            '3':student.student,
            '4':quit
        }
        print(show.strip())
        choice=input('\033[1;34m请输入你的选择:\033[0m')
        print('')
        if choice in dic:
            dic[choice]()
        else:
            print('\033[1;31mError\033[0m')

