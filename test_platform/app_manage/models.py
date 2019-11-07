from django.db import models

# Create your models here.
#创建数据库模型
#创建表
class Project(models.Model):
    """
    项目表
    """
    name = models.CharField("名称", max_length=100, null=False, default="")
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态", default=True)
    updatae = models.DateTimeField("更新时间",auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)



