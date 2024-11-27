from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import CustomUser
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Keiziban_post(models.Model):
    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.CASCADE)
    title=models.CharField(verbose_name='タイトル',max_length=100)
    comment=models.TextField(verbose_name='コメント',)
    posted_at=models.DateTimeField(verbose_name='投稿日時',auto_now_add=True)
    def __str__(self):
        return self.title

class ViewCount(models.Model):
    count=models.IntegerField(default=0)
    last_viewed = models.DateTimeField(default=timezone.now)
    