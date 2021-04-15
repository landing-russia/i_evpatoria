from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/', include('tailwind.urls', namespace='tailwind')),
]
