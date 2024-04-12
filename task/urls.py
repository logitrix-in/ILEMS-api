from django.urls import path
from .views import TaskRegisterView, TaskUpdateView

urlpatterns = [
    path("register/", TaskRegisterView.as_view(), name="task-view"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
]
