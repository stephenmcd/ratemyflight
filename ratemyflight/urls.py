
from django.conf.urls.defaults import *


urlpatterns = patterns("ratemyflight.views",
    url("^airport/list/(?P<south>.*)/(?P<west>.*)/(?P<north>.*)/(?P<east>.*)/", 
        "airports_for_boundary", name="airports_for_boundary"),
    url("^flight/list/(?P<south>.*)/(?P<west>.*)/(?P<north>.*)/(?P<east>.*)/", 
        "flights_for_boundary", name="flights_for_boundary"),

)


