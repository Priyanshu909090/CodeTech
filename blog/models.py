from django.db import models


# Create your models here.

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=500, default="")
    heading = models.CharField(max_length=5000, default="")
    content = models.CharField(max_length=50000, default="")
    category = models.CharField(max_length=20, default="")
    subcategory = models.CharField(max_length=20, default="")
    views = models.IntegerField(default=0)
    timeStemp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=100, default="")
    summary = models.CharField(max_length=50000, default="")
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return f'{self.title} by {self.author}'


class Feature(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=500, default="")
    heading = models.CharField(max_length=5000, default="")
    content = models.CharField(max_length=50000, default="")
    category = models.CharField(max_length=20, default="")
    subcategory = models.CharField(max_length=20, default="")

    timeStemp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=100, default="")
    summary = models.CharField(max_length=50000, default="")
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return f'{self.title} by {self.author}'
