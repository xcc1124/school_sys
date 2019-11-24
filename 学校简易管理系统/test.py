#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
import pickle
class person:
    def __init__(self,name):
        self.name=name

obj=person('xcc')
data=pickle.dumps(obj)
print(data)
# json.dump(obj,open('obj.txt','wb'))