from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from account.permissions import HasPermission
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
                response.set_cookie(
                    "uid", db.pk, secure=True, httponly=True, samesite="None"
                )
                return response
            else:
                return Response(
                    {"message": "Invalid password"}, status=HTTP_401_UNAUTHORIZED
                )
        else:
            return Response(
                {"message": "User does not exist"}, status=HTTP_404_NOT_FOUND
            )

    def get(self, request):
        pk = request.COOKIES.get("uid", None)
        if pk:
            db = CustomUser.objects.get(pk=pk)
            return Response(UserSerializer(db).data)
        else:
            return Response(
                {"message": "User not logged in"}, status=HTTP_404_NOT_FOUND
            )

    def delete(self, request):
        response = Response({"message": "User Logged Out"})
        response.delete_cookie(
            "uid", expires=0, max_age=0, secure=True, samesite="none"
        )
        return response


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
            db.employee_id = employee_id
            db.department = department
            db.rank = rank
            db.police_station = police_station
            db.contact = contact
            db.profile_created_by = profile_created_by

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


class GetUpdateUsersAPI(APIView):
    def get(self, request):
        db = CustomUser.objects.all()
        return Response(UserSerializer(db, many=True).data)

    def post(self, request):
        pk = request.COOKIES.get("uid", None)
        if pk:
            user = CustomUser.objects.get(pk=pk)
            # if user.groups.filter(name="SP").exists():

            employee_id = request.data.get("employee_id", user.employee_id)
            username = request.data.get("username", user.username)
            email = request.data.get("email", user.email)
            first_name = request.data.get("first_name", user.first_name)
            last_name = request.data.get("last_name", user.last_name)
            department = request.data.get("department", user.department)

            user.employee_id = employee_id
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.department = department
            user.save()

            return Response(UserSerializer(user).data)
            # else:
            #     return Response(
            #         {"message": "User does not have permission"},
            #         status=HTTP_401_UNAUTHORIZED,
            #     )
        else:
            return Response(
                {"message": "User not logged in"}, status=HTTP_404_NOT_FOUND
            )
