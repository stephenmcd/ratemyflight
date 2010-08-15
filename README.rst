========
Overview
========

`Rate My Flight`_ is a Django application that allows users to rate flights 
they've taken. The application focuses around the homepage which displays a 
map of the world and can be used to display data collected in various ways. 
Ratings can be entered directly on the website or via twitter. 

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

Notes
=====

`Rate My Flight`_ has no specific dependencies but was developed and deployed 
with the following software selected for its environment, and using 
alternatives may result in issues due to limited amount of testing over the 
48 hour competition period::

  * `Python 2.5`_
  * `Django 1.2`_
  * `Ubuntu`_
  * `Google Chrome`_ - Firefox showed various issues with Google maps. Internet Explorer surely won't render some elements.
  * `MySQL`_ - aftering installing fixtures, the column ``ratemyflight_airline.name`` requires its collation to be set to unicode.

.. _`Rate My Flight`: http://ratemyflight.org
.. _`Andrew Fisher`: http://ajfisher.me
.. _`Josh de Blank`: http://www.joshdeblank.com
.. _`Stephen McDonald`: http://jupo.org
.. _`Django Dash`: http://djangodash.com
.. _`setuptools`: http://pypi.python.org/pypi/setuptools
.. _`distribute`: http://pypi.python.org/pypi/distribute
.. _`Python 2.5`: http://python.org
.. _`Django 1.2`: http://djangoproject.com
.. _`Ubuntu`: http://ubuntu.com
.. _`Google Chrome`_: http://www.google.com/chrome/
.. _`MySQL`: http://mysql.com

