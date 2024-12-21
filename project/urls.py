# project/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('profile/', include('dashboard_app.urls')),
    path('obtain_data/', include('obtained_data_app.urls', namespace='obtained_data_app')),  # Add namespace here
    re_path(r'^(?!obtain_data).*$', lambda request: redirect('auth_app:login'))
]
