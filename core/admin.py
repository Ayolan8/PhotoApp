from django.contrib import admin
from .models import Photos
#from PIL import Image as Im
#from django.utils.safestring import mark_safe

class PhotosAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "photo",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Photos, PhotosAdmin)

#def image_tag(self):
    #return mark_safe('<img src="/../../media/%s width="150" height="150"/>' %(self.photo))

#def save(self):
#super().save()

