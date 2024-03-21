from django.urls import path
from .views import TaskRegisterView

urlpatterns = [
    path("register/", TaskRegisterView.as_view(), name="task-view"),
]
