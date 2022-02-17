# Keep this file separate

# https://apps.twitter.com/
# Create new App and get the four strings
import os


def oauth():
    return {"consumer_key": os.getenv("consumer_key"),
            "consumer_secret": os.getenv("consumer_secret"),
            "token_key": os.getenv("token_key"),
            "token_secret": os.getenv("token_secret") }
