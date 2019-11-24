#!_*_coding:utf-8_*_
#__author__:"Xiao CC"

import os,sys
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from core import main
if __name__=='__main__':
    main.main()


