#encoding=utf8
from JDPackage import *
from sys import *
#DOCS : https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/account.md
jdid=sys.argv[1]
jdpwd=sys.argv[2]
rkid=sys.argv[3]
rkpwd=sys.argv[4]
a=Account(jdid, jdpwd, rkid, rkpwd) #新建账号a
a.login_pc() #账号PC端登录
# a.login()   #账号M端登录

a.get_couponlist() #获取优惠券列表
a.get_msglist() #获取消息列表
a.get_payment() #获取订单列表

# b=Account('#', '#', '#', '#') #新建账号b
# b.login_pc() #账号PC端登录
# b.login()   #账号M端登录

# b.get_couponlist() #获取优惠券列表
# b.get_msglist() #获取消息列表
# b.get_payment() #获取订单列表
