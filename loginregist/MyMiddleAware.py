from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class MyMiddleAware2(MiddlewareMixin):
    #如果验证成功，则什么一个不用做，否则返回HttpResponse即可响应请求(中断)
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)
        print("init1")


    def process_request(self,request):#强制登录判断
        if "login" not in request.path:#路径中如果没有"login"
            print("登录验证")
            session = request.session #获取session
            print(session.get('login'))
            if session.get("login")=='ok': #判断是否有登录的标记
                print("已登录")
            else:
                print("未登录")
                return render(request, "loginregistapp/login.html") #未登录则，跳转登录页面
        else:
            print("正在登录") #如果路径中"login"则是登录动作本身
    def process_response(self,request,response):
        print("response:",request,response)
        return response #持续返回响应