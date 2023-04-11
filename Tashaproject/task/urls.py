from django.urls import path
from . import views


urlpatterns = [
    path('', views.Tasks, name='tests' ),
    path('add/', views.add , name= 'add')
]