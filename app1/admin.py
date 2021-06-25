from django.contrib import admin

# Register your models here.
from .models import Album,Photo
admin.site.register(Album) #this command will help to show the Album model in the admin panel of django
admin.site.register(Photo)