from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField()
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    tags = TaggableManager()
    categories = models.ManyToManyField(Category, related_name="category")

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

