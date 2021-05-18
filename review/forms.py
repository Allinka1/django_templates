from django import forms
from products.models import Products
from django.core.exceptions import ValidationError


class ReviewForm(forms.Form):
    review = forms.CharField(label='Product Review', widget=forms.Textarea, required=False)
    rating = forms.IntegerField(label='Product Rate')
    # product = forms.ModelChoiceField(queryset=Products.objects.all

    def clean_review(self):
        review = self.cleaned_data.get('review')
        if not review:
            raise ValidationError('review text required')
        return review

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise ValidationError('rating should be in range 1..5')
        return rating

    def clean(self):
        super().clean()
