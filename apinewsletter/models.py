from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL


class Subscribe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} subscribed successful"


class Interest(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class SubscribeInterest(models.Model):
    interest = models.ForeignKey(Interest,on_delete=models.CASCADE)
    subscribe = models.ForeignKey(Subscribe, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.subscribe.user.username} as interested for {self.interest.name}"



class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Interest)

