from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}_{self.id}' 

    @property
    def get_total_likes(self):
        likes =  self.like.all().count()

        return likes
        
    
    def get_last_like(self):
        try:
            return self.like.all().last().user
        except:
            return ""

    def is_liked_by_current_user(self, user):
        likes = self.like.all()
        
        for like in likes:
            if like.user == user:
                return True
        return False

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.post.user.username}_{self.post.id}_{self.id}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')

    def __str__(self):
        return f'{self.user.username} liked post_{self.post.id}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user.username}_{self.post.id}_{self.id}"

class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='stories/', null=True, blank=True)
    views = models.ManyToManyField(User, related_name="viewed_by", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"{self.id}"

    @property
    def views_cnt(self):
        return self.views.all().count()
