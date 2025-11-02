from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Retrieve all properties from cache if available, otherwise fetch from DB and cache for 1 hour.
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all())  # Convert to list to store in cache
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour (3600 seconds)
    return properties
