from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
class SignupSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone', 'role']
        
    def create(self, validated_data):
        phone = validated_data.pop('phone')
        role = validated_data.pop('role')
        user = User.objects.create_user(**validated_data)
        userotherinfo = UserOtherInfo.objects.create(user=user, phone=phone, role=role)
        return user


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token ['username'] = user.username
        token ['email'] = user.email
        return token