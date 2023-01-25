from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.header, name='header'),
    path('user_info/', views.user_info, name='user_info'),
]