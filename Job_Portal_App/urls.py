from django.urls import path
from .views import *

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('change_password/',change_password,name='change_password'),
]