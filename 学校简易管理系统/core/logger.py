#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
import logging,os,time
from conf import setting
from core import path
def log(content,log_type,account):
    log_path=os.path.join(path.log_path(log_type),account)
    logger=logging.getLogger()
    logger.setLevel(setting.formatter)
    fh=logging.FileHandler(log_path,encoding='utf-8')
    ch=logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    formatter1 = logging.Formatter('\033[1;33m%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s\033[0m\n')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter1)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.warning(content)
    logger.removeHandler(fh)
    logger.removeHandler(ch)
    time.sleep(0.01)  #短暂阻塞

