from django.urls import path
from . import views

appname = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>/', views.detail_list, name='detail'),
    path('myphotos/', views.my_photos, name='my_photos'),
]
