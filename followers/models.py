from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name="followee", null=True, on_delete=models.CASCADE)
    followee = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name="follower")     # user that is being followed

    def __str__(self):
        return f"{self.follower.username} follows {self.followee.username}"

class FollowRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username} {self.status}"