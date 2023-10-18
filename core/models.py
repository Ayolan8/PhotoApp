from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Photos(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=False, blank=False, upload_to="images_folder")
    slug = models.SlugField(default="", unique=True)

    class Meta:
        verbose_name_plural = 'photos'
        ordering = ['-created_at',]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



     
