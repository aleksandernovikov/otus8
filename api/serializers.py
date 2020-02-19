from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        return super().create(validated_data)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name'
