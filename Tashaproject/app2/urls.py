
from django.urls import path
from . import views

urlpatterns = [
    path('', views.app2, name='app2' )
]