from django.db import models
import uuid

class Lead(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    primary_goal = models.CharField(max_length=50)
    sub_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - Goal: {self.primary_goal}"