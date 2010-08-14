
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
)
