from django.shortcuts import render


def my_salon(request):

    """
    Renders the home page of the salon.
    """
    
    return render(request, 'home/home_page.html')