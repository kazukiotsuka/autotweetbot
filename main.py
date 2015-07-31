#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import tweepy
import keys
import excludes
import random
import logging

"""access keys"""
CONSUMER_KEY_BOT = keys.twitter_access_keys['consumer_key']
CONSUMER_SECRET_BOT = keys.twitter_access_keys['consumer_secret']
ACCESS_TOKEN_KEY_BOT = keys.twitter_access_keys['access_token_key']
ACCESS_TOKEN_SECRET_BOT = keys.twitter_access_keys['access_token_secret'] 

"""Api only for bot"""
auth = tweepy.OAuthHandler(CONSUMER_KEY_BOT, CONSUMER_SECRET_BOT)
auth.set_access_token(ACCESS_TOKEN_KEY_BOT, ACCESS_TOKEN_SECRET_BOT)
api = tweepy.API(auth_handler=auth)

"""Exclude words list"""
exlist = excludes.exclude_list

"""Fetch limit settings"""
MAXPAGES = 100

class AutoTweet(webapp2.RequestHandler):
	def get(self):
		alltweets = list(set(self.getTweets()))
		r = random.randint(0,len(alltweets)-1)
		logging.info(r)
		logging.info(alltweets[r])
		post = alltweets[r]
		api.update_status(post)

	def getTweets(self):
		twlist = []
		for tweets in tweepy.Cursor(api.user_timeline,count=200,include_rts=None,include_entities=None,contributor_details=None,trim_user=None).pages(MAXPAGES):
			for tweet in tweets:
				text = tweet.text
				logging.info(text)
				#check if text includes the word in exclusion list
				exclusive = None 
				for ex in exlist:
					if ex in text:
						exclusive = True
				if not exclusive:
					twlist.append(text)
		return twlist 

app = webapp2.WSGIApplication([
    ('/autotweet', AutoTweet)
], debug=True)
