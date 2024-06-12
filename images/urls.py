from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index_view, name='images-index'),
    path('upload/', views.upload_view, name='images-upload'),
    path('test/', views.testing, name='test'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', views.blog_detail_view, name='blog_detail'),
]