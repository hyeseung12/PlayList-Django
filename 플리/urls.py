from django.urls import path

from 플리 import views

app_name = '플리'

urlpatterns = [
    path('', views.show_index, name='show_index'),
    path('login/', views.show_login, name='show_login')
]