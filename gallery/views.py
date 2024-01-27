from django.shortcuts import render
from .models import HairSalonImage, HairstyleImage

def gallery_page(request):
    hair_salon_images = HairSalonImage.objects.all()
    hairstyle_images = HairstyleImage.objects.all()
    return render(request, 'gallery/gallery_page.html', {'hair_salon_images': hair_salon_images, 'hairstyle_images': hairstyle_images})
