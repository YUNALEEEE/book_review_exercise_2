from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    CHOICES = (
        ('1','1점'),
        ('2','2점'),
        ('3','3점'),
        ('4','4점'),
        ('5','5점'),
    )
    title = models.CharField(max_length= 50)
    contents = models.TextField()
    img = models.FileField(null=True)
    price = models.FloatField()
    rating = models.CharField(max_length = 50, choices=CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50, default = "")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'comments')
    content = models.TextField()
    author = models.CharField(max_length=30, default='')




