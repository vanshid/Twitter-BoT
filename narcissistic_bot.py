import tweepy
import time

#print(dir(tweepy))

authenticated = tweepy.OAuthHandler("exJzlKobNxv1bVFweqLKKdLv7","kBhTin1PXqWxQCq4APCe1jJ2LOU1Qg9Jy5eeOc5kDgSYX3JZ7l")
authenticated.set_access_token("1419295999000924160-a04KMeRxvcET4QkvWRPWF71ZNL6H4r","CqpG5Rx3K25CSxu28ZzT6uxsmrQ3ygnluUiXZxFBtQSPL")

api = tweepy.API(authenticated)

tweets_public = api.home_timeline()
for tweet in tweets_public:
 	print(tweet.text)

 #setting api limit server

def limit(cursor):
	try:
	 while True:
	  yield cursor.next()
	except tweep.RateLimitError:
		time.sleep(200)

word_search = "Football"
no_of_tweets = 4
 
for tweet in tweepy.cursor(api.search, word_search).items(no_of_tweets):
	try:
		tweet.favorite()
		tweet.retweet()
		print("Woah that's in my fav list!!!!")
	except tweepy.TweepError as te:
		print(te.reason)
	except StopIteration:
		break
