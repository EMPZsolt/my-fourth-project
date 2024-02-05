from django.db import models
from cloudinary.models import CloudinaryField


class SalonImage(models.Model):

    """
    This model stores images related to the salon, such as the salon's exterior, interior, or logo.
    It is used to showcase visual content associated with the salon.
    """

    salon_image = CloudinaryField('image', default='placeholder')

class HairstyleImage(models.Model):

    """
    This model stores images related to hairstyles, such as different haircuts, colors, or styles.
    It is used to showcase various hairstyle options offered by the salon.
    """

    hairstyle_image = CloudinaryField('image', default='placeholder')