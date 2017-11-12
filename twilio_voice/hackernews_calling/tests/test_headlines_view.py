# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory
import mock
from twilio_voice.hackernews_calling.views import HackerNewsStories

class TestHeadlinesView(TestCase):

    @mock.patch('twilio_voice.hackernews_calling.hackernews.get_headlines', return_value=['headline 1'])
    def test_headlines_xml(self, get_headlines_patched_func):
        request = RequestFactory()
        endpoint = 'headlines'
        get_headlines = request.get(endpoint)
        twiml_response = HackerNewsStories.as_view()(get_headlines)
        self.assertEqual(get_headlines_patched_func.call_count, 1)
        self.assertEqual(twiml_response.status_code, 200)
        expected_content = '<?xml version="1.0" encoding="UTF-8"?><Response><Say voice="woman" language="en-gb">headline 1</Say></Response>'
        self.assertEqual(twiml_response.content, expected_content)
