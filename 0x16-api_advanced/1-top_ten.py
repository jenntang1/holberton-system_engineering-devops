#!/usr/bin/python3
""" Query Reddit API """


import requests


def top_ten(subreddit):
    """
    Query for the titles of the first ten hot posts
    for a given subreddit
    Arg:
        subreddit: given subreddit
    Return:
        total subscribers in integer
    """

    """ If no subreddit was given """
    if subreddit is None:
        print(None)

    """ Try query but return KeyError if no data key found """
    try:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".\
            format(subreddit)
        response = requests.get(url, headers={"User-agent": "please-thanks"}).\
            json()

        children_list = response["data"]["children"]

        for elmt_dicts in children_list:
            for data, data_values in elmt_dicts.items():
                if data == "data":
                    for title, title_values in data_values.items():
                        if title == "title":
                            print(title_values)
    except KeyError:
        print(None)
