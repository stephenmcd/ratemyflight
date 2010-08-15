#!/usr/bin/env python

"""
Convert the text database ``data/airports.txt`` into airport obects.
Database taken from http://www.partow.net/miscellaneous/airportdatabase/
"""

import os
import sys

scripts_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(scripts_path, "..")))
os.environ["DJANGO_SETTINGS_MODULE"] = "example_project.settings"

from ratemyflight.models import Country, Airport


with open(os.path.join(scripts_path, "data", "airports.txt"), "r") as f:
    for line in f:
        parts = line.strip().split(":")
        airport = Airport()
        airport.icao_code = parts[0]
        airport.iata_code = parts[1]
        airport.name = parts[2].title()
        airport.city = parts[3].title()
        name = parts[4].title()
        airport.country, created = Country.objects.get_or_create(name=name)
        lat = float(parts[5]) + float(parts[6]) / 60. + float(parts[7]) / 3600.
        if parts[8] == "S":
            lat *= -1
        airport.latitude = lat
        lon = float(parts[9]) + float(parts[10]) / 60. + float(parts[11]) / 3600.
        if parts[12] in ("W", "U"):
            lon *= -1
        airport.longitude = lon
        airport.save()



