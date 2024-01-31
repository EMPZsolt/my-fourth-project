from django.db import models
from cloudinary.models import CloudinaryField

class SalonImage(models.Model):
    salon_image = CloudinaryField('image', default='placeholder')

class HairstyleImage(models.Model):
    hairstyle_image = CloudinaryField('image', default='placeholder')