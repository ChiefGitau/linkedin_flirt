import logging
import os

import tweepy

logger = logging.getLogger('twitter')

auth = tweepy.OAuthHandler(
    os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_API_SECRET")
)

auth.set_access_token(
    os.environ.get("TWITTER_ACCESS_TOKEN"), os.environ.get("TWITTER_ACCESS_SECRET")
)

api = tweepy.API(auth)