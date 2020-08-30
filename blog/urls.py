from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.blog, name='blog'),
    path('<str:slug>', views.blogPost, name='blogPost'),

]
