#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
from django.contrib.auth.hashers import make_password, check_password

class create_pwd:
    def __init__(self,password):
        self.password=password
    def mk_pwd(self):  #通过自带加密算法加密记录到数据库中
        pwd=make_password(self.password)
        return pwd
    def chk_pwd(self,pwd):#通过密码与加密后的字符串比对得bool值
        bl=check_password(self.password,pwd)
        return bl