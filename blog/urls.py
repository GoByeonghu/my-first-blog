from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('k/', views.post_list, name='post_list'),
]