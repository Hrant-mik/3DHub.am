from django.shortcuts import render

def home_view(request):
    return render(request, 'main/home.html')

def printing_view(request):
    return render(request, 'main/printing.html')

def modeling_view(request):
    return render(request, 'main/modeling.html')

def scanning_view(request):
    return render(request, 'main/scanning.html')

def contact_view(request):
    return render(request, 'main/contact.html')

def sign_in_view(request):
    return render(request, 'main/sign_in.html')