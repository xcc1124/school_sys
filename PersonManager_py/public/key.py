#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
#此模块用于前台与后台数据交互时密码加密
from Cryptodome import Random
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from urllib import parse
import base64

def create_rsa_key():
    random_generator=Random.new().read
    key=RSA.generate(1024,random_generator)
    private_key=key.exportKey().decode('utf8')       #私钥用于后台解密
    public_key=key.publickey().exportKey().decode('utf8')  #公钥用于前台加密
    return private_key,public_key

def Decrypt(private_key,ciphertext):#根据秘钥和密文解密
    cipher_rsa = PKCS1_v1_5.new(RSA.import_key(private_key.encode()))
    ret = cipher_rsa.decrypt(base64.b64decode(ciphertext),None)
    if ret!=None:
        return ret.decode()
    else:
        return None