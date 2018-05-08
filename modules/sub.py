#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# _____       _         _                       _       
#/  ___|     | |       | |                     (_)      
#\ `--. _   _| |__   __| | ___  _ __ ___   __ _ _ _ __  
# `--. \ | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \ 
#/\__/ / |_| | |_) | (_| | (_) | | | | | | (_| | | | | |
#\____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_|
# author  : joker-Security   
# WEBSITE : http://dev-labs.co
# GITHUB  : https://github.com/joker25000
# Twitter : https://twitter.com/SecurityJoker
# YOUTUBE : https://www.youtube.com/c/Professionalhacker25
# FACE Pg : https://facebook.com/kali.linux.pentesting.tutorials                                                 

#Module dependencies
import json
import requests
import argparse
from urlparse import urlparse

#Colors
class colors():
    bleu = "\033[94m"
    rouge= "\033[91m"

def results(algeria):
	with open ('resultat.txt','w') as k:
		json.dump(algeria,k)
parser = argparse.ArgumentParser(description='Simple Script Python For Searching Subdomain And Domain ')
parser.add_argument('-t','--targets', action='store',help='Your Target Choice',required=True)
parser.add_argument('-l','--language', help='Your Language Of Searching \n\n\t(fr)-French\n\t(en)-English', required=False)
kader = parser.parse_args()
targets=kader.targets
language=kader.language
if language is None:
	language="en"
if ((language != "fr") and (language !="en")):
	print "\033[91mThis Language not available"
	exit(1)
link="https://sedo.com/service/common.php?safe_search=2&synonyms=true&number_of_words_min=1&number_of_words_max=0&len_min=1&len_max=0&special_characters%5B%5D=3&special_characters%5B%5D=1&special_characters%5B%5D=2&cat%5B%5D=0&cat%5B%5D=0&cat%5B%5D=0&type=0&special_inventory=4&kws=contains&age_min=0&age_max=0&keyword="+targets+"&page=1&rel=6&orderdirection=2&domainIds=&cc=&member=&v=0.1&o=json&m=search&f=requestSearch&pagesize=100&keywords_join=AND&language="+language
joker=requests.get(link)
sanfour=joker.text
algeria = json.loads(sanfour)

name=[]
print "Your Target Choice :\033[91m"+targets
for dz in algeria['b']['general']['searchRequest']['resultList']:
	if dz != None:
		print dz['0']
		name.append(dz['0'])
	results(name)
