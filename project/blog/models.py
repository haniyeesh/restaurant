from django.db import models
from django.conf import settings

from django.db import models


class Article_category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Article_category, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='img', blank=True , null=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like', blank=True)

    def like_count(self):
        return self.like.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default='....@gmail.com')
    parent = models.ForeignKey('self', null=True , blank=True , related_name='replies', on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name