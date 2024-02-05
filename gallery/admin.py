from django.contrib import admin
from .models import SalonImage, HairstyleImage


@admin.register(SalonImage)
class SalonImageAdmin(admin.ModelAdmin):

    """
    This class defines the administration interface for the SalonImage model,
    allowing administrators to manage salon images.
    """

    pass

@admin.register(HairstyleImage)
class HairstyleImageAdmin(admin.ModelAdmin):

    """
    This class defines the administration interface for the HairstyleImage model,
    allowing administrators to manage hairstyle images.
    """

    pass