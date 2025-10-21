from django.shortcuts import render

def home_view(request):
    """الصفحة الرئيسية للموقع"""
    return render(request, 'home.html')
