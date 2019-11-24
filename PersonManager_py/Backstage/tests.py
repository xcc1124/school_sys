from Cryptodome import Random
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from urllib import parse
import base64
message = "hello client, this is a message"
key ="""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC26X6A0WCWiVxdxq3jtm42yDdG
bf+99v2zyi0UMVGZfowlnkcWeMvpz8NBm2UVlrjZpnFr8wFkdHyjFFkq/ilclH3A
N4+Xw8Ap7CGJ2jVMyS5h9RRBUyf3F4D5Og8789Ywh9HXYyvD/6J62EtbbkhGPxg3
aa8n2kfKZ9N6Q7DqrwIDAQAB
-----END PUBLIC KEY-----"""
rsakey = RSA.importKey(key)
cipher = PKCS1_v1_5.new(rsakey)
cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
print(cipher_text.decode('utf-8'))

#eM/YId4Oo1Yb6oN4YXpL4HfnF6ae2169+ouQUW0Wm60t/zgC42s91MD6IKtFVB40+1SrzPI8CBb3SGNVuV8XIrBSyMuPG09c2+uK0GaPSduNTXeq58O0k2/KbiKFcNLjBUbzifEmHkdt/NR4Q1CcO6MKWbUXIKUBaFEmEmAd/HQ=

# random_generator = Random.new().read
# # rsa算法生成实例
# rsa = RSA.generate(1024, random_generator)
# encrypt_text="eM/YId4Oo1Yb6oN4YXpL4HfnF6ae2169+ouQUW0Wm60t/zgC42s91MD6IKtFVB40+1SrzPI8CBb3SGNVuV8XIrBSyMuPG09c2+uK0GaPSduNTXeq58O0k2/KbiKFcNLjBUbzifEmHkdt/NR4Q1CcO6MKWbUXIKUBaFEmEmAd/HQ="
# key = """-----BEGIN RSA PRIVATE KEY-----
# MIICXQIBAAKBgQC26X6A0WCWiVxdxq3jtm42yDdGbf+99v2zyi0UMVGZfowlnkcW
# eMvpz8NBm2UVlrjZpnFr8wFkdHyjFFkq/ilclH3AN4+Xw8Ap7CGJ2jVMyS5h9RRB
# Uyf3F4D5Og8789Ywh9HXYyvD/6J62EtbbkhGPxg3aa8n2kfKZ9N6Q7DqrwIDAQAB
# AoGBAJn5qu1D1FxE24Vxl7ZGPzdMigN227+NaPptak9CSR++gLm2KL+JBpcXt5XF
# +20WCRvnWjl2QijPSpB5s6pWdHezEa1cl6WrqB1jDJd1U99WNCL5+nfEVD9IF+uE
# ig0pnj+wAT5fu78Z0UjxD9307f9S7BLC8ou3dWVkIqob6W95AkEAuPGTNlTkquu/
# wBJTb4/+/2ZCf7Ci9qvsN3+RcrzFkKa3uTtBOa6Xk2R61zBkucUgY6cQHPbxhFLN
# TVmXdbwxTQJBAP0wGenVOq4dCPdz3NhyghkKT6SL2w/SgbrROiJ1mG9MoBq58/0g
# k85I91R7nuvOYTKTUkhWdPYITpDarmPJzesCQGRBmOMgHCHH0NfHV3Gn5rz+61eb
# IoyD4Hapceh4CsWCiyAfzhj9229sTecvdbr68Lb0zphVCdIIrQCca63IShUCQGYI
# e3jzmHlQdCudArQruWgz8pKiVf7TW7qY1O/MKkk4PRFoPP6WoVoxp5LhWtM20Y7b
# Nf628N2xzU+tAThvvE8CQQCI1C7GO3I5EMfqPbTSq2oZq8thvGlyFyI7SNNuvAHj
# hj2+0217B9CcTZqloYln01CNDVuaoUgEvFSw1OdRB1tC
# -----END RSA PRIVATE KEY-----"""
# rsakey = RSA.importKey(key)
# cipher = PKCS1_v1_5.new(rsakey)
# text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
# print(text.decode('utf-8'))
