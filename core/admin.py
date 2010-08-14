from django.contrib import admin
from core.models import Airline, Airport, Country, Rating


class AirlineAdmin(admin.ModelAdmin):
    
    list_display = ("name", "callsign", "country", "iata_code", "icao_code",)
    list_filter = ("country",)
    search_fields = ("name", "callsign", "country", "iata_code", "icao_code",)


class AirportAdmin(admin.ModelAdmin):
    
    list_display = ("name", "city", "country", "iata_code", "icao_code", 
        "latitude", "longitude",)
    list_filter = ("country",)
    search_fields = ("name", "city", "country", "iata_code", "icao_code",)


admin.site.register(Airline, AirlineAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Country)
admin.site.register(Rating)

