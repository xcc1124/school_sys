#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
import os
import logging
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

formatter=logging.DEBUG

log_type={
    'admin':[
        'admin/log_on',
        'admin/handle'
    ],
    'teacher':[
        'teacher/log_on',
        'teacher/handle'
    ],
    'student':[
        'student/log_on',
        'student/handle'
    ]
}

db_type=[
    'admin',
    'teacher',
    'student',
    'school',
    'class',
    'subject'
]
def every_path(type,obj):
    from core import path
    dic={
        'teacher':path.every_path(db_type[3],obj.id,db_type[1]),
        'class':path.every_path(db_type[3],obj.id,db_type[4]),
        'subject':path.every_path(db_type[3], obj.id, db_type[5]),
        'student': path.every_path(db_type[3], obj.id, db_type[2]),
    }
    return dic[type]
