# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views import View
import hackernews
from twilio.twiml.voice_response import VoiceResponse

class HackerNewsStories(View):
    """
    Hacker News Stories View
    """

    def get(self, request):
        """
        Return top Hacker News story headlines in TwiML format
        """
        headlines = hackernews.get_headlines(5);
        resp = VoiceResponse()
        for headline in headlines:
            resp.say(headline, voice='woman', language='en-gb')

        twiml_str = str(resp)
        return HttpResponse(twiml_str, content_type='text/xml')
