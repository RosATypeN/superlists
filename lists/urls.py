from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:list_id>/',
        views.list_page,
        name='list_view'
    ),
]