#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kousuke Ebihara'
SITENAME = u'co3k.org'
SITEURL = ''

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'ja'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

THEME = "themes/basic"
MENUITEMS = [("About", "/"), ("Blog", "/category/blog.html")]
ARTICLE_SAVE_AS = "blog/{slug}.html"
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_LANG_URL = "blog/{slug}-{lang}.html"
ARTICLE_LANG_SAVE_AS = "blog/{slug}-{lang}.html"
AUTHOR_SAVE_AS = ""
AUTHOR_URL = ""

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
