from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Product
from django.shortcuts import render


def index_view(request: WSGIRequest):
    products = Product.objects.exclude(is_deleted=True).order_by('title', 'category')
    context = {
        'products': products
    }
    return render(request, 'index.html', context=context)
