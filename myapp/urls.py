from django.urls import path
from .views import *


urlpatterns = [
    path('', get_data),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('signup_function', signup_function)
]
