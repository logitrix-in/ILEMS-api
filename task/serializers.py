from rest_framework.serializers import ModelSerializer

from .models import Task
from account.models import CustomUser


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        depth = 2


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "employee_id",
            "id",
            "first_name",
        ]
