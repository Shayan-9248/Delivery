from django.db import models
from django.utils.text import slugify
from django.utils.html import format_html
from accounts.models import (
    User
)


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.created.strftime('%Y-%m-%d')}"
    

class Category(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(default='1.jpg')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    def image_thumbnail(self):
        return format_html('<img src="{}" width=90>'.format(self.image.url))
    image_thumbnail.short_description = 'Image'


class OrderModel(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(MenuItem, blank=True, related_name='items')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"