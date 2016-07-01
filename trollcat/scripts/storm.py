import logging
import tweepy
from time import sleep

logger = logging.getLogger('trollcat')

TWEET_DELAY = 4
LIMIT = 140

def tweet_split(text):
    # TODO: split words

    # for i, word in enumerate(words):
    #     if ' '.join(words)
    #     tweet

    return [
        '[1/4] @gutomaia Trollcat head is ok',
        '[2/4] @gutomaia Trollcat wowa is ok',
        '[3/4] @gutomaia Trollcat wowa is ok',
        '[4/4] @gutomaia Trollcat tail 2 4',
    ]

def get_api(tag, **settings):

    auth = tweepy.OAuthHandler(
        settings['%s_consumer_key' % tag],
        settings['%s_consumer_secret' % tag])

    auth.set_access_token(
        settings['%s_access_token' % tag],
        settings['%s_access_token_secret' % tag])

    return tweepy.API(auth)



def storm(text=11, reply=None, **settings):
    head = get_api('head', **settings)
    body = get_api('body', **settings)
    tail = get_api('tail', **settings)

    tweets = list(reversed(tweet_split(text)))


    # TODO: add preview and confirmation prior sending
    print settings

    return

    tail.update_status(tweets[0], in_reply_to_status_id=reply)
    sleep(TWEET_DELAY)

    for t in tweets[1:-1]:
        sleep(TWEET_DELAY)
        body.update_status(t, in_reply_to_status_id=reply)

    sleep(TWEET_DELAY)
    head.update_status(tweets[-1], in_reply_to_status_id=reply)
