import tweepy
import time

#print(dir(tweepy))

authenticated = tweepy.OAuthHandler("exJzlKobNxv1bVFweqLKKdLv7","kBhTin1PXqWxQCq4APCe1jJ2LOU1Qg9Jy5eeOc5kDgSYX3JZ7l")
authenticated.set_access_token("1419295999000924160-a04KMeRxvcET4QkvWRPWF71ZNL6H4r","CqpG5Rx3K25CSxu28ZzT6uxsmrQ3ygnluUiXZxFBtQSPL")

api = tweepy.API(authenticated)

tweets_public = api.home_timeline()
for tweet in tweets_public:
 	print(tweet.text)
 
#following back

def limit(cursor):
	try:
	 while True:
	   yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(200)

for follower in limit(tweepy.Cursor(api.followers).items()):
	#following a particular person
	if follower.followers_count > 100:
	 follower.follow()
	break
	#print(follower.name)
'''
following a specific following ratio count 
 if follower.followers_count > 100 

 '''