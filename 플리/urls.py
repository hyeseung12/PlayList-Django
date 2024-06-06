from django.urls import path

from 플리 import views

app_name = 'img'

urlpatterns = [
    path('', views.show_index, name='show_index')
]