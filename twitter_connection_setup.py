import tweepy

# We import our access keys:

# Consume:
CONSUMER_KEY    = 'nwVs6YNP10O0vzWOHkVJ0eDgR'
CONSUMER_SECRET = 'aVcA7nuqLFc1CVb3uWCM4yEZYOP5qIjWHyOZ3fsZ3EOiqhoxnU'

# Access:
ACCESS_TOKEN  = '928109258-XDscdmCehF5ZRStwObVkFaTleR90q96nk5hJ3Zqh'
ACCESS_SECRET = 'pJksbGMEPtjtkmAa2Yu4594dIdt5nrNrxCAhqCJOdQcRk'


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

print(twitter_setup())

def collect():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="french",rpp=50)
    for tweet in tweets:
        print(tweet.text)





