from django.shortcuts import render


"""
Renders the information page.
"""
def information_page(request):
    return render(request, 'information/information_page.html')