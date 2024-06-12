from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=128)
    file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.title}"


from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[
        ('world', 'World'),
        ('india', 'India'),
        ('technology', 'Technology'),
        ('design', 'Design'),
        ('culture', 'Culture'),
        ('buisness', 'Buisness'),
        ('polotics', 'Polotics'),
        ('opinion', 'Opinion'),
        ('health', 'Health'),
        ('style', 'Ttyle'),
        ('travel', 'Travel'),
        # Add more categories as needed
    ], blank=True)
    priority = models.IntegerField(default=2)
    date_added = models.DateTimeField(default=timezone.now)
    keywords = models.CharField(max_length=255, blank=True)
    heading = models.CharField(max_length=255, blank=True)
    sub_heading = models.CharField(max_length=255, blank=True)
    sub_heading_2 = models.CharField(max_length=255, blank=True)
    context_1 = models.TextField(blank=True)
    context_2 = models.TextField(blank=True)
    context_3 = models.TextField(blank=True)
    context_4 = models.TextField(blank=True)
    context_5 = models.TextField(blank=True)
    image_1 = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")

    class Meta:
        ordering = ['priority', '-date_added']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_contexts(self):
        return [getattr(self, f'context_{i}') for i in range(1, 6)]

    def get_images(self):
        return [getattr(self, f'image_{i}') for i in range(1, 6) if getattr(self, f'image_{i}')]

