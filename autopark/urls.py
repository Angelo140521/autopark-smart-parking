from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from parking import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # 👈 redirect root to login
    path('accounts/', include('django.contrib.auth.urls')),  # built-in login/logout
    path('', include('parking.urls')),  # your app routes
    path('admin-report/', views.admin_report, name='admin_report')
]
