from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from taggit.managers import TaggableManager
from django.urls import reverse


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=20)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField()
    color = models.CharField(max_length=60)
    size = models.CharField(max_length=60)
    recommendations = models.TextField()
    categories = TaggableManager()
    likes = GenericRelation(Like)
    SKU = models.CharField(max_length=60)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title + " color: " + self.color

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'product_id': self.pk})

    @property
    def total_likes(self):
        return self.likes.count()



class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    gallery = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')

    def __str__(self):
        return self.image.url

