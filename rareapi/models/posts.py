from django.db import models
from .user import User
from .category import Category

class Post(models.Model):
    rare_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    publication_date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=150)
    image_url = models.CharField(max_length=150)
    approved = models.BooleanField(default=True)
