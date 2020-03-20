import GetOldTweets3 as got


def query():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#AAPL').setSince('2019-05-01').setUntil('2019-09-30').setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    print(tweet.text)


if __name__ == '__main__':
    query()
