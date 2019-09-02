#! /usr/local/bin/python3

import tweepy
import os
import random
import time
import datetime
import base64


def get_api():

    CONSUMER_API_KEY = "API_KEY"
    CONSUMER_API_SECRET_KEY = "API_SECRET_KEY"
    ACCESS_TOKEN = "ACCESS_TOKEN"
    ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET"

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    return api

def get_rand_str():

    rand = os.urandom(100)
    rand = str(base64.b64encode(rand))[2:68]

    return rand

def get_time():

    now = datetime.datetime.now()
    hr = now.hour
    mn = now.minute
    sc = now.second

    return hr, mn, sc

def next_number_time(hr, mn):

    if mn >= 50:
        hr = (hr + 1) % 24
    mn = ((mn//10)*10 + 10) % 60

    x, y = [str(hr), str(mn)]

    if hr in range(10):
        x = '0' + x

    if mn in range(10):
        y = '0' + y

    return x, y

def wait_time(mn, sc):
    
    now = (60*mn + sc) % 300
    left = 300 - now
    
    if left >= 150:
        left -= 150
    else:
        left += 150

    return left

def main():
    
    api = get_api()


    while True:

        #Get time now in hr:mn
        hr, mn, sc = get_time()

        #Post a tweet every 5 minutes starting from 02m30s - 2 tweets per number
        wait = wait_time(mn, sc)s
        time.sleep(wait)

        #Do a time-check every 1000 tweets
        for i in range(1000):

            hr, mn, _ = get_time()
            hr, mn = next_number_time(hr, mn)

            randstring = get_rand_str()

            #Post a new tweet
            api.update_status("#unicorn_beacon Entropy for number that will start computing at " + hr + "h" + mn + "m is " + randstring)
            print("Added entropy for number at " + hr + "h" + mn + "m")

            #Sleep for 5 minutes
            time.sleep(300)

    return 0


main()
