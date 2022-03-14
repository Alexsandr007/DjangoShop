from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Category(models.Model):
    name = models.CharField(max_length=60)

class Size(models.Model):
    name = models.CharField(max_length=20)
    value = models.IntegerField()

class Product(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField()
    color = models.CharField(max_length=60)
    size = models.ManyToManyField(Size, related_name="size")
    recommendations = models.TextField()
    categories = models.ManyToManyField(Category, related_name="category")
    likes = GenericRelation(Like)

    @property
    def total_likes(self):
        return self.likes.count()

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
