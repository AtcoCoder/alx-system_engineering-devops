#!/usr/bin/python3
""" reddit api function """
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
    url = f"https://www.reddit.com/r/{subreddit}/.json"
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'sort': 'hot', 'limit': 100}

    response = requests.get(
        url,
        params=params,
        headers=headers,
        allow_redirects=False)
    if response.status_code != 200:
        return print(None)
    content = response.json()
    posts = content['data']['children']
    for post in posts:
        title = post['data']['title']
        print(title)
