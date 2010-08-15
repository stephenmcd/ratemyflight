
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("ratemyflight.views",
    url("^api/airport/list/(?P<south>.*)/(?P<west>.*)/(?P<north>.*)/(?P<east>.*)/", 
        "airports_for_boundary", name="airports_for_boundary"),
    url("^api/flight/list/(?P<south>.*)/(?P<west>.*)/(?P<north>.*)/(?P<east>.*)/", 
        "flights_for_boundary", name="flights_for_boundary"),
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
)


