from django.urls import path

from 플리 import views

app_name = '플리'

urlpatterns = [
    path('', views.show_index, name='show_index'),
    path('login/', views.show_login, name='show_login'),
    path('signup/', views.show_signup, name='show_signup'),
    path('url/', views.show_url, name='show_url'),
    path('mypage/', views.show_mypage, name='show_mypage'),
]