from django.urls import path
from account.views import RegistrationAPIView, UserLoginView, UserProfileView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
]