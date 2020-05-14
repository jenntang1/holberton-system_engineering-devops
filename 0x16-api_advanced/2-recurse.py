#!/usr/bin/python3
""" Query Reddit API """


import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Query for the titles of hot articles
    for a given subreddit
    Arg:
        subreddit: given subreddit
    Return:
        titles of hot articles
    """

    if after is None:
        return None

    elif subreddit is None:
        return None

    else:
        try:
            params = {"after": after, "limit": 20}

            url = "https://www.reddit.com/r/{}/hot.json?".\
                format(subreddit)

            response = requests.get(url,
                                    params=params,
                                    allow_redirects=False,
                                    headers={"User-agent": "please-thanks"})

            results = response.json()

            for elmt_dicts in results["data"]["children"]:
                for title in elmt_dicts["data"]["title"]:
                    if title == "title":
                        hot_list.append(title)

            return recurse(subreddit, hot_list=[], after=results["data"])
        except KeyError:
            return None
