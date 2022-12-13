from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_pic = models.ImageField(default='images/default-user.png', null=True, blank=True)
    # bio = models.CharField(max_length=200, null=True, blank=True)
    # followers = models.ManyToManyField()
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'name', 'date_of_birth']

    def get_total_followers(self):
        no_of_followers = self.follower.all().count()
        return no_of_followers
    
    def get_total_followings(self):
        no_of_followings = self.followee.all().count()
        return no_of_followings
    
    def is_followed(self, user_id):
        self_following = self.followee.all()
        user = User.objects.get(id=user_id)
       
        for following in self_following:  
            if user == following.followee:
                return True
        return False
