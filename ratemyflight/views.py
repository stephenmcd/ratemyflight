
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from ratemyflight.forms import RatingForm
from ratemyflight.models import Airport, Rating
from ratemyflight.settings import MAX_AIRPORTS, MAX_FLIGHTS


def rating(request, template="rating.html"):
    """
    Rating form.
    """
    form = RatingForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse("rating"))
    context = {"form": form}
    return render_to_response(template, context, RequestContext(request))


def airports_for_boundary(request, south, west, north, east):
    """
    Return a JSON formatted list of airports in the given boundary.
    """
    try:
        airports = Airport.objects.for_boundary(south, west, north, east)
    except ValueError:
        return HttpResponse("[]", mimetype="application/json")
    json = serializers.serialize("json", airports[:MAX_AIRPORTS])
    return HttpResponse(json, mimetype="application/json")

def flights_for_boundary(request, south, west, north, east):
    """
    Returns the flights within the bounding box supplied.
    """
    try:
        airports = Airport.objects.for_boundary(south, west, north, east)
    except ValueError:
        return HttpResponse("[]", mimetype="application/json")
    flights = Rating.objects.filter(Q(airport_from__in=airports) | 
        Q(airport_to__in=airports))
    json = serializers.serialize("json", flights[:MAX_FLIGHTS])
    return HttpResponse(json, mimetype="application/json")
    
def flights_for_airline(request, iata_code):
    """
    Returns a list of flights for a given carrier.
    
    Arguments:
    carrier_code: 2 letter IATA carrier code
    """
    
    json = serializers.serialize("json", {})
    
    if request:
        return HttpResponse(json, mimetype="application/json")
    else:
        return json

def flights_for_username(request, username):
    """
    Returns a list of flights for a given username.
    
    Arguments:
    username: the username that you are looking for.
    """
    
    json = serializers.serialize("json", {})
    if request:
        return HttpResponse(json, mimetype="application/json")
    else:
        return json

def recent_flights(request, num):
    """
    Returns num list of flights, sorted by recency. No bounding area.
    
    Arguments:
    num: the number you want to return
    """
    
    json = serializers.serialize("json", {})
    if request:
        return HttpResponse(json, mimetype="application/json")
    else:
        return json

