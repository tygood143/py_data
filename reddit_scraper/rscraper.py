import praw

class Rscraper:
    
    def __init__(self, user_agent, client_id, client_secret):
        self.user_agent=user_agent
        self.client_id=client_id
        self.client_secret=client_secret
   
    #creates reddit instance   
    reddit = praw.Reddit(user_agent=user_agent,
               client_secret=client_secret,
               client_id=client_id)
    
    #extracts all comments into a csv file or list
    def comments(self, post_id,csv=False):
        post = reddit.submission(id=post_id).comments
        #gets rid of more comments button when there are a lot of comments
        post.replace_more(limit=None)
        a = [i.body for i in post.list()]
        if csv:
            #turns into csv
            df = pd.Series(data=a)
            df.to_csv('comments.csv', index=True, encoding='utf-8')
        else:
            #if returned as list, will get comment format i.e. \n, links, etc.
            #don't know how to fix that yet
            return a