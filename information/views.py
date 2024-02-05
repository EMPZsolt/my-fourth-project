from django.shortcuts import render


def information_page(request):

    """
    Renders the information page.
    """
    
    return render(request, 'information/information_page.html')