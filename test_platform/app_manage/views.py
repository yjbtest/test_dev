from django.shortcuts import render
from django.http import HttpResponseRedirect #导入重定向
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #登陆验证
from app_manage.models import Project #导入数据库模板
from app_manage.forms import ProjectFrom,ProjectEditFrom #导入表单
# Create your views here.
###登陆后的页面
@login_required###视图文件需要验证登陆后才可以请求
def mange(requests):
    """
    项目管理
    :param requests:
    :return:
    """
    project_list = Project.objects.all().order_by('-create_time')
    return render(requests,"project_list.html",{"projects":project_list})


def list_project(requests):
    return render(requests,"project_list.html")

def add_project(requests):
    """
    创建项目
    :param requests:
    :return:
    """
    if requests.method == "POST":
        form = ProjectFrom(requests.POST)#把post请求和表单绑定
        if form.is_valid():#校验表单数据是否有效
            #如果验证通过，取出表单中的值
            # name = form.cleaned_data['name']
            # describe = form.cleaned_data['describe']
            # status = form.cleaned_data['status']
            Project.objects.create(**form.cleaned_data)
        #创建成功以后重定向返回列表页
            return HttpResponseRedirect("/project/")
        else:
            print(form.errors)

    else:
        #把空表单返回给创建项目页面
        form = ProjectFrom()
    return render(requests,'add_project.html',{'form':form})


def edit_project(requests,pid):
    """
    编辑项目
    :param requests:
    :return:
    """
    if requests.method == "POST":
        form = ProjectFrom(requests.POST)  # 把post请求和表单绑定
        if form.is_valid():  # 校验表单数据是否有效
            # 如果验证通过，取出表单中的值
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            #通过pid查询出要更新的数据
            p = Project.objects.get(id=pid)
            #把更新的值重新赋值给查询出来的值
            p.name = name
            p.describe = describe
            p.status = status
            #保存
            p.save()

        # 创建成功以后重定向返回列表页
        return HttpResponseRedirect("/project/")
    else:
        if pid:
            p = Project.objects.get(id=pid)
            #把要修改的对象通过instance传入form组件中
            form = ProjectEditFrom(instance=p)
        else:
            form = ProjectFrom()
        return render(requests, "project_edit.html", {"form": form, "id": pid})

def del_project(requests,pid):
    """
    删除项目
    :param requests:
    :return:
    """
    if requests.method == "GET":
        p = Project.objects.get(id=pid)
        # 删除
        p.delete()
        # 删除成功以后重定向返回列表页
    return HttpResponseRedirect("/project/")
