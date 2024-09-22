from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Staff(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='staff_photos/')
    bio = models.TextField()

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name