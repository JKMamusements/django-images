from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index_view, name='images-index'),
    path('upload/', views.upload_view, name='images-upload'),
    path('test/', views.testing, name='test'),
    path('', views.home, name='home'),
    
]