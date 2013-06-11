"""
sentry_jsonmailprocessor
~~~~~~~~~~~~~~
"""

try:
    VERSION = __import__('pkg_resources')\
    .get_distribution('sentry_jsonmailprocessor').version
except Exception, e:
    VERSION = 'unknown'
