import os

from flask import Flask
from db import db
from bot import search_recent_tweets, retweet
from models import Tweet
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def ping():
    return True


@app.route('/retweet')
def retweet():
    tweets = search_recent_tweets()
    for tw in tweets:
        retweet(tw)
        new_id = Tweet(
            tweet_id=tw
        )
        db.session.add(new_id)
        db.session.commit()


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
