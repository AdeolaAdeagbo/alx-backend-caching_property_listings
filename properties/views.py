from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties

@cache_page(60 * 15)  # Cache the entire response for 15 minutes
def property_list(request):
    """
    Return all properties as JSON.
    Property queryset is cached in Redis for 1 hour.
    """
    properties = get_all_properties()
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
