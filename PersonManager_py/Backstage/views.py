from django.shortcuts import render,HttpResponse,redirect
from django.forms import fields,widgets
from django import forms
import io,datetime
from public import CAPTCHA as code
from public import pwd,key
from Backstage import models
# Create your views here.


class login_form(forms.Form):
    username=fields.CharField(
        widget=widgets.TextInput(
          attrs={'placeholder':'请输入用户名',
                 }))
    pa=fields.CharField(
        widget=widgets.PasswordInput(
          attrs={'placeholder':'请输入密码',
                 'id':'password_look'
                 }))

def login_test(func):  #登录检测装饰器
    def inner(req,*args,**kwargs):
        is_login=req.session.get('is_login')
        if is_login:
            return func(req,*args,**kwargs)
        else:
            return redirect('B/login.this/')
    return inner

def test(req):
    username='xcc'
    password='123456'
    obj=pwd.create_pwd(password)
    make_password=obj.mk_pwd()
    models.user.objects.create(name=username,password=make_password)
    return HttpResponse("管理员账户初始化完成")

def login(req):
    messge=''
    pwd_messge=''
    obj=login_form()
    private_key, public_key = key.create_rsa_key()
    if req.method=="GET":
        req.session['private_key'] = private_key
        req.session['public_key']=public_key
    elif req.method=="POST":
        obj = login_form(req.POST)
        yz_code=req.session['yz_code']
        yz_code_post=req.POST.get("Code")
        ciphertext=req.POST.get("password")
        password=key.Decrypt(req.session['private_key'],ciphertext)
        if yz_code.lower()==yz_code_post.lower():
            username = req.POST.get('username')
            if models.user.objects.filter(name=username).count()>0:
                _pwd=models.user.objects.get(name=username).password
                pwd_obj=pwd.create_pwd(password)
                if pwd_obj.chk_pwd(_pwd):
                    req.session['is_login']=True
                    req.session['username']=username
                    return redirect('/B/')
            pwd_messge = '用户名或密码错误'
        else:
            messge='验证码错误'
    return render(req, 'Backstage_login.html',{'pwd_messge':pwd_messge,'messge':messge,'obj':obj,'public_key':req.session['public_key']})
def CAPTCHA(req):
    stream=io.BytesIO()
    p,c=code.create_validate_code()
    p.save(stream,"png")
    req.session['yz_code']=c
    return HttpResponse(stream.getvalue())
@login_test
def index(req):
    username=req.session['username']
    now_time=datetime.datetime.now()
    return render(req,'index.html',{"time":now_time,"username":username})

def log_out(req):
    req.session.clear()
    return redirect("/B/login.this")

@login_test
def update_user(req):
    username = req.session['username']
    messge=''
    if req.method=='GET':
        pass
    elif req.method=="POST":
        old_pwd=req.POST.get('old_pwd')
        _pwd=models.user.objects.get(name=username).password
        obj_pwd=pwd.create_pwd(old_pwd)
        if obj_pwd.chk_pwd(_pwd):
            new_pwd=req.POST.get('new_pwd')
            new_y_pwd=req.POST.get('new_y_pwd')
            if new_pwd==new_y_pwd:
                new_obj_pwd=pwd.create_pwd(new_pwd)
                _pwd=new_obj_pwd.mk_pwd()
                models.user.objects.filter(name=username).update(name=username,password=_pwd)
                req.session.clear()
                return redirect("/B/")
            else:
                messge='两次输入值不一致'
        else:
            messge='旧密码错误'

    return render(req,'update_user.html',{'username':username,'messge':messge})