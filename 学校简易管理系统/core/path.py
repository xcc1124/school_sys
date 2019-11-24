#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
from conf import setting
import os
def db_path(db_type):#公共
    path=os.path.join(setting.path,'db',db_type)
    return path
def log_path(log_type):
    path=os.path.join(setting.path,'log',log_type)
    return path
def school_path(db_type,school_id):
    path=os.path.join(db_path(db_type),school_id)
    return path
def every_path(db_type,school_id,db_tpye2):
    path=os.path.join(school_path(db_type,school_id),db_tpye2)
    return path

