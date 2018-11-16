from textblob import TextBlob, Word
import nltk
import tweepy
from tweet_collection.credentials import *
from tweet_collection.twitter_connection_setup import *

#many other imports to do

#Fonctionalité 8 :

#getting familiar with textblob :
'''wiki = TextBlob("""Python is a high-level, general-purpose programming language.""")
print(wiki.tags)
print(wiki.noun_phrases)

zen = TextBlob("But don't you hate him?")
print(zen.words)
print(zen.sentences)
print(zen.sentiment)

sentence = TextBlob('Use 4 spaces per indentation level. We are level 1')
print(sentence.word_counts['level'])'''



def collect_tweets(): #we create another function to collect tweets.
# This one returns a list of 50 tweets with the words "Emmanuel Macron".
    L = []
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron", language = "french", rpp=20)
    for tweet in tweets:
        L = L + [tweet.text]
    return L

tweets = collect_tweets()
'''print(tweets)'''

def get_words(tweet): #create a list of all the words in a tweet
    tweet_blob = TextBlob(tweet)
    tweet_blob = tweet_blob.words
    tweet_blob = tweet_blob.singularize()
    tweet_blob = tweet_blob.lemmatize() #Return a list of the words present in the 50 tweets, lemmatized and singularized
    L = []
    for word in tweet_blob: #we make sure each word is only present one time in the list
        if word not in L:
            L += [word]
    return L

Words = get_words(tweets[0])
'''print(Words)'''

#Fonctionalité 9 : analyse de l'opinion

def opinion_tweet(tweet): #to judge the polarity of a tweet we take the average polarity of all the words
    return sum(TextBlob(word).sentiment[0] for word in get_words(tweet))/len(tweet)

print(opinion_tweet('Les comptes de campagne montrent que Laurent Ruquier déteste'))

def opinion_tweets(tweets):
    pos_tweets = [] #list of the tweets with positive polarity
    neg_tweets = [] #list of the tweets with negative polarity
    neu_tweets = [] #list of the tweets with neutral polarity
    for tweet in tweets:
        if opinion_tweet(tweet) > 0:
            pos_tweets += [tweet]
        elif opinion_tweet(tweet) < 0:
            neg_tweets += [tweet]
        else:
            neu_tweets += [tweet]
    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(tweets)))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(tweets)))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(tweets)))

'''print(opinion_tweets(tweets))'''

