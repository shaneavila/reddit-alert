import praw
import pause

posts = []
url_set = set()
message_user = 'VirtualLeak'
reddit = praw.Reddit('user')
subreddit = reddit.subreddit('friends')


# Output post data in markdown table format
def output():
    format_title = '|'.join(['title', 'author', 'subreddit', 'url', '# of comments\n'])
    format_columns = '|'.join(['-', '-', '-', '-', '-\n'])
    for i in range(len(posts)):
        posts[i] = '|'.join([posts[i].title, str(posts[i].author), str(posts[i].subreddit),
                             posts[i].shortlink, str(posts[i].num_comments)])
    format_table = '\n'.join(posts)
    print(format_title + format_columns + format_table)
    reddit.redditor(message_user).message('New Posts', format_title + format_columns + format_table)
    posts.clear()


for post in subreddit.stream.submissions(pause_after=0):  # Optional parameters: pause_after=0, skip_existing=True
    # Avoids posts that link to the same url in multiple subreddits
    if post is not None and post.url not in url_set:
        url_set.add(post.url)
        posts.insert(0, post)
    # If there are new posts, send message
    if post is None and len(posts) > 0:
        output()
    # If there aren't any new posts, pause for 24 hours
    if len(posts) == 0:
        pause.hours(24)

