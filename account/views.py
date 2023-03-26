from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from account.models import CustomerUser
from account.serializers import RegistrationSerializer, UserLoginSerializer


class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):

        data = request.data
        username = data['username']
        full_name = data['full_name']
        email = data['email']
        password = data['password']
        password1 = data['password1']
        country = data['country']
        company_name = data['company_name']
        user_type = data['user_type']
        phone_number = data['phone_number']
        corporate_number = data['corporate_number']

        if CustomerUser.objects.filter(email=email).exists():
            return Response({'Error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if password != password1:
            return Response({'Error': 'Passwords arent match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = CustomerUser.objects.create_user(
                username=username,
                full_name=full_name,
                email=email,
                password=password,
                country=country,
                company_name=company_name,
                user_type=user_type,
                phone_number=phone_number,
                corporate_number=corporate_number
            )
            user.set_password(password)
            user.save()

            return Response({
                'Message': request.data,
            },
                status=status.HTTP_200_OK
            )

class UserLoginView(generics.GenericAPIView):

    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                return Response({
                    'Message': serializer.data},
                    status=status.HTTP_200_OK
                )