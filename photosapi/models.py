from django.db import models


class PhotoModel(models.Model):
    title = models.CharField(max_length=255, default='the picture')
    photo = models.ImageField(upload_to='photos/')
    caption = models.TextField(default='This is picture')
    date_added = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
