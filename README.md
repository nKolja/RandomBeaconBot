# RandomBeaconBot
RandomBeaconBot is a bot that publishes a tweet with 32 bits of entropy every 5 minutes.
Thanks for https://twitter.com/UtahraptorECC for the idea, and some helpful code on https://github.com/P1K/UTAHRAPTOR_ECC/ !

This bot helps the unicorn beacon - [trx.epfl.ch/beacon/](trx.epfl.ch/beacon/) - to generate random numbers. The beacon computes a random number every 10 minutes using the seeds gathered in a 10minute pre-processing window. During that time all the tweets with the hashtag #unicorn_beacon are gathered and used as a seed in order to compute a random number. Furthermore the randomness of that number is uncontestable and can be proved after the number is published. For more info visit [trx.epfl.ch/beacon/](trx.epfl.ch/beacon/) .

This bot publishes a randomly generated sentence in 5 minute intervals starting from 2m30s of each hour.

_Dependencies_: 
 - tweepy - a library for connecting to twitter and posting tweets
 - Beautiful soup 4 - a library for extracting the current beacon number from the unicorn beacon website
