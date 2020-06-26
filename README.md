# Better Reddit Alerts
A post notification system that will check if anyone you are following on Reddit has posted within the last 24 hours. If there are any new posts, it will send a message containing all the new posts in a tabular format that is easily readable and compact on both mobile and desktop. The table contains the post title, post author, post subreddit, link to the post, and the number of comments the post has.

# Purpose
Reddit currently has no way of recieving notifications from people you are following. Instead it blends in posts from users with posts from subreddits you are following. I enjoy content that certain people on Reddit post, so I want to know what they are posting regardless of what subreddit it is in. I wanted to create a script that would send messages from people I follow, but also not clutter my phone with notifications so once a day the script will check for new posts, if there aren't any it wont send a message but if there are any new posts it will send all new posts in a message since the last time checked. It sends the message to your Reddit account that way you still get the notification from the Reddit app.

# Usage
Go to https://www.reddit.com/prefs/apps and click on this button<br>![alt text](https://i.imgur.com/C2KpTxC.png "Developer Button")<br>
Under create application fill out the details as follows then select create app<br> ![alt text](https://i.imgur.com/7Nqv4ih.png "Create App")<br>
You should now see the script.<br>
![alt text](https://i.imgur.com/uZQpS5B.png "Script")<br>
RedditScraper is the `user_agent`. Under "personal use script" is the `client_id`. Secret is the `client_secret`.<br>
In a directory place the `reddit_scraper.py` and `example_praw.ini` files. Rename the `example_praw.ini` to `praw.ini`.<br>
Open `praw.ini` and fill out all the fields. `username` and `password` are the username and password for the Reddit account.
```
[user]
user_agent=
client_id=
client_secret=
username=
password=
```
Finally, make sure the PRAW and Pause libraries are installed by using `pip install praw` and `pip install pause`.

## Desktop View
![alt text](https://i.imgur.com/8D4qs5P.png "Desktop View")

## Mobile View
![alt text](https://i.imgur.com/BIWBYbE.png "Mobile View")
