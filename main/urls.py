from django.urls import path
from . import views

urlpatterns = [
    path('<str:name_filter>/', views.index_filter),
    path('', views.index, name='index')
]
