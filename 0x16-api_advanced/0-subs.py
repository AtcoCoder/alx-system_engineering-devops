#!/usr/bin/python3
""" reddit api function """
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    content = response.json()
    data = content['data']
    subscribers = data['subscribers']
    return subscribers
