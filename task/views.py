from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from .models import Task, CustomUser
from .serializers import TaskSerializer


# Create your views here.
class TaskRegisterView(APIView):
    def get(self, request):
        db = Task.objects.all()
        return Response(TaskSerializer(db, many=True).data)

    def post(self, request):
        pk = request.COOKIES.get("uid", None)
        if pk:
            user = CustomUser.objects.get(pk=pk)
            title = request.data.get("title", None)
            deadline = request.data.get("deadline", None)
            description = request.data.get("description", None)
            status = request.data.get("status", "Pending")
            assigned_to_id = request.data.get("assigned_to", None)

            if assigned_to_id:
                try:
                    assigned_user = CustomUser.objects.get(employee_id=assigned_to_id)
                except CustomUser.DoesNotExist:
                    return Response(
                        {"message": "Assigned user does not exist"},
                        status=HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"message": "Assigned user ID is required"},
                    status=HTTP_400_BAD_REQUEST,
                )

            db = Task.objects.create(
                user=user,
                title=title,
                deadline=deadline,
                description=description,
                assigned_to=assigned_user,
                status=status,
            )
            return Response(
                {"message": "Task Created Successfully"},
                status=HTTP_200_OK,
            )

        else:
            return Response(
                {"message": "User not logged in"}, status=HTTP_404_NOT_FOUND
            )
