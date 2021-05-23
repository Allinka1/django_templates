from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from products.models import Products
from review.models import Review

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def product_detail(request, product_slug):

    product = Products.objects.get(pid=product_slug)
    reviews = Review.objects.filter(product_id=product.pid)

    context = {
        'title': 'Product Detail',
        'product': product,
        'reviews': reviews
    }

    return render(request, "product_detail.html", context)

    # return HttpResponse(f"This a product detail page: {product_slug}")


def products_list(request):

    products = Products.objects.all()


    context = {
        'title': 'Products List',
        'products': products
    }

    return render(request, 'products.html', context)