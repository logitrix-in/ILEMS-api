from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
