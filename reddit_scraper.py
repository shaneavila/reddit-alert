import praw

posts = []
title_set = set()
reddit = praw.Reddit('user')
subreddit = reddit.subreddit('friends').new(limit=25)
# To avoid posts in multiple subreddits with identical names
for post in subreddit:
    if post.title not in title_set:
        title_set.add(post.title)
        posts.append([post.title, str(post.subreddit), post.shortlink + " ", str(post.num_comments)])
format_titles = '|'.join(['title', 'subreddit', 'url', '# of comments\n'])
format_separation = '|'.join(['-', '-', '-', '-\n'])
for i in range(len(posts)):
    posts[i] = '|'.join(posts[i])
format_table = '\n'.join(posts)
reddit.redditor('urmom723').message('New Posts', format_titles + format_separation + format_table)
