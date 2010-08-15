from django.core import serializers
from django.http import HttpResponse

from ratemyflight.models import Airport
from ratemyflight.settings import MAX_AIRPORTS


def airports_for_boundary(request, south, west, north, east):
    """
    Return a JSON formatted list of airports in the given boundary.
    """
    
    lookup = {}
    lookup_alt = {}
    
    #do a really quick check to determine if we are crossing the PM or IDL
    if float(west) * float(east) < 0:
        # we need to do two lookups but we need to determine which side of
        # which meridian you actually are.
        
        #TODO: convert this back to a Q object
        
        # this check looks to see if we are closer to the IDL or the PM.
        # that then determines how we do the split on the two lookups
        if (180 - float(west)) < float(west) :
            #we're closest to IDL
            try:
                lookup = {
                    "latitude__gt": float(south), "longitude__gt": float(west),
                    "latitude__lt": float(north), "longitude__lt": 180,
                }
                lookup_alt = {
                    "latitude__gt": float(south), "longitude__gt": -180,
                    "latitude__lt": float(north), "longitude__lt": float(east),
                }   
                
            except ValueError:
                lookup = {}
                lookup_alt={}
        else:
        
            # closest to PM
            try:
                lookup = {
                    "latitude__gt": float(south), "longitude__gt": float(west),
                    "latitude__lt": float(north), "longitude__lt": 0,
                }
                lookup_alt = {
                    "latitude__gt": float(south), "longitude__gt": 0,
                    "latitude__lt": float(north), "longitude__lt": float(east),
                }   
                
            except ValueError:
                lookup = {}
                lookup_alt={}
        
    else:
        #we only need to do one lookup in this instance
    
        try:
            lookup = {
                "latitude__gt": float(south), "longitude__gt": float(west),
                "latitude__lt": float(north), "longitude__lt": float(east),
            }
        except ValueError:
            lookup = {}
    
    airports = Airport.objects.filter(**lookup)
    airports_alt = Airport.objects.filter(**lookup_alt)
    
    json = serializers.serialize("json", (airports | airports_alt)[:MAX_AIRPORTS])

    if request:
        return HttpResponse(json, mimetype="application/json")
    else:
        #used to display the data at command line
        return json
    
def flights_for_boundary (request, south, west, north, east):
    """
    Returns the flights within the bounding box supplied.
    """
    
    json = serializers.serialize("json", {})
    
    if request:
        return HttpResponse(json, mimetype="application/json")
    else:
        return json
    
def flights_for_carrier (request, carrier_code):
    """
    Returns a list of flights for a given carrier
    
    Arguments:
    carrier_code: 2 letter IATA carrier code
    """
    
    json = serializers.serialize("json", {})
    
    if request:
        return HttpResponse(json, mimetype="application/json")
    else:
        return json

def flights_for_username (request, username):
    """
    Returns a list of flights for a given username
    
    Arguments:
    username: the username that you are looking for.
    """
    
    json = serializers.serialize("json", {})
    if request:
        return HttpResponse(json, mimetype="application/json")
    else:
        return json

def recent_flights (request, num):
    """
    Returns num list of flights, sorted by recency. No bounding area
    
    Arguments:
    num: the number you want to return
    """
    
    json = serializers.serialize("json", {})
    if request:
        return HttpResponse(json, mimetype="application/json")
    else:
        return json

