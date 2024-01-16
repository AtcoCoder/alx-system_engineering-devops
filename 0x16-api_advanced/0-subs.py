#!/usr/bin/python3
""" reddit api function """
import requests



def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about"
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    response = requests.get(url, headers=headers)
    print(response)
    
number_of_subscribers("programming")


