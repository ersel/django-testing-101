# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views import View
import hackernews

class HackerNewsStories(View):
    """
    Hacker News Stories View
    """

    def get(self, request):
        """
        Return top Hacker News story headlines in TwiML format
        """
        twiml_str = '<?xml version="1.0" encoding="UTF-8"?>'
        twiml_str += '<Response>'
        headlines = hackernews.get_headlines(5);
        for headline in headlines:
            twiml_str += '<Say voice="woman" language="en-gb">{0}</Say>'.format(headline)
        twiml_str += '</Response>'

        return HttpResponse(twiml_str, content_type='text/xml')
