import os
import time

from django.db import transaction
from django.shortcuts import render,redirect,HttpResponse

from admin01.models import EmpList
from loginregist.models import AdminList
import random,string
from loginregist.captcha.image import ImageCaptcha

# Create your views here.


def login(request):
    if request.session.get('login') == 'o':
        return render(request,'loginregistapp/login.html')
    else:
        name = request.COOKIES.get('name')
        pwd = request.COOKIES.get('pwd')
        result = AdminList.objects.filter(name=name,pwd=pwd)
        print(name,pwd)
        if result:
            request.session['login'] = 'ok'
            return redirect('admin01:emplist')
        return render(request,'loginregistapp/login.html')


def loginlogic(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    rem = request.POST.get('remember')
    try:
        with transaction.atomic():
            result = AdminList.objects.filter(name=name,pwd=pwd)
            if result:
                request.session['login'] = 'ok'
                res = redirect('admin01:emplist')
                if rem:
                    res.set_cookie('name',name,max_age=7*24*3600)
                    res.set_cookie('pwd',pwd,max_age=7*24*3600)
                    request.session['login'] = 'ok'
                return res
            return HttpResponse('账户密码错误')
    except:
        print('shibai')


def regist(request):
    return render(request, 'loginregistapp/regist.html')


def registlogic(request):
    name = request.POST.get('username')
    a = AdminList.objects.filter(name=name)
    if a:
        print('name:',name)
        return HttpResponse('此用户名已被注册')
    t_name=request.POST.get('name')
    pwd = request.POST.get('pwd')
    gender = request.POST.get('sex')

    code = request.session.get('code')
    if code.lower() == request.POST.get('number').lower():
        result = AdminList.objects.create(name=name, pwd=pwd, T_name=t_name, gender=gender)
        request.session['login'] = 'o'  # 1
        return redirect('loginregist:login')
    return render(request,'loginregistapp/regist.html')


def getcapthca(request):
    image = ImageCaptcha()   #生成一个验证码图片
    code = random.sample(string.ascii_letters+string.digits,4) #随机生成一个字符列表
    random_code = ''.join(code)  #将字符串转为列表
    # print(random_code)
    request.session['code']=random_code
    data = image.generate(random_code)  #将生成的字符串 写入到 图片上
    return HttpResponse(data,'image/png')

# def codeexchange(request):
#     code = request.session.get('code')
#     if code.lower() == request.POST.get('number').lower():
#         return
def checkname(request):
    name = request.POST.get('name')
    # time.sleep(1)
    result = EmpList.objects.filter(name=name)
    if result:
        return HttpResponse('<img src="/static/img/error_3.jpg" width="15px">')
    else:
        return HttpResponse('<img src="/static/img/right.jpg" width="15px">')

def checkcode(request):
    code = request.POST.get('code')
    # print(code)
    if code.lower() == request.session.get('code').lower():
        return HttpResponse('true1')
    else:
        return HttpResponse('false1')