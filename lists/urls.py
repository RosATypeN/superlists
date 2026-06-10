from django.urls import path
from lists import views

urlpatterns = [
    path('new', views.new_list, name='new_list'),        # POST 创建新列表
    path('<int:list_id>/', views.view_list, name='view_list'),  # 查看列表
]