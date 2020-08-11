# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mark McLoughlin'
SITENAME = u"Crusty Blaa"
SITEURL = 'https://crustyblaa.com'

PATH = 'content'
THEME = './theme'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('markmc_', 'http://twitter.com/markmc_'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
