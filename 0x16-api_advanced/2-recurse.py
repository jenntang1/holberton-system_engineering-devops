#!/usr/bin/python3
""" Query Reddit API """


import requests


def recurse(subreddit):
    """
    Query for the titles of hot articles
    for a given subreddit
    Arg:
        subreddit: given subreddit
    Return:
        titles of hot articles
    """

    """ If no subreddit was given """
    if subreddit is None:
        return None

    """ Implementing recursion """
    return get_limit(subreddit)


def get_limit(subreddit):
    """
    Query for the entire json of a given subreddit
    Arg:
       subreddit: given subreddit
    Return:
        entire json
    """

    """ Retrieving json from Reddit API """
    url = "https://www.reddit.com/r/{}/hot.json?limit=20&after_id=40".\
        format(subreddit)
    response = requests.get(url, headers={"User-agent": "please-thanks"}).\
        json()
    return response
