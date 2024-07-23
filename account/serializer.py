from rest_framework import serializers
from django.contrib.auth.models import User

class SignUpSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

        extra_kwargs = {
            'password': {'required': True, 'allow_blank': True, 'min_length' : 8 },
            'first_name': {'required': True, 'allow_blank': True },
            'last_name': {'required': True, 'allow_blank': True },
            'email': {'required': True, 'allow_blank': True }
        }

class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
