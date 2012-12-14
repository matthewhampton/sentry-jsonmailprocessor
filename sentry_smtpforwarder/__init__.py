"""
sentry_smtpforwarder
~~~~~~~~~~~~~~
"""

try:
    VERSION = __import__('pkg_resources')\
    .get_distribution('sentry_smtpforwarder').version
except Exception, e:
    VERSION = 'unknown'
