#!/usr/bin/python3
""" Query Reddit API """


import requests


def number_of_subscribers(subreddit):
    """
    Query for the number of total subscribers
    for a given subreddit
    Arg:
        subreddit: given subreddit
    Return:
        total subscribers in integer
    """

    """ If no subreddit was given """
    if subreddit is None:
        return 0

    """ Try query but return KeyError if no data key found """
    try:
        url = "https://www.reddit.com/r/{}/about.json".\
            format(subreddit)
        response = requests.get(url, headers={"User-agent": "please-thanks"}).\
            json()
        total = response["data"]["subscribers"]
        return total
    except KeyError:
        return 0
