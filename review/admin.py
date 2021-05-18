from django.contrib import admin
from review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    fields = ['product', 'body', 'rating']
    ordering = ['rid']
    list_display = ['product', 'body', 'rating', 'created_at']


admin.site.register(Review, ReviewAdmin)
