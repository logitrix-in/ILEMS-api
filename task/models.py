from django.db import models
from account.models import CustomUser

# Create your models here.
STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Completed", "Completed"),
)


class Task(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="tasks_assigned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    assigned_to = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="tasks_to_complete"
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
