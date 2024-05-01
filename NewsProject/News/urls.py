from django.urls import path, include
from News.views import index

urlpatterns = [
    path('', index),
]
