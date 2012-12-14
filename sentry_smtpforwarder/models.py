"""
sentry_smtpforwarder.models
~~~~~~~~~~~~~~~~~~~~~
"""

from django import forms

from sentry.conf import settings
from sentry.plugins import Plugin, register
from sentry.plugins.sentry_mail.models import MailProcessor

import sentry_smtpforwarder
import json

@register
class Smtpforwarder(MailProcessor):
    author = 'Justin C'
    version = sentry_smtpforwarder.VERSION
    description = "Sentry event forwarding via SMTP."
    slug = 'smtpforwarder'
    title = 'SMTP Forwarder'
    conf_title = title
    conf_key = 'smtpforwarder'

    def get_plaintext_body(self, group, event, link, interface_list):
        import pdb; pdb.set_trace()
        header = "SENTRY_EVENT_MAIL"
        data = dict()
        data['server_name'] = event.server_name
        data['culprit'] = event.culprit
        data['level'] = event.level
        data['event_id'] = event.event_id
        data['message'] = event.message
        data['date'] = str(event.datetime)
        data['data'] = event.data
        return " ".join([header, json.dumps(data, separators=(',', ':'))])
