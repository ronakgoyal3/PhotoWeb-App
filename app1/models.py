from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
def upload_location(User, filename):
    return "%s/%s" %(User.id, filename)

class Album(models.Model):
    # artist=models.CharField(max_length=250)
    albumtitle = models.CharField(max_length=250)
    # Owner = models.CharField(max_length=250)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Album_logo = models.FileField(upload_to=upload_location, null=True,blank=True)
    def get_absolute_url(self):
        return reverse('app1:index')

    def __str__(self):
        return self.albumtitle
def upload_loc(User, filename):
    return "%s/%s" %(User.id, filename)
class Photo(models.Model):
    albumname = models.ForeignKey(Album, on_delete=models.CASCADE)
    Picture = models.FileField(upload_to=upload_loc,null=True, blank=True)
    # filetype = models.CharField(max_length=10)
    is_favourite = models.BooleanField(default= False)

    def get_absolute_url(self):
        return reverse('app1:index')

    def __str__(self):
        return self.Picture

