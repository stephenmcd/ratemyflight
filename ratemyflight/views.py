from django.core import serializers
from django.http import HttpResponse

from core.models import Airport
from core.settings import MAX_AIRPORTS


def airports_for_boundary(request, south, west, north, east):
    """
    Return a JSON formatted list of airports in the given boundary.
    """
    try:
        lookup = {
            "latitude__gt": float(south), "longitude__gt": float(west),
            "latitude__lt": float(north), "longitude__lt": float(east),
        }
    except ValueError:
        lookup = {}
    airports = Airport.objects.filter(**lookup)[:MAX_AIRPORTS]
    json = serializers.serialize("json", airports)
    return HttpResponse(json, mimetype="application/json")
