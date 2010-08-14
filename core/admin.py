
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from core.models import Airline, Airport, Country, Rating


class AirlineAdmin(admin.ModelAdmin):
    
    list_display = ("name", "callsign", "country", "iata_code", "icao_code",)
    list_display_links = ("name", "callsign", "country", "iata_code", 
        "icao_code",)
    list_filter = ("country",)
    search_fields = ("name", "callsign", "country", "iata_code", "icao_code",)


class AirportAdmin(admin.ModelAdmin):
    
    list_display = ("name", "city", "country", "iata_code", "icao_code", 
        "latitude", "longitude",)
    list_display_links = ("name", "city", "country", "iata_code", "icao_code", 
        "latitude", "longitude",)
    list_filter = ("country",)
    search_fields = ("name", "city", "country", "iata_code", "icao_code",)


class RatingAdmin(admin.ModelAdmin):
    
    list_display = ("avatar_link", "name", "flight", "airline", 
        "airport_from", "airport_to", "value", "time",)
    list_display_links = ("name", "flight", "airline", 
        "airport_from", "airport_to", "value", "time",)
    fieldsets = (
        (None, {"fields": (("name", "value", "avatar_url"),)}),
        (_("Flight info"), {"fields": 
            (("flight", "airline"), ("airport_from", "airport_to"))},),
        (_("Twitter info"), {"fields": (("tweet_id", "tweet_text",),),
            "classes": ("collapse",)},),
    )

admin.site.register(Airline, AirlineAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Country)
admin.site.register(Rating, RatingAdmin)

