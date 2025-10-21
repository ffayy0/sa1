from django.shortcuts import render
from store.models import Product

def home_view(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'products': products})
