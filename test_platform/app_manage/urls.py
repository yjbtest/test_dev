from django.urls import path
from app_manage import views

urlpatterns = [
    path('',views.mange),
    path('add',views.add_project),
    path('edit/<int:pid>/',views.edit_project),
    path('del/<int:pid>/',views.del_project),
]