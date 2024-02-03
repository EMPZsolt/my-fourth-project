from django.shortcuts import render
from .models import About


"""
View for rendering the About page.
Retrieves the first About object from the database
and renders the about.html template with the about object.
"""
def about_me(request):
    about = About.objects.all().first()
    return render(
        request,
        "about/about.html",
        {"about": about},
    )