from rest_framework import serializers

from account.models import CustomerUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = (
            'username',
            'full_name',
            'email',
            'password',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number'
        )