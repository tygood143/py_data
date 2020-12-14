from logins import client_id, client_secret, user_agent
import praw
from praw.models import MoreComments
import pandas as pd 


reddit = praw.Reddit(
client_id=client_id,
client_secret=client_secret,
user_agent=user_agent,)
#replace thsi id with id of post you want to scrape
id= 'h7u3ea'

comments = reddit.submission(id=id).comments
#gets rid of more comments button when there are a lot of comments
comments.replace_more(limit=None)
comment_list = [i.body for i in comments.list()]

#stores comments in csv
df = pd.Series(data=comment_list)
df.to_csv('/Users/tylergood/py_git/py_data/reddit_scraper/comments.csv', index=True, encoding='utf-8')
