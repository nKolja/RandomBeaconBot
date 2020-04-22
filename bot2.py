#! /usr/local/bin/python3

import tweepy
import os
import random
import time
import datetime

#Read html
from bs4 import BeautifulSoup
from six.moves.urllib.request import urlopen



# Randomize "The quick brown fox jumps over the lazy dog"

determiner_1 = ["The"]
adjective_1 = ["quick", "nimble", "fast", "swift", "rapid", "speedy", "brisk", "agile"]
colour_1 = ["brown", "black", "red", "white", "spotted", "orange", "grey", "silver"]
animal_1 = ["fox", "dog", "cat", "wolf", "jackal", "coyote",  "dingo", "dhole"]
verb_1 = ["jumped", "hopped", "leaped", "pounced", "skipped", "dashed", "bounced", "springed"]
preposition_1 = ["over", "above", "atop", "around", "across", "next to", "ahead", "beyond"]
determinder_2 = ["the"]
adjective_2 = ["lazy", "slow", "phlegmatic", "idle", "slothful", "laying", "indifferent", "sleepy"]
animal_2 = ["dog", "fox", "cat", "wolf", "jackal", "coyote",  "dingo", "dhole"]
additional = ["and"]
verb_2 = ["barked", "said", "meowed", "woofed", "howled", "growled", "yipped", "yelped"]
sound_1 = ["Bark", "Boof", "Meow", "Woof", "Howl", "Growl", "Yipp", "Yelp", "bark", "boof", "meow", "woof", "howl", "growl", "yipp", "yelp"]
sound_2 = ["bark", "boof", "meow", "woof", "howl", "growl", "yipp", "yelp"]
stop_symbol = [".", "!"]

degree_symb = u'\xb0'.encode('utf-8')



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

    random.seed(os.urandom(12))

    rand_str = ""
    rand_str += determiner_1[random.randint(0,len(determiner_1)-1)] + " "
    rand_str += adjective_1[random.randint(0,len(adjective_1)-1)] + " "
    rand_str += colour_1[random.randint(0,len(colour_1)-1)] + " "
    rand_str += animal_1[random.randint(0,len(animal_1)-1)] + " "
    rand_str += verb_1[random.randint(0,len(verb_1)-1)] + " "
    rand_str += preposition_1[random.randint(0,len(preposition_1)-1)] + " "
    rand_str += determinder_2[random.randint(0,len(determinder_2)-1)] + " "
    rand_str += adjective_2[random.randint(0,len(adjective_2)-1)] + " "
    rand_str += animal_2[random.randint(0,len(animal_2)-1)] + " "
    rand_str += additional[random.randint(0,len(additional)-1)] + " "
    rand_str += verb_2[random.randint(0,len(verb_2)-1)] + ": "
    rand_str += sound_1[random.randint(0,len(sound_1)-1)] + ", "
    rand_str += sound_2[random.randint(0,len(sound_2)-1)]
    rand_str += stop_symbol[random.randint(0,len(stop_symbol)-1)]

    #curr_len = len(rand_str)
    #rand_str += str(base64.b64encode(os.urandom(8)))[2:]
    #rand_str = rand_str[0:curr_len+6] + "!"


    
    return rand_str

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
    if left >+ 150:
        left -= 150
    else:
        left += 150

    return left

def main():
    
    api = get_api()

    while True:

        #Get time now in hr:mn
        hr, mn, sc = get_time()

        #Post a tweet every 5 minutes starting from 00h02m30s - 2 tweets per number
        #This function computes how long we need to wait until **h*2m30s or **h*7m30s
        wait = wait_time(mn, sc)


        time.sleep(wait)


        while True:
            webpage = "http://trx.epfl.ch/beacon/index.php"
            soup = BeautifulSoup(urlopen(webpage), "html.parser")
            unicorn_webpage = soup.find_all("div", attrs={"class":"section"})        
            if (len(unicorn_webpage) >= 5):
                break
            time.sleep(1)

               
        beacon_number = unicorn_webpage[5].text.strip()[38:43]

        randstring = get_rand_str()

        #Encoding strings into utf-8 is used for Python 2
        tw1 = u"#unicorn_beacon Entropy for beacon n".encode('utf-8') + degree_symb
        tw2 = " " + beacon_number + " is: \"" + randstring + "\""
        
        tweet = tw1 + tw2.encode('utf-8')

        #Post a new tweet
        api.update_status(tweet)
        #print(tweet)

        time.sleep(5)


    return 0






main()
