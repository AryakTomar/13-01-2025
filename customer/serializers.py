# from rest_framework import serializers
# from .models import Customer # Make sure to import your model

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer  # This is the missing piece
#         fields = '__all__' # Or a list of specific fields like ['id', 'name']

# THIS ABOVE CODE IS WORKING FINE

#------------------------------------------------------------------------------

from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # This hashes the password before it hits the DB
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

