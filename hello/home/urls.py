from django.urls import path,include
from home import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services')
]

