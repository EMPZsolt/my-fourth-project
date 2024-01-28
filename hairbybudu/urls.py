from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("booking/", include("booking.urls"), name="booking-urls"),
    path("gallery/", include("gallery.urls"), name="gallery-urls"),
    path("information/", include("information.urls"), name="information-urls"),
    path("summernote/", include('django_summernote.urls')),
    path("", include("home.urls"), name="home-urls"),
]
