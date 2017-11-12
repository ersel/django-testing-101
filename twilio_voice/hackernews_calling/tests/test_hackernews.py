# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import httpretty
import re
from twilio_voice.hackernews_calling import hackernews

class TestHackerNewsService(TestCase):

    @httpretty.activate
    def test_get_headlines(self):
        # mock for top stories
        httpretty.register_uri(
            httpretty.GET,
            "https://hacker-news.firebaseio.com/v0/topstories.json",
           body="[1,2,3,4,5,6,7,8,9,10]")

        # mock for individual story item
        httpretty.register_uri(
            httpretty.GET,
            re.compile("https://hacker-news.firebaseio.com/v0/item/(\w+).json"),
            body="{\"title\":\"some story title\"}")

        headlines = hackernews.get_headlines(5);
        self.assertEqual(len(headlines), 5)
        self.assertEqual(headlines[0], 'some story title')
        last_request = httpretty.last_request()
        self.assertEqual(last_request.method, 'GET')
        self.assertEqual(last_request.path, '/v0/item/5.json')
