
from django.utils import simplejson

from ratemyflight.models import Airport
from ratemyflight.settings import MAX_FLIGHTS


def flights_as_json(flights_qs, limit):
    """
    Given a queryset of flights, return it as JSON with the from/to airports 
    grafted onto it since Django's serializer can't follow relationships.
    We also need to call values() on both the airports and flights since 
    simplejson doesn't understand models.
    """
    flights = list(flights_qs.values()[:limit])
    airport_ids = []
    for flight in flights:
        airport_ids.extend([flight["airport_from_id"], flight["airport_to_id"]])
    airports = Airport.objects.filter(pk__in=airport_ids).values()
    airports = dict([(a["id"], a) for a in airports])
    for (i, flight) in enumerate(flights):
        flights[i]["airport_from"] = airports[flight["airport_from_id"]]
        flights[i]["airport_to"] = airports[flight["airport_to_id"]]
        del flights[i]["time"] # Not serializeable.
    return simplejson.dumps(flights)

