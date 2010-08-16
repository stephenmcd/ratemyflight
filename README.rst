========
Overview
========

`Rate My Flight`_ is a Django application that allows users to rate flights 
they've taken. The application consists of two parts: an API and the homepage 
which implements it by displaying a map of the world which can be used to 
display data collected in various ways. Ratings can be entered directly on 
the website or via twitter. 

`Rate My Flight`_ was created by `Andrew Fisher`_, `Josh de Blank`_ and 
`Stephen McDonald`_ for the `Django Dash`_ competition 2010.

Installation
============

`Rate My Flight`_ is available on pypi and can be installed via 
`setuptools`_::

    $ easy_install -U ratemyflight
    
or via `distribute`_::

    $ pip install ratemyflight
    
Once installed you can run the command ``ratemyflight project_name`` which 
will create a new Django project with the given ``project_name`` that has the 
``ratemyflight`` app installed.

Consuming Tweets
================

In order to consume tweets it is necessary to create a cron job that runs 
the command in your project's directory::

    $ python manage.py poll_twitter
    
Once the cron job is running it will consume tweets containing the hash tag 
``#ratemyflight`` if found to contain rating information in the following 
format::

    flight_number airport_from airport_to rating comment hashtag

For example if you flew British Airways (BA) flight 227 from Sydney (SYD) to 
Los Angeles (LAX) and gave it a rating of 8 you'd tweet::

    BA227 SYD LAX 8/10 I really enjoyed this flight! #ratemyflight

API
===

`Rate My Flight`_ primarily consists of an API callable over HTTP that 
returns JSON data. The following URLs are implemented.

``/api/airport/boundary/<south>/<west>/<north>/<east>/``
Returns a list of airports (maximum defined in 
``ratemyflight.settings.MAX_AIRPORTS``) within the given boundaries ``<south>``, 
``<west>``, ``<north>`` and ``<east>`` which make up latitude and longitude 
in decimal format.

``/api/flight/boundary/<south>/<west>/<north>/<east>/``
Returns a list of flights (maximum defined in 
``ratemyflight.settings.MAX_FLIGHTS``) within the given boundaries ``<south>``, 
``<west>``, ``<north>`` and ``<east>`` which make up latitude and longitude 
in decimal format.

``/api/flight/airline/<iata_code>/``
Returns a list of flights (maximum defined in 
``ratemyflight.settings.MAX_FLIGHTS``) for the given airline using its given 
``<iata_code>``.

``/api/flight/username/<username>/``
Returns a list of flights (maximum defined in 
``ratemyflight.settings.MAX_FLIGHTS``) that have been given ratings by the 
given ``<username>``.

``/api/flight/recent/``
Returns the most recent flights (maximum defined in 
``ratemyflight.settings.MAX_FLIGHTS``).

JSON
----

The following examples show the JSON format returns for aiports and flights.

Airports::

    [
        {
            pk: 9044,
            model: "ratemyflight.airport",
            fields: {
                city: "Adelaide",
                name: "Adelaide International",
                icao_code: "YPAD",
                longitude: 138.530555555556,
                iata_code: "ADL",
                country: 235,
                latitude: -34.945
            }
        }
    ]

Flights::

    [
        {
            comment: "I like turtles!!",
            flight: "GQ483",
            name: "stephen_mcd",
            tweet_id: null,
            airport_from_id: 9075,
            airport_from: {
                city: "Tamworth",
                name: "Tamworth",
                icao_code: "YSTW",
                country_id: 235,
                longitude: 150.846666666667,
                iata_code: "TMW",
                latitude: -31.0838888888889,
                id: 9075
            },
            tweet_text: null,
            value: 6.7,
            airport_to_id: 2082,
            avatar_url: "http://a3.twimg.com/profile_images/690849843/UNI_2223_normal.jpg",
            airline_id: 1428,
            airport_to: {
                city: "Swartkop",
                name: "Swartkop",
                icao_code: "FASK",
                country_id: 43,
                longitude: 28.1644444444444,
                iata_code: "N/A",
                latitude: -25.8094444444444,
                id: 2082
            },
            id: 81
        }
    ]

Notes
=====

`Rate My Flight`_ has no specific dependencies but was developed and deployed 
with the following software selected for its environment, and using 
alternatives may result in issues due to limited amount of testing over the 
48 hour competition period.

  * `Python 2.5`_
  * `Django 1.2`_
  * `nginx`_
  * `gunicorn`_
  * `gunicorn-console`_
  * `Ubuntu`_
  * `Google Chrome`_ - `Firefox`_ showed various issues with `Google Maps`_. `Internet Explorer`_ surely won't render some elements.
  * `SQLite`_ - `MySQL`_ can be used but will raise an error while installing fixtures. In this case simply set the collation for the column ``ratemyflight_airline.name`` to unicode and re-run ``syncdb``.

.. _`Rate My Flight`: http://ratemyflight.org
.. _`Andrew Fisher`: http://ajfisher.me
.. _`Josh de Blank`: http://www.joshdeblank.com
.. _`Stephen McDonald`: http://jupo.org
.. _`Django Dash`: http://djangodash.com
.. _`setuptools`: http://pypi.python.org/pypi/setuptools
.. _`distribute`: http://pypi.python.org/pypi/distribute
.. _`Python 2.5`: http://python.org
.. _`Django 1.2`: http://djangoproject.com
.. _`nginx`: http://nginx.net
.. _`gunicorn`: http://gunicorn.org
.. _`gunicorn-console`: http://pypi.python.org/pypi/gunicorn-console/
.. _`Ubuntu`: http://ubuntu.com
.. _`Google Chrome`: http://www.google.com/chrome/
.. _`Firefox`: http://mozilla.com/firefox/
.. _`Google Maps`: http://maps.google.com
.. _`Internet Explorer`: http://www.microsoft.com/windows/internet-explorer
.. _`SQLite`: http://www.sqlite.org
.. _`MySQL`: http://mysql.com

