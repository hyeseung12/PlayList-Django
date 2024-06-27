from django.urls import path

from 플리 import views
from 플리.views import EmailLoginView, SignUpView, PlayListCreateView, PlayListView, PlayListDeleteView, \
    PlayListUpdateView, PlayListDetailView

app_name = '플리'

urlpatterns = [
    path('', views.show_index, name='show_index'),
    path('login/', EmailLoginView.as_view(), name='show_login'),
    path('signup/', SignUpView.as_view(), name='show_signup'),
    path('url/', views.show_url, name='show_url'),
    path('mypage/', PlayListView.as_view(), name='show_mypage'),
    path('create/', PlayListCreateView.as_view(), name='show_create'),
    path('delete/<int:pk>/', PlayListDeleteView.as_view(), name='show_delete'),
    path('update/<int:pk>/', PlayListUpdateView.as_view(), name='show_update'),
    path('detail/<int:pk>/', PlayListDetailView.as_view(), name='show_detail'),
]