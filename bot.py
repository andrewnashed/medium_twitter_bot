import tweepy
import dotenv
import os
from models import Tweet

dotenv.load_dotenv()


def create_tweet():
    client = tweepy.Client(consumer_key=os.getenv('API_KEY'), consumer_secret=os.getenv('API_SECRET'),
                           access_token=os.getenv('ACCESS_TOKEN'),
                           access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'),
                           )
    try:
        response = client.create_tweet(text='Hello everyone!')
        return response
    except Exception:
        return 'an error occured'


def retweet(tweet_id):
    client = tweepy.Client(consumer_key=os.getenv('API_KEY'), consumer_secret=os.getenv('API_SECRET'),
                           access_token=os.getenv('ACCESS_TOKEN'),
                           access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'),
                           )
    client.retweet(tweet_id)


def check_id(tweet_id):
    tweet = Tweet.query.filter_by(tweet_id=tweet_id).first()
    if tweet:
        return True
    return False


def search_recent_tweets():
    client = tweepy.Client(bearer_token=os.getenv('BEREAR_TOKEN'))
    tweets = client.search_recent_tweets(query='#medium')
    valid_ids = []
    for tw in tweets.data:
        if not check_id(tw.id):
            valid_ids.append(tw)
    return valid_ids



