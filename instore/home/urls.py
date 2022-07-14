
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('recognize', views.recognize, name='recognize_me'),
    path('recognize/insert', views.Insertrecord, name='Insertrecord'),
    path('loan', views.Viewloan, name="Viewloan"),
    path('search', views.search, name="search"),
    path('loan/calculate', views.calculate, name="calculate"),
    path('loan/calculate/interest', views.interest_calculation, name="interest_calculation")
]
