from django.shortcuts import render


"""
Renders the home page of the salon.
"""
def my_salon(request):
    return render(request, 'home/home_page.html')