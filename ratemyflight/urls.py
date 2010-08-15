
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("ratemyflight.views",
    url("^api/airport/boundary/(?P<south>.*)/(?P<west>.*)/(?P<north>.*)/(?P<east>.*)/$", 
        "airports_for_boundary", name="airports_for_boundary"),
    url("^api/flight/boundary/(?P<south>.*)/(?P<west>.*)/(?P<north>.*)/(?P<east>.*)/$", 
        "flights_for_boundary", name="flights_for_boundary"),
    url("^api/flight/airline/(?P<iata_code>.*)/$", 
        "flights_for_airline", name="flights_for_airline"),
    url("^api/flight/username/(?P<username>.*)/$", 
        "flights_for_username", name="flights_for_username"),
    url("^api/flight/recent/$", "recent_flights", name="recent_flights"),
    url("^$", "home", name="home"),
)


