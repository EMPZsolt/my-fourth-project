from django.shortcuts import render

def information_page(request):
    return render(request, 'information/information_page.html')