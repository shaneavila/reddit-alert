from bs4 import BeautifulSoup
import pandas
import praw
import requests

reddit = praw.Reddit('user')
old_submission = set()
site = 'https://reddit.com'

for submission in reddit.subreddit('friends').new(limit=50):
    if submission.title not in old_submission:
        old_submission.add(submission.title)
        print('{}: {}'.format(submission.title, site + submission.permalink))

'''
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'first'})
len(results)
'''
