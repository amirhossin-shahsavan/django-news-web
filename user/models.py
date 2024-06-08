from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    user_image = models.ImageField(upload_to='images/user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title