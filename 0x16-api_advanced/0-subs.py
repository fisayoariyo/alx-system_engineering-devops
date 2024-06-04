#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers to the subreddit, or 0 if
        the request fails or the subreddit does not exist.
    """
    
    # Make a GET request to the Reddit API to fetch subreddit information
    sub_info = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )
    
    # Check for errors in the request
    if sub_info.status_code >= 300:
        return 0
    
    # Parse the JSON response to extract the number of subscribers
    return sub_info.json().get("data").get("subscribers")

if __name__ == "__main__":
    # Example usage
    subreddit = "python"  # Replace with your subreddit of interest
    print(f"The number of subscribers in r/{subreddit} is: {number_of_subscribers(subreddit)}")

