from rest_framework import serializers

from account.models import CustomerUser


class RegistrationSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(max_length=30)
    class Meta:
        model = CustomerUser
        fields = (
            'username',
            'full_name',
            'email',
            'password',
            'password1',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number'
        )

class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomerUser
        fields = [
            'email',
            'password'
        ]

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = [
            'full_name',
            'email',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number',
        ]

class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(max_length=30)
    class Meta:
        model = CustomerUser
        fields = ['password', 'new_password']