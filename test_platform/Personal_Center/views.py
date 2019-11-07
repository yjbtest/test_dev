from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect ####url重定向
from django.contrib import auth  ####引入django自带的账号管理体系
from django.contrib.auth.decorators import login_required ###验证视图文件需要登陆
# Create your views here.
###用来写请求的处理逻辑的
def login(requests):
    """
    用户登陆
    :param reqests:
    :return:
    """
    ###返回登陆页面
    if requests.method == "GET":
        return render(requests,"login.html")
    ####处理登陆请求
    if requests.method == "POST":
        username = requests.POST.get("username")
        password = requests.POST.get("password")
        if username == '' or password == "":
            return render(requests,"login.html",{"error":"用户名或密码为空!"})
        ####验证用户是否存在
        user = auth.authenticate(username=username, password=password)
        #####如果验证成功，就重定向跳转到登陆成功后的页面
        if user is not None:
            ####记录用户的登陆状态，登陆成功后记录用户的登陆状态
            auth.login(requests,user)
            return HttpResponseRedirect("/project/")
        else:
            return render(requests, "login.html", {"error": "用户名或者密码错误!"})

# ###登陆后的页面
# @login_required###视图文件需要验证登陆后才可以请求
# def mange(requests):
#     """
#     登陆成功后首页
#     :param requests:
#     :return:
#     """
#     return render(requests,"manage.html")

###退出
def logout(requests):
    """
    退出功能
    :param requests:
    :return:
    """
    ####清缓存
    auth.logout(requests)
    ###重定向到首页
    return HttpResponseRedirect("/")