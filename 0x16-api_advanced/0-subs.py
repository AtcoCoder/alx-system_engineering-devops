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
    content = response.json()
    try:
        data = content['data']
        subscribers = data['subscribers']
    except Exception:
        return 0
    return subscribers
