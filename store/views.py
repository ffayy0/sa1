from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list_view(request):
    """
    عرض جميع المنتجات في صفحة المنتجات.
    """
    products = Product.objects.all().order_by('-created_at')
    context = {
        'products': products,
    }
    return render(request, 'store_templates/products.html', context)


def product_detail_view(request, product_id):
    """
    عرض تفاصيل منتج محدد.
    """
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store_templates/product_detail.html', {'product': product})
