# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

# !! This is the configuration of Nikola. !! #
# !!  You should edit it to your liking.  !! #

# Data about this site
BLOG_AUTHOR = "punchagan"  # (translatable)
BLOG_TITLE = "Crumb Demo Site"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "https://punchagan.github.io/crumb-demo"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "https://punchagan.github.io/crumb-demo"
BLOG_EMAIL = "punchagan+github@muse-amuse.in"
BLOG_DESCRIPTION = "This is a demo site for Crumb -- a GitHub based commenting system."  # (translatable)

DEFAULT_LANG = 'en'

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/archive.html", "Archive"),
        ("/categories/index.html", "Tags"),
        ("/rss.xml", "RSS feed"),
    ),
}

# Name of the theme to use.
THEME = "bootstrap3"

TIMEZONE = "Asia/Kolkata"

POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
)
PAGES = (
    ("stories/*.rst", "stories", "story.tmpl"),
    ("stories/*.txt", "stories", "story.tmpl"),
)

COMPILERS = {
    "rest": ('.rst', '.txt'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm'),
    # PHP files are rendered the usual way (i.e. with the full templates).
    # The resulting files have .php extensions, making it possible to run
    # them without reconfiguring your server to recognize them.
    "php": ('.php',),
    # Pandoc detects the input from the source filename
    # but is disabled by default as it would conflict
    # with many of the others.
    # "pandoc": ('.rst', '.md', '.txt'),
}

CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": ''
        }
    )
}

CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="http://getnikola.com" rel="nofollow">Nikola</a>         {license}'

# To use comments, you can choose between different third party comment
# systems.  The following comment systems are supported by Nikola:
#   disqus, facebook, googleplus, intensedebate, isso, livefyre, muut
# You can leave this option blank to disable comments.
COMMENT_SYSTEM = "crumb"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = "s-pZZUF7vnkxXD1k89-Y3KJVrkM/punchagan/crumb-demo"

SOCIAL_BUTTONS_CODE = ""

LOGGING_HANDLERS = {
    'stderr': {'loglevel': 'INFO', 'bubble': True},
    # 'smtp': {
    #     'from_addr': 'test-errors@example.com',
    #     'recipients': ('test@example.com'),
    #     'credentials':('testusername', 'password'),
    #     'server_addr': ('127.0.0.1', 25),
    #     'secure': (),
    #     'level': 'DEBUG',
    #     'bubble': True
    # }
}
