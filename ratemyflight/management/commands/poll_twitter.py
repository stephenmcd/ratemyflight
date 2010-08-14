
from datetime import datetime, timedelta
from time import timezone
from urllib2 import urlopen, quote, HTTPError

from django.core.management.base import NoArgsCommand
from django.utils.simplejson import loads

from ratemyflight.models import Airline, Airport, Rating


hashtag = "#ratemyflight"
url = "http://search.twitter.com/search.json?q=%s" % quote(hashtag)

# Put the airports and airlines into dicts by IATA code for fast lookup that 
# doesn't hammer the database, otherwise our server might be susceptible to a 
# DOS attack via tweets.
airports = Airport.objects.all()
airports = dict([(a.iata_code, a) for a in airports if a.iata_code])
airlines = Airline.objects.all()
airlines = dict([(a.iata_code, a) for a in airlines if a.iata_code])


class Command(NoArgsCommand):
    """
    Polls the Twitter API for ratings with the #ratemyflight hashtag.
    """
    def handle_noargs(self, **options):
        # Hit the twitter search API with the #ratemyflight hashtag to search 
        # for tweeted ratings. Use the tweet's username and avatar for the 
        # rating, then try and parse the flight number, airports and rating 
        # from the tweet text. Finally we only save the rating if we have 
        # parsed enough meaningful information.
        try:
            json = urlopen(url).read()
        except HTTPError:
            return
        tweets = loads(json)["results"]
        for tweet in tweets:
            tweet_id = tweet["id"]
            rating, created = Rating.objects.get_or_create(tweet_id=tweet_id)
            if not created:
                continue
            rating.name = tweet["from_user"]
            rating.avatar_url = tweet["profile_image_url"]
            rating.tweet_text = tweet["text"]
            rating.time = datetime.strptime(tweet["created_at"], 
                "%a, %d %b %Y %H:%M:%S +0000") - timedelta(seconds=timezone)
            parts = tweet["text"].split()
            parsed = [] 
            # ``parsed`` stores the indexes of parsed parts to remove them 
            # from the final tweet text.
            for (i, part) in enumerate(parts):
                # A flight number is found when the first two chars are 
                # an airline IATA code and remaning chars are numeric.
                if not rating.flight and part[:2] in airlines and \
                    part[2:].isdigit():
                    parsed.append(i)
                    rating.flight = part
                    rating.airline = airlines[part[:2]]
                # When an airport code is found, assume the departure 
                # airport is first.
                if (not rating.airport_from or not rating.airport_to) and \
                    part in airports:
                    if not rating.airport_from:
                        parsed.append(i)
                        rating.airport_from = airports[part]
                    elif not rating.airport_to:
                        parsed.append(i)
                        rating.airport_to = airports[part]
                # A rating could be in the format 4.5/10
                if not rating.value and \
                    part.split("/")[0].replace(".", "", 1).isdigit():
                    parsed.append(i)
                    rating.value = float(part.split("/")[0])
                # Mark the hashtag to be removed.
                if part.lower() == hashtag.lower():
                    parsed.append(i)
            parts = [p for (i, p) in enumerate(parts) if i not in parsed]
            rating.comment = " ".join(parts)
            # If we have a rating and either both airports or a flight number
            # then save the rating.
            if rating.value and ((rating.airport_from or rating.airport_to) or 
                rating.flight):
                rating.save()

