from django.urls import path
from .views import RegisterUser, LoginUser, GetUpdateUsersAPI

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("get-update/", GetUpdateUsersAPI.as_view(), name="get-users"),
]
