from django.contrib import admin
from django.urls import path,include
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Job_Portal_App.urls')),
    path('', include(notifications.urls, namespace='notifications')),
]
