from bs4 import BeautifulSoup
from ordered_set import OrderedSet
import requests
import pandas
import praw


posts = []
title_set = set()
reddit = praw.Reddit('user')
subreddit = reddit.subreddit('friends').new(limit=25)
# To avoid posts in multiple subreddits with identical names
for post in subreddit:
    if post.title not in title_set:
        title_set.add(post.title)
        posts.append([post.title, post.subreddit, post.shortlink, post.num_comments])
posts = pandas.DataFrame(posts, columns=['title', 'subreddit', 'url', '# of comments'])
reddit.redditor('urmom723').message('TEST',
                                    '''Column A | Column B | Column C
                                    ---------|----------|----------
                                    A1 | B1 | C1
                                    A2 | B2 | C2''')
