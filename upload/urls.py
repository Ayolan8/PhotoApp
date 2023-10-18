from django.urls import path
from . import views

urlpatterns = [
    path('addform/', views.addform, name='addform'),
    path('<slug:slug>/editform', views.editform, name='editform'),
    path('<slug:slug>/pre_delete', views.delete_warning, name='pre_delete'),
    path('<slug:slug>/delete', views.delete_photo, name='delete'),
]