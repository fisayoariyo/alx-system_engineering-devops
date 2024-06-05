#!/usr/bin/python3
"""Module for querying the Reddit API to get the number of subscribers of a subreddit"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers to the subreddit

    Args:
        subreddit (str): The name of the subreddit to query.

    Return:
        int: The number of subscribers to the subreddit, or 0 if
        the request fails or the subreddit does not exist.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        response = requests.get(url, headers={"User-Agent": "reddit-subscriber-counter"})
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0

