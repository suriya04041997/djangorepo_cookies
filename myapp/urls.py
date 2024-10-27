# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('delete-cookie/', views.delete_cookie, name='delete_cookie'),
]
