#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
from core import path
from core import logger
import pickle,os
def input_on(db_type,log_type):
    account=input('\033[1;34m账号:\033[0m')
    pwd=input('\033[1;34m密码:\033[0m')
    user_data=enroll(account,pwd,db_type)
    if user_data!=None:
        logger.log('登录成功',log_type,user_data['id'])
    return user_data
def enroll(username,password,db_type):
    data=None
    db_path=path.db_path(db_type)
    try:
        for item in os.listdir(db_path):
            obj=pickle.load(open(os.path.join(db_path,item),'rb'))
            if obj['username']==username:
                data=obj
                break
    except Exception:
        print('\033[1;31m数据库为空,请初始化数据\033[0m')
        exit()
    else:
        if data==None:
            print('\033[1;31m此账户不存在\033[0m')
        else:
            if data['password']==password:
                data['id']=item
                return data
            else:
                print('\033[1;31m密码错误\033[0m')



