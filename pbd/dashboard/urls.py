from django.urls import path
from . import views


urlpatterns = [
    path('', views.index1, name='index1'),
    path('data2', views.index2, name='index2'),
    path('data3', views.index3, name='index3'),
]
