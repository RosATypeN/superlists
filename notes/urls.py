from django.contrib import admin
from django.urls import path, include
from lists import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),       # 根路径显示首页
    path('lists/', include('lists.urls')),        # lists 应用 URL
]