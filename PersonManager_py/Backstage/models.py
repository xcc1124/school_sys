#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
from django.db import models

class user(models.Model):
    """管理员表"""
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=128)

class em_province(models.Model):
    """省份表"""
    na_name = models.CharField(verbose_name='省份', max_length=64)

class em_city(models.Model):
    """城市表"""
    ci_name=models.CharField(verbose_name='城市', max_length=64)
    belong_to=models.ForeignKey(verbose_name='隶属省份',to='em_province',on_delete=models.CASCADE)

class em_nation_choice(models.Model):
    """民族表"""
    na_name=models.CharField(verbose_name='民族',max_length=64)

class departmentld(models.Model):
    """部门表"""
    de_name=models.CharField(verbose_name='部门',max_length=64)
    de_createTime=models.TimeField(verbose_name='登记时间',auto_now_add=True)
    de_bz=models.TextField(verbose_name='备注',blank=True,null=True)

class tb_employee(models.Model):
    """员工表"""
    em_name=models.CharField(verbose_name='姓名',max_length=64)
    em_age=models.PositiveSmallIntegerField(verbose_name='年龄')
    em_sex_choice=((1,'男'),(0,'女'))
    em_sex=models.SmallIntegerField(verbose_name='性别',choices=em_sex_choice)
    em_IDCard=models.PositiveSmallIntegerField(verbose_name='身份证号')
    em_born=models.CharField(verbose_name='出生日期',max_length=32)
    em_nation=models.ForeignKey(verbose_name='民族',to="em_nation_choice",on_delete=models.CASCADE)
    em_marriage_choice=((1,'已婚'),
                        (2,'未婚')
                        )
    em_marriage=models.SmallIntegerField(verbose_name='婚姻状况',choices=em_marriage_choice)
    em_visage_choice=((1,'中共党员'),
                      (2,'共青团员'),
                      (3,'无'))
    em_visage=models.SmallIntegerField(verbose_name='政治面貌',choices=em_visage_choice)
    em_ancestralHone=models.ForeignKey(verbose_name='籍贯',to='em_city',on_delete=models.Model)
    em_tel=models.PositiveSmallIntegerField(verbose_name='电话')
    em_address=models.CharField(verbose_name='联系地址',max_length=64)
    em_afterSchool=models.CharField(verbose_name='毕业学校',max_length=64)
    em_speciality=models.CharField(verbose_name='所学专业',max_length=64)
    em_culture=models.CharField(verbose_name='学历',max_length=64)
    em_startime=models.TimeField(verbose_name='上岗时间')
    em_departmentld=models.ForeignKey(verbose_name='部门名称',to='departmentld',on_delete=models.CharField)
    em_creatime=models.TimeField(verbose_name='登记时间',auto_now_add=True)
    em_createName=models.ForeignKey(verbose_name='登记人名',to='user',on_delete=models.CASCADE)
    em_bz=models.TextField(verbose_name='备注',blank=True,null=True)

class tb_invitejob(models.Model):
    name=models.CharField(verbose_name='姓名',max_length=64)
    sex_choice = ((1, '男'), (0, '女'))
    sex = models.SmallIntegerField(verbose_name='性别', choices=sex_choice)
    age=models.PositiveSmallIntegerField(verbose_name='年龄')
    born = models.CharField(verbose_name='出生日期', max_length=32)
    job=models.CharField(verbose_name='应聘岗位',max_length=64)
    specialty=models.CharField(verbose_name='所学专业',max_length=64)
    culture_choice=((1,'博士'),
                    (2,'硕士'),
                    (3,'本科'),
                    (4,'大专'),
                    (5,'其他'))
    culture=models.SmallIntegerField(verbose_name='学历',choices=culture_choice)
    afterSchool=models.CharField(verbose_name='毕业学校',max_length=64)
    tel=models.PositiveSmallIntegerField(verbose_name='电话')
    address=models.CharField(verbose_name='联系地址',max_length=64)
    createTime=models.TimeField(verbose_name='创建时间',auto_now_add=True)
    bz=models.TextField(verbose_name='备注',blank=True,null=True)

class tb_pay(models.Model):
    """财务支出表"""
    pay_emId=models.ForeignKey(verbose_name='员工号',to='tb_employee',on_delete=models.CASCADE)
    pay_month=models.TimeField(verbose_name='当前月份')
    pay_baseMoney=models.PositiveSmallIntegerField(verbose_name='基本工资')
    pay_overtime=models.PositiveSmallIntegerField(verbose_name='加班工资',default=0)
    pay_age=models.PositiveSmallIntegerField(verbose_name='工龄费',default=0)
    pay_check=models.PositiveSmallIntegerField(verbose_name='考勤费',default=50)
    pay_absent=models.PositiveSmallIntegerField(verbose_name='旷工费',default=0)
    pay_safety=models.PositiveSmallIntegerField(verbose_name='保险费',default=100)

class tb_conference(models.Model):
    """会议记录"""
    man=models.CharField(verbose_name='主持人',max_length=64)
    title=models.CharField(verbose_name='会议主题',max_length=64)
    content=models.TextField(verbose_name='主要内容')
    time=models.TimeField(verbose_name='会议时间')
    address=models.CharField(verbose_name='会议地点',max_length=64)
    join=models.CharField(verbose_name='参与人员',max_length=64)
    bz=models.TextField(verbose_name='备注',blank=True,null=True)

class tb_cj(models.Model):
    """惩罚与奖励"""
    em_id=models.ForeignKey(verbose_name='员工号',to='tb_employee',on_delete=models.CASCADE)
    title=models.CharField(verbose_name='主题',max_length=64)
    type_choice=((1,'奖励'),
                 (2,'惩罚'))
    type=models.SmallIntegerField(choices=type_choice)
    content=models.CharField(verbose_name='内容',max_length=64)
    money=models.PositiveSmallIntegerField(verbose_name='金额')
    time=models.TimeField(verbose_name='惩奖时间')

