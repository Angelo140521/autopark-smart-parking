from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='parking/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('payment/', views.payment_page, name='payment'),
    path('history/', views.history_page, name='history'),
    
    path('adminlogin/', views.admin_login_page, name='admin_login'),
    path('adminreport/', views.admin_report_page, name='admin_report'),
]
