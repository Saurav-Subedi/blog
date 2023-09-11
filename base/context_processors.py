from .models import Category
from django.db.models import Count

def categories(request):
    categories = Category.objects.annotate(post_count=Count('posts'))
    return {'categories': categories}
