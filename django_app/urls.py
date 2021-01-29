from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post_create/', post_create, name='post_create'),
]
