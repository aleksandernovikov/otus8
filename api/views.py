from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Record
from .serializers import CustomTokenObtainPairSerializer, UserSerializer, RecordSerializer

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RecordViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
