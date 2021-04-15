from django.urls import path
from .views import *

app_name = 'tailwind'

urlpatterns = [
    path('', tailwind_home),
]
