from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', include('excursions.urls', namespace='excursions')),
    path('contacts', contacts, name='contacts'),
    path('t/', include('tailwind.urls', namespace='tailwind')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT, )


admin.site.index_title = 'Админка'
admin.site.site_header = 'Я-Евпатория!'
admin.site.site_title = 'Я-Евпатория!'