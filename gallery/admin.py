from django.contrib import admin
from .models import SalonImage, HairstyleImage

@admin.register(SalonImage)
class SalonImageAdmin(admin.ModelAdmin):
    pass

@admin.register(HairstyleImage)
class HairstyleImageAdmin(admin.ModelAdmin):
    pass