from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):

    """
    This model stores information about the salon, including the owner's name, salon name, profile picture,
    salon logo, and additional content or description. It is used to populate the 'About' section of the salon's website.
    """

    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    owner_name = models.CharField(max_length=100, default='Marisa Speidel')
    salon_image = CloudinaryField('image', default='placeholder')
    salon_name = models.CharField(max_length=200, default='Hair by Budu')
    content = models.TextField()

    def __str__(self):
        return self.title