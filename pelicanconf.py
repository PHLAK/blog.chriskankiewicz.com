#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site info
AUTHOR       = 'Chris Kankiewicz'
SITENAME     = 'Chris Kankiewicz'
SITEBLURB    = 'Thoughts and ramblings of a web geek'
AUTHOR_EMAIL = 'Chris@ChrisKankiewicz.com'
SITEURL      = 'http://blog.chriskankiewicz.com'

# Site timezone
TIMEZONE = 'America/Phoenix'

# Set defaults
DEFAULT_LANG        = 'en'
DEFAULT_CATEGORY    = 'Uncategorized'
DEFAULT_DATE_FORMAT = ('%B %d, %Y - %I:%M %p')

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM         = None
# CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None

# Theming
THEME = 'themes/bootstrapped'

SUMMARY_MAX_LENGTH = 80


# Analytics
GOOGLE_ANALYTICS = {
    'id': 'UA-00000000-1',
    'url': 'blog.chriskankiewicz.com'
}

# Plugins
PLUGIN_PATH = 'plugins'
PLUGINS = [
    'googleplus_comments',
    'gravatar',
    'related_posts',
    'share_post',
    'sitemap'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Static Paths
# STATIC_PATHS = ['images']

# Blogroll
LINKS =  (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/')
)

# Social widget
SOCIAL = (
    ('Google+', 'https://plus.google.com/+ChrisKankiewicz'),
    ('Twitter', 'https://twitter.com/PHLAK'),
    ('GitHub', 'https://github.com/PHLAK')
)

# Pagination
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Output retention
OUTPUT_RETENTION = ('.gitignore')