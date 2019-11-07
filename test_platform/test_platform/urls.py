"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #include二级菜单的跳转
from Personal_Center import views as Personal_views
from app_manage import views as manage_views
urlpatterns = [
    #admin后台管理
    path('admin/', admin.site.urls),
    #账户管理
    path('', Personal_views.login),
    path('login/', Personal_views.login),
    path('logout/', Personal_views.logout),
    #项目管理
    # path('manage/', manage_views.mange),
    path('project/', include('app_manage.urls')),

]
