import re
import tweepy
from tweepy import OAuthHandler
import operator
import json
from collections import Counter
 
import hybrid

################################################
##STOP WORDS######################

from nltk.corpus import stopwords
import string

punctuation=list(string.punctuation)
stop = stopwords.words('english') + punctuation +['rt','RT','via']
#################################################
import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

##################################################
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        access_token = '327284428-gCvR2imeV7Izmupgl1Y7wYC7Xsq7GBtOg9bwl3ap'
        access_token_secret = 'NmYEcWCEQmaF9YvYUaIOPxDEGskuiy9tQCxq50dhqtj0F'
        consumer_key = '0UJSM5veBNvIs2j8UmaxB7XBO'
        consumer_secret = 'PICmVh55kaCw10VtuvqBwhvWSdSLu6o6D8uaP0Wy727ZqsIxbC'
 
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    
 
    def get_tweets(self, query, count = 200):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
 
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)
 
            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
                # saving text of tweet
                parsed_tweet['text'] = self.clean_tweet(tweet.text)
              
 
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
 
def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    c_pos=0
    c_neg=0
    c_neutral=0
    # calling function to get tweets
    tweets = api.get_tweets(query = '#yogi', count = 200)
    #for tweet in tweets:
     #   x=int(hybrid.myFunction(tweet['text']))
     #    if(x==4):
     #       c_pos+=1
      #  elif(x==2):
       #     c_neutral+=1
       # else:
        #    c_neg+=1  
    #print(str(c_pos)+" "+str(c_neg)+" "+str(c_neutral))
    count_all=Counter()
    for tweet in tweets:
        terms_all = [term for term in preprocess(tweet['text']) if term not in stop]
        count_all.update(terms_all)
    print(count_all.most_common(10))
if __name__ == "__main__":
    # calling main function
    main()
