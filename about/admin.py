from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    """
    Admin configuration for the About model.
    """

    list_display = ('title', 'owner_name')
    summernote_fields = ('content',)