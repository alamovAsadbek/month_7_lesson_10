from django.urls import path

from app_tweets import views as tweet_views
from users import views as user_views

urlpatterns = [
    path('auth/register/', user_views.RegisterView.as_view(), name='register'),
    path('auth/login/', user_views.LoginView.as_view(), name='login'),
    path('auth/logout/', user_views.LogoutView.as_view(), name='logout'),
    path('verify-email/<uidb64>/<token>/', user_views.VerifyEmailView.as_view(), name='verify-email'),
    path('verify-resend/', user_views.ResendEmailVerificationView.as_view(), name='verify-resend'),
    path('tweets/', tweet_views.TweetView.as_view(), name='tweets'),
]
