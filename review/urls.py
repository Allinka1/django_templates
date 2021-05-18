from django.urls import path
from review.views import review, review_form_valid, review_form_invalid

urlpatterns = [
    path('review/', review, name='review'),
    path('form_valid/', review_form_valid),
    path('form_invalid/', review_form_invalid)
]
