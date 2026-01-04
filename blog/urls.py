from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('register/', views.register, name='register'),
     path('create/', views.create_post, name='create-post'),
     path('edit/<int:pk>/', views.edit_post, name='edit-post'),
path('delete/<int:pk>/', views.delete_post, name='delete-post'),

]
