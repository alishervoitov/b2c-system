from django.urls import path
from account.views import RegistrationAPIView, UserLoginView, UserProfileView, ChangePasswordView, EditProfileView, SendPasswordEmailView, UserPasswordResetView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile'),
    path('send-email/', SendPasswordEmailView.as_view()),
    path('reset-password/', UserPasswordResetView.as_view()),
]