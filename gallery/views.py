from django.shortcuts import render
from .models import SalonImage, HairstyleImage


def gallery_page(request):

    """
    View for rendering the gallery page.
    Retrieves all SalonImage and HairstyleImage objects from the database
    and renders the gallery_page.html template with the retrieved images.
    """
    
    salon_images = SalonImage.objects.all()
    hairstyle_images = HairstyleImage.objects.all()
    return render(request, 'gallery/gallery_page.html', {'salon_images': salon_images, 'hairstyle_images': hairstyle_images})