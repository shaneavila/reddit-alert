import praw
import schedule

posts = []
url_set = set()
message_user = 'urmom723'
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
    reddit.redditor(message_user).message('New Posts', format_title + format_columns + format_table)
    posts.clear()


schedule.every(8).hours.do(output)
for post in subreddit.stream.submissions(skip_existing=True):
    # Avoids posts that link to the same url in multiple subreddits
    if post.url not in url_set:
        url_set.add(post.url)
        posts.insert(0, post)
    if len(posts) > 0:
        schedule.run_pending()
