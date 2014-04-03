autotweetbot
============

This bot tweets randomly from your past tweets and omits your time to use for keeping influences. written by python. for GAE

###Set up
============
###1. Get Twitter API Keys  

https://apps.twitter.com/

***"Consumer Keys"***, ***"Consumer Secret"***, ***"Access Token Key"***, ***"Access Token Secret"*** are neccessory.

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

###4. Put the appname into app.yaml

`application: yourappname`

###5. Set up the cron interval

`schedule: every 300 minutes`

_schedule task syntax_  
https://developers.google.com/appengine/docs/python/config/cron
