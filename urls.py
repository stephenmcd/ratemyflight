
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    url("^api/", include("core.urls")),
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
)

if getattr(settings, "DEV_SERVER", False):
    urlpatterns += patterns("",
        ("^%s/(?P<path>.*)$" % settings.MEDIA_URL.strip("/"),
            "django.views.static.serve",
                {"document_root": settings.MEDIA_ROOT}),
        ("^favicon.ico$", "django.views.static.serve", {"document_root":
            settings.MEDIA_ROOT, "path": "img/favicon.ico"}),
    )
