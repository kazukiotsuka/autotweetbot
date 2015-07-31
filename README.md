Simple Auto Tweet Bot
======================

This bot saves your precious time by tweeting randomly from your past tweets in some regular interval. written with python. for GAE


###1. Get Twitter API Keys  

At first, you need to register a twitter app by using the account you want to make tweet automatically.   

https://apps.twitter.com/

#####Then, you can get  ***"Consumer Keys"***, ***"Consumer Secret"***, ***"Access Token Key"***, ***"Access Token Secret"***

_※please make sure that the permission (Access Level) is ***"Read, write, and direct messages"***_


###2. Put these keys into keys.py

```python
twitter_access_keys = {
'consumer_key' : 'YOUR CONSUMER KEY',
'consumer_secret' : 'CONSUMER SECRET',
'access_token_key' : 'ACCESS TOKEN KEY',
'access_token_secret' : 'ACCESS TOKEN SECRET'
}
```

###3. Get GAE app

https://appengine.google.com/

###4. Put the appname of GAE app into app.yaml

`application: yourappname`


###4. Adjust fetches limit

The default value is 200 tweets x _100_ pages.
If you want to change, set a number to  

`MAXPAGES = 100`  

in main.py


###5. List up exclusing words

If you set the exclusing list, this bot doesn't pick up the tweets including any of these words.  

```python
exclude_list = [
u'tweets includes words here is excluded from random choice',
u'',
u'',
...

]
```

###6. Set up the cron interval

`schedule: every 300 minutes`

_schedule task syntax_  
https://developers.google.com/appengine/docs/python/config/cron


###7. Deploy it  

Now your twitter account begins to tweet automatically.  

  
  
  
  
  
---
This program is including Tweepy 2.2  
https://github.com/tweepy/tweepy
