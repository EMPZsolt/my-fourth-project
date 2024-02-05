from django.shortcuts import render
from .models import About


def about_me(request):

    """
    View for rendering the About page.
    Retrieves the first About object from the database
    and renders the about.html template with the about object.
    """
    
    about = About.objects.all().first()
    return render(
        request,
        "about/about.html",
        {"about": about},
    )