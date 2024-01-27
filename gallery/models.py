from django.db import models

class HairSalonImage(models.Model):
    image = models.ImageField(upload_to='hair_salon_images/')

class HairstyleImage(models.Model):
    image = models.ImageField(upload_to='hairstyle_images/')