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
	# plugin vars
    author = 'Justin C'
    version = sentry_smtpforwarder.VERSION
    description = "Sentry event forwarding via SMTP."
    slug = 'smtpforwarder'
    title = 'SMTP Forwarder'
    conf_title = title
    conf_key = 'smtpforwarder'

	# this overrides an abstracted method from MailProcessor
    def get_plaintext_body(self, group, event, link, interface_list):
        header = "SENTRY_EVENT_MAIL"
        
        data = {
            'server_name' : event.server_name,
            'culprit' : event.culprit,
            'level' : event.level,
            'event_id' : event.event_id,
            'message' : event.message,
            'date' : str(event.datetime),
            'data': event.data
        }
        return " ".join([header, json.dumps(data, separators=(',', ':'))])
       
    
        
    
