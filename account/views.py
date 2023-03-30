from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from account.models import CustomerUser
from account.serializers import RegistrationSerializer, UserLoginSerializer, UserProfileSerializer, \
    ChangePasswordSerializer, EditProfileSerializer

from account.renderer import UserRenderer


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
    # renderer_classes = [UserRenderer]

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

class UserProfileView(generics.GenericAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    # renderer_classes = [UserRenderer]

    def get(self, request, format=None):

        serializer = UserProfileSerializer(request.user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class ChangePasswordView(generics.UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    # renderer_classes = [UserRenderer]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        data = request.data
        new_password = data['new_password']

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('password')):
                return Response({"password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(new_password)
            self.object.save()
            return Response({
                'Message': request.data,
                'Msg': 'Password changed succesfully'
            },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class EditProfileView(generics.GenericAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = EditProfileSerializer
    queryset = CustomerUser.objects.all()
    # renderer_classes = [UserRenderer]

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method put not allowed'})
        try:
            instance = CustomerUser.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})
        serializer = EditProfileSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'Message': request.data,
                'Msg': 'Your profile updated succesfully'
            },
            status=status.HTTP_400_BAD_REQUEST
        )