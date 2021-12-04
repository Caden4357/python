from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    
    path('clubs', views.clubs),
    path('clubs/new', views.new),
    path('clubs/create', views.create),
    path('clubs/edit/<int:id>', views.edit),
    path('clubs/<int:id>/update', views.update),
    path('clubs/<int:id>', views.show),
    path('clubs/<int:c_id>/join', views.join),
    path('clubs/<int:id>/delete', views.delete),
    path('clubs/<int:c_id>/cancel', views.cancel),

]
