from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer, UserSerializer

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
