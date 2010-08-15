#!/usr/bin/env python

"""
Create some random flights.
"""

import os
import sys

scripts_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(scripts_path, "..")))
os.environ["DJANGO_SETTINGS_MODULE"] = "example_project.settings"

from random import choice, random, randint

from ratemyflight.models import Rating, Airline, Airport


airports = [a for a in Airport.objects.all() if a.iata_code]
airlines = [a for a in Airline.objects.all() if a.iata_code]

users = (
    ("stephen_mcd", "http://a3.twimg.com/profile_images/690849843/UNI_2223_normal.jpg"),
    ("ajfisher", "http://a2.twimg.com/profile_images/93415866/afisher_citrus.com.au_aa97ef53_normal.jpg"),
    ("joshwins", "http://a0.twimg.com/profile_images/179238148/n820185192_3656151_9483_normal.jpg"),
)

flights = 100

for i in range(flights):
    user = choice(users)
    rating = Rating()
    rating.name = user[0]
    rating.avatar_url = user[1]
    rating.value = float("%.1f" % (random() * 10.))
    rating.airline = choice(airlines)
    rating.flight = "%s%s" % (rating.airline.iata_code, randint(100, 999))
    rating.airport_from = choice(airports)
    while not rating.airport_to or \
        rating.airport_from.id == rating.airport_to.id:
        rating.airport_to = choice(airports)
    rating.comment = "I like turtles!!"
    rating.save()

