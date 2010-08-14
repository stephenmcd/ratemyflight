
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

    
class Airline(models.Model):
   
    name = models.CharField(_("Name"), max_length=100)
    callsign = models.CharField(_("Call sign"), max_length=200, blank=True, 
        null=True)
    country = models.ForeignKey("Country", related_name="airlines", null=True)
    iata_code = models.CharField(_("IATA Code"), max_length=3, blank=True, 
        null=True)
    icao_code = models.CharField(_("ICAO Code"), max_length=3, blank=True, 
        null=True)

    class Meta:
        verbose_name = _("Airline")
        verbose_name_plural = _("Airlines")
        ordering = ("name",)

    def __unicode__(self):
        return self.name


class Airport(models.Model):
    
    name = models.CharField(_("Name"), max_length=100)
    city = models.CharField(_("City"), max_length=100)
    country = models.ForeignKey("Country", related_name="airports")
    iata_code = models.CharField(_("IATA Code"), max_length=3, blank=True, 
        null=True)
    icao_code = models.CharField(_("ICAO Code"), max_length=4, unique=True)
    latitude = models.FloatField(_("Latitude"))
    longitude = models.FloatField(_("Longitude"))

    class Meta:
        verbose_name = _("Airport")
        verbose_name_plural = _("Airports")
        ordering = ("name",)

    def __unicode__(self):
        return self.name


class Country(models.Model):

    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = ("name",)

    def __unicode__(self):
        return self.name


class Rating(models.Model):
   
    name = models.CharField(_("Name"), max_length=100)
    avatar_url = models.URLField(_("Avatar URL"))
    value = models.FloatField(_("Rating"), null=True)
    time = models.DateTimeField("Date/Time", default=datetime.now)
    flight = models.CharField(_("Flight number"), max_length=10,
        blank=True, null=True)
    airline = models.ForeignKey("Airline", related_name="ratings", 
        blank=True, null=True)
    airport_from = models.ForeignKey("Airport", verbose_name="Airport from",
        related_name="airports_from", blank=True, null=True)
    airport_to = models.ForeignKey("Airport", verbose_name="Airport to",
        related_name="airports_to", blank=True, null=True)
    comment = models.TextField(_("Comment"), blank=True, null=True)
    tweet_id = models.IntegerField("Tweet ID", blank=True, null=True)
    tweet_text = models.CharField("Tweet text", max_length=140, blank=True, 
        null=True)

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")
        ordering = ("-id")

    def __unicode__(self):
        return str(self.value)

    def avatar_link(self):
        return "<img style='vertical-align:middle; margin-right:3px;' " \
            "src='%s' />" % self.avatar_url
    avatar_link.allow_tags = True
    avatar_link.short_description = ""

