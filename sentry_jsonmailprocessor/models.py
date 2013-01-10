"""
sentry_jsonmailprocessor.models
~~~~~~~~~~~~~~~~~~~~~
"""

from django import forms

from sentry.conf import settings
from sentry.plugins import Plugin, register
from sentry.plugins.sentry_mail.models import MailProcessor

import sentry_jsonmailprocessor
import json

"""
 Extends the existing mailer plugin and overrides the get_plaintext_body() method
 to send the event data in JSON format.
"""

#@register
class JsonMailProcessor(MailProcessor):
	# Plug-in vars.
    author = 'Justin C'
    author_url = None
    version = sentry_jsonmailprocessor.VERSION
    description = "Sentry event forwarding via SMTP in JSON format."
    slug = 'jsonmailprocessor'
    title = 'JSON Mailer'
    conf_title = title
    conf_key = 'jsonmailprocessor'

	# Overrides the method from MailProcessor
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
       
    
        
    
