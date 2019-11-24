#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
import os,shutil
def update_path(path):
    os.chdir(path)

def new_folder(path,name):
    update_path(path)
    os.makedirs(name)

def del_folder(path,name):
    update_path(path)
    shutil.rmtree(name)

def rename_folder(path,old_name,new_name):
    update_path(path)
    os.renames(old_name,new_name)