#!/usr/bin/python
"""
no of subs
"""
import requests

def number_of_subscribers(subreddit):
    if not isinstance(subreddit, str) or not subreddit:
        return 0
    
    user_agent = "Custom User Agent"
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        """
        to raise an error for bad response status
        """
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0


