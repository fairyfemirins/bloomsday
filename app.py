#!/usr/bin/env python3
"""
Bloomsday - Positive News Aggregator

Features:
- Fetch positive news from Reddit (mock data for MVP).
- Display news in a simple frontend.
"""

import os
import requests
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "bloomsday/1.0")


def get_reddit_token():
    """Get OAuth token for Reddit API."""
    auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET)
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=auth,
        data=data,
        headers={"User-Agent": REDDIT_USER_AGENT}
    )
    return response.json().get("access_token")


def fetch_positive_news():
    """Fetch positive news from Reddit."""
    token = get_reddit_token()
    headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": REDDIT_USER_AGENT
    }
    
    # Fetch posts from subreddits known for positive news
    subreddits = ["UpliftingNews", "HappyNews", "GoodNews", "PositiveNews"]
    posts = []
    
    for subreddit in subreddits:
        response = requests.get(
            f"https://oauth.reddit.com/r/{subreddit}/hot?limit=5",
            headers=headers
        )
        if response.status_code == 200:
            posts.extend(response.json()["data"]["children"])
    
    # Filter and format posts
    positive_news = []
    for post in posts:
        positive_news.append({
            "title": post["data"]["title"],
            "url": f"https://reddit.com{post['data']['permalink']}",
            "score": post["data"]["score"],
            "subreddit": post["data"]["subreddit"]
        })
    
    return positive_news


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/news')
def get_news():
    # Mock data for testing
    news = [
        {
            "title": "Scientists Discover a New Species of Butterfly in the Amazon Rainforest",
            "url": "https://reddit.com/r/UpliftingNews/comments/123456",
            "score": 1200,
            "subreddit": "UpliftingNews"
        },
        {
            "title": "Community Raises $50,000 for Local Family in Need",
            "url": "https://reddit.com/r/HappyNews/comments/789012",
            "score": 850,
            "subreddit": "HappyNews"
        },
        {
            "title": "Teen Develops App to Help Elderly Neighbors with Groceries",
            "url": "https://reddit.com/r/GoodNews/comments/345678",
            "score": 2300,
            "subreddit": "GoodNews"
        }
    ]
    return jsonify(news)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)