
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('messaging/', include(('rest_messaging.urls', 'rest_messaging'), namespace='rest_messaging')),
]
