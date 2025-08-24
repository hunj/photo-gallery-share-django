from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('gallery:album_detail', kwargs={'pk': self.pk})
    
    def get_photo_count(self):
        return self.photos.count()


class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('gallery:photo_detail', kwargs={'pk': self.pk})
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None
