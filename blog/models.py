from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True, null=True)
    category = models.CharField(max_length=255, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.body, self.date_added)
