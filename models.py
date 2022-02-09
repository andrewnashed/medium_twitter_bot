from db import db


class Tweet(db.Model):
    tweet_id = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<User %r>' % self.tweet_id