from django.contrib import admin
from app_manage.models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','name','describe','updatae','create_time']  #显示字段
    search_fields = ['name']   # 搜索栏
    list_filter = ['status']   # 过滤器


admin.site.register(Project, ProjectAdmin)