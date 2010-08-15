#!/usr/bin/env python

"""
Convert the HTML table ``data/airlines.html`` into airline obects.
Table taken from http://en.wikipedia.org/wiki/Airline_codes-All
"""

import os
import sys

scripts_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(scripts_path, "..")))
os.environ["DJANGO_SETTINGS_MODULE"] = "example_project.settings"

from BeautifulSoup import BeautifulSoup
from ratemyflight.models import Country, Airline


with open(os.path.join(scripts_path, "data", "airlines.html"), "r") as f:
    for tr in BeautifulSoup(f.read())("tr"):
        cells = [unicode(td).replace("<td>", "").replace("</td>", "") 
            for td in tr("td")]
        if cells and not cells[-1]: # Ignore cells with a comment.
            airline = Airline()
            if cells[0].strip():
                airline.iata_code = cells[0].strip()
            if cells[1].strip():
                airline.icao_code = cells[1].strip()
            a.name = cells[2]
            if ">" in airline.name:
                airline.name = airline.name.replace("</a>", "").split(">")[1]
            if cells[3].strip():
                airline.callsign = cells[3].strip()
            if cells[4].strip():
                airline.country, created = Country.objects.get_or_create(
                    name=cells[4].strip())
            airline.save()
