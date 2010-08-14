
from django.conf.urls.defaults import *


urlpatterns = patterns("ratemyflight.views",
    url("^airport/list/(?P<south>.*)/(?P<west>.*)/(?P<north>.*)/(?P<east>.*)/", 
        "airports_for_boundary", name="airports_for_boundary"),
)


