import praw

posts = []
url_set = set()
message_user = 'urmom723'
reddit = praw.Reddit('user')
subreddit = reddit.subreddit('friends').new(limit=25)
# Avoids posts that link to the same url in multiple subreddits
for post in subreddit:
    if post.url not in url_set:
        url_set.add(post.url)
        posts.append([post.title, str(post.subreddit), post.shortlink + " ", str(post.num_comments)])
format_titles = '|'.join(['title', 'subreddit', 'url', '# of comments\n'])
format_separation = '|'.join(['-', '-', '-', '-\n'])
for i in range(len(posts)):
    posts[i] = '|'.join(posts[i])
format_table = '\n'.join(posts)
reddit.redditor(message_user).message('New Posts', format_titles + format_separation + format_table)

# TODO messaging a username to the bot will add it to friends list
# TODO keep track of most recent post - if post is same as last post send no message
