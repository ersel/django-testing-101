"""
This Module Talks to HackerNews API
to fetch latest headlines
"""
import json
import urllib2

def get_headlines(no_of_headlines):
    """
    gets the titles of top stories
    """
    top_story_ids = urllib2.urlopen("https://hacker-news.firebaseio.com/v0/topstories.json").read()

    ids = json.loads(top_story_ids)[:no_of_headlines]
    headlines = []
    for story_id in ids:
        story_url = "https://hacker-news.firebaseio.com/v0/item/{0}.json".format(story_id)
        story = urllib2.urlopen(story_url).read()
        story_json = json.loads(story)
        headlines.append(story_json["title"])
    return headlines

