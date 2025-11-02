from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    """
    Return all properties as JSON.
    Cached in Redis for 15 minutes.
    """
    properties = Property.objects.all()
    data = [
        {
            'title': prop.title,
            'price': prop.price,
            'location': prop.location,
            'description': prop.description
        }
        for prop in properties
    ]
    return JsonResponse({'data': data})

