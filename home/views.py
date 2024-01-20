from django.shortcuts import render


def my_salon(request):
    return render(request, 'home/home_page.html')

