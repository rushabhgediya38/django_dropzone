from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('post_create/', post_create, name='post_create'),
    path('create/', create, name='create'),
    path('final_post/', final_post, name='final_post'),
    path('test_post/', test_post, name='test_post'),
]
