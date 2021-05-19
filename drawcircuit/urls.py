from django.urls import path, include
from django.conf.urls import url

from drawcircuit import views

app_name = 'snippets'

urlpatterns = [
    path('test/', views.test, name='test'),
]
