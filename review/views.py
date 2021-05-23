from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from review.models import Review
from review.forms import ReviewForm, SearchForm
from products.models import Products

def review(request):
    # return HttpResponse(f'Review {review_id} for {products_slug}')

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            return render(request, 'form_valid.html')
        else:
            return render(request, 'form.html', {'form':review_form})

    if request.method == 'GET':
        context = {
            'form': ReviewForm()
        }
        return render(request, 'form.html', context)


def review_form_valid(request):
    return render(request, 'form_valid.html')


def review_form_invalid(request):
    return render(request, 'form_invalid.html')


def search(request):
    if request.method == 'GET':
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            word = search_form.cleaned_data.get('find')
            is_my = search_form.cleaned_data.get('is_my')
            reviews = Review.objects.filter(body__icontains=word)

            if is_my == "True":
                reviews = reviews.filter(aurhor_id=request.user.id)

            context = {
                'search_form': search_form,
                'reviews': reviews
            }

            return render(request, 'get_comment.html', context)
