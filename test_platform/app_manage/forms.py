#表单文件
from django import forms
from django.forms import widgets #导入样式库
from app_manage.models import Project
#利用django提供的表单模板创建表单

#定义form表单
class ProjectFrom(forms.Form):
    name = forms.CharField(label="名称",
                           max_length = 50,
                           min_length = 1,
                           required=True,
                           widget = widgets.TextInput(attrs={'class': "form-control"}),
                           error_messages={'required': '用户名不能为空'},
                           )#attrs={'class': "form-control"}定义表单样式
    describe = forms.CharField(label="描述",
                               widget=widgets.Textarea(attrs={'class': "form-control"}))
    status = forms.BooleanField(label="状态",required=False)


class ProjectEditFrom(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','describe','status',]

