
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('recognize', views.recognize, name='recognize_me'),
    path('recognize/insert', views.Insertrecord, name='Insertrecord'),
    # path('loan', views.Viewrecord, name="Viewrecord")
]
