from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('details/<id>/', views.details, name='details'),
    path('delete/<id>/', views.delete, name='delete'),
    path('edit/<id>/', views.edit, name='edit'),
]