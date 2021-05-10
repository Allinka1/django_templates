from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def product_detail(request, product_slug):

    return render(request, "product_detail.html", {'product_slug': product_slug})

    # return HttpResponse(f"This a product detail page: {product_slug}")


def products_list(request):

    products = [
            {'title': 'Product №1', 'url': 'product-1'},
            {'title': 'Product №2', 'url': 'product-2'},
            {'title': 'Product №3', 'url': 'product-3'},
            {'title': 'Product №4', 'url': 'product-4'},
            {'title': 'Product №5', 'url': 'product-5'},
        ]


    context = {
        'title': 'Products List',
        'products': products,
        'list': [1, 2, 3, 4, 5]
    }

    return render(request, 'products.html', context)