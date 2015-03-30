# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:37:45 2015

@author: delfi
"""
import tweepy

consumer_key = ""
consumer_secret = ""

access_key = ""
access_secret = ""

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#Do something
#USER_NAME = "oriolpujol"
#user = api.get_user(id=USER_NAME)

#Get followers niv1
USER_NAME="delfiobradors"
followers=api.followers_ids(id=USER_NAME)
#Ahora tenemos los followers de nivel 1

#Get 2nd level followers
followers2=[]
for user in followers[0:1]:
    followers_user=api.followers_ids(id=user)
    followers2.append(followers_user)       
print followers2
#Funciona, pero al iterar por TODOS los followers, da error de demasiados requests...
#Cómo hacemos para poner el temporizador y que no salte?
        
        