from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from account.serializers import UserSerializer
from django.contrib.auth.models import Group
from .models import CustomUser


class LoginUser(APIView):
    def post(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        try:
            db = CustomUser.objects.get(username=username)
            print("User exists")
        except CustomUser.DoesNotExist:
            print("User does not exist")
            return Response(
                {"message": "User does not exist"}, status=HTTP_404_NOT_FOUND
            )

        if db:
            if db.check_password(password):
                response = Response({"message": "User Logged In"})
                response.set_cookie("uid", db.pk, secure=False, httponly=True)
                return response
            else:
                return Response(
                    {"message": "Invalid password"}, status=HTTP_401_UNAUTHORIZED
                )
        else:
            return Response(
                {"message": "User does not exist"}, status=HTTP_404_NOT_FOUND
            )


class RegisterUser(APIView):
    def get(self, request):
        db = CustomUser.objects.all()
        return Response(UserSerializer(db, many=True).data)

    def post(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        email = request.data.get("email", None)
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("last_name", None)
        department = request.data.get("department", None)
        type = request.data.get("type", "Staff")
        employee_id = request.data.get("employee_id", None)
        police_station = request.data.get("police_station", None)
        rank = request.data.get("rank", None)
        date_of_joining = request.data.get("date_of_joining", None)
        contact = request.data.get("contact", None)
        profile_created_by = request.data.get("profile_created_by", None)

        db, created = CustomUser.objects.get_or_create(username=username)
        print(db)
        if created:

            db.password = make_password(password)
            db.email = email
            db.first_name = first_name
            db.last_name = last_name
            if type == "SP":
                groupDB, group_created = Group.objects.get_or_create(name="SP")
                groupDB.user_set.add(db)

            if type == "PI":
                groupDB, group_created = Group.objects.get_or_create(name="PI")
                groupDB.user_set.add(db)

            if type == "PSI":
                groupDB, group_created = Group.objects.get_or_create(name="PSI")
                groupDB.user_set.add(db)

            if type == "Staff":
                groupDB, group_created = Group.objects.get_or_create(name="Staff")
                groupDB.user_set.add(db)

            db.save()

            return Response({"message": "User Created"}, status=HTTP_201_CREATED)
        else:
            return Response({"message": "User Exists"}, status=HTTP_400_BAD_REQUEST)
