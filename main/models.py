from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return self.title

class Talks(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    date = models.DateField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return self.title

