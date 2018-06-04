# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Script di test del servizio
"""

from TwitterAPI import TwitterAPI
consumer_key='put something here'
consumer_secret='put something here'
access_token_key='put something here'
access_token_secret='put something here'
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
#r = api.request('statuses/update', {'status':'FakeFight from Demo_FF_test!'})
r = api.request('search/tweets', {'q':'#Governo'})
print (r.status_code)
SCREEN_NAME='alexdelprete'
r = api.request('users/lookup', {'screen_name':SCREEN_NAME})
for item in r.get_iterator():
    print (item['user']['screen_name'])
risposta='Cioè M5S e Borghi si lamentano, la lamentela viene ripresa da FT, e diventa una prova. Giochiamo a "specchio riflesso"?'
r = api.request('search/tweets', {'q':'#spread'})
for item in r.get_iterator():
    print (item['user']['text'])
