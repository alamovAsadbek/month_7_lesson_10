from django.urls import path

from users import views as user_views

urlpatterns = [
    path('auth/register/', user_views.RegisterView.as_view(), name='register'),
    path('auth/login/', user_views.LoginView.as_view(), name='login'),
    path('auth/logout/', user_views.LogoutView.as_view(), name='logout'),
    path('verify-email/<uidb64>/<token>/', user_views.VerifyEmailView.as_view(), name='verify-email')
]
