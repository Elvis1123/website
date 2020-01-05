from django.urls import path
from django.template import loader
from . import views

app_name = 'music'

urlpatterns = [
    #/accounts/register/
    path('register/',views.register, name = 'register'),
    path('login/',views.login, name='login'),
]