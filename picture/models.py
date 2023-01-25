from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    picture = models.ImageField(upload_to='media/picture', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description
    #
    # def get_absolute_url(self):
    #     return reverse('picture_detail', args=[str(self.id)])
    #


class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='media/video', null=True,
                            blank=True, validators=[
            FileExtensionValidator(allowed_extensions=[
                'MOV', 'avi', 'mp4', 'webm', 'mkv'
            ])
        ])
    description = models.TextField()

    def __str__(self):
        return self.description
