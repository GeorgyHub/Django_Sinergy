from django.urls import path, include
from News.views import *

urlpatterns = [
    path('', index),
    path('test/', test),
]