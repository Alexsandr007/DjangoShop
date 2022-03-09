from django.db import models

from taggit.managers import TaggableManager

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField()
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    tags = TaggableManager()