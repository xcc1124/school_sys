#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
from core import enroll
from core import register
from core import main
from conf import setting
def student():
    while True:
        show='''
\033[1;35m      学员模块v1.0\033[0m\033[1;32m
        1.登录
        2.注册
        3.退出\033[0m
    '''
        print(show.strip())
        dic={
            '1':enroll.input_on,
            '2':register.register,
            '3':main.main
        }
        while True:
            choice=input('\033[1;34m请输入你的选择:\033[0m')
            print('')
            if choice in dic:
                if choice=='1'or choice=='2':
                    dic[choice](setting.db_type[2],setting.log_type['student'][0])
                else:
                    dic[choice]()
            else:
                print('\033[1;31mError\033[0m')