from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Messages(models.Model):
    message_body = models.TextField(max_length=500, null=False, blank=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    thread_name = models.CharField(max_length=50, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}"