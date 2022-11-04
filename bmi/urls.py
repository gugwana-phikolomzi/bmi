
from django.contrib import admin
from django.urls import path
from .views import home, matric, imperial

urlpatterns = [
    path('', home, name='home'),
    path('matric/', matric, name='matric'),
    path('imperial/', imperial, name='imperial'),

]