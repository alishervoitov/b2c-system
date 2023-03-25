from django.urls import path
from account.views import RegistrationAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
]