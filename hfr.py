# High fidelity reddit script
# Finds comments with equal or greater karma than parent karma

#TODO parse reddit page 'reddit.com' 'reddit.com/r/x' for posts
#TODO In a post, find parent and child comment karma. Need to this recursively? For every child look at grandchild
#TODO Print link to awesome comments
#TODO Figure out the API secret thing. Don't commit the API key! OAuth?

import praw
from praw.models import MoreComments
import requests
import requests.auth

# client_auth = requests.auth.HTTPBasicAuth('Zll5_fdpFwwn1g', '4HtMXIh3w3o5Y24F1pzJfNwPQMs')
# post_data = {"grant_type": "password", "username": "srs_sput", "password": "JZA9kLzzmq#7IrDbY2wamPX^P*u*u39B&hd6w^SsAIB^lR1&JJF26oGnojvIOxi5"}
# headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
# response.json()

reddit = praw.Reddit(client_id='KOfCVjtEpTZM0g',
                     client_secret="UUZwbktcmcx8kJgqAOLWqXjwMgk", password='JZA9kLzzmq#7IrDbY2wamPX^P*u*u39B&hd6w^SsAIB^lR1&JJF26oGnojvIOxi5',
                     user_agent='USERAGENT', username='srs_sput')
"""
https://www.reddit.com/r/funny/comments/5om9es/people_running_backwards_put_in_reverse_looks/
https://www.reddit.com/r/harrypotter/comments/2b99jx/if_hogwarts_visited_another_school_for_the/
"""
submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/5om9es/people_running_backwards_put_in_reverse_looks/')

# Prints top level comments
# for top_level_comment in submission.comments:
#     if isinstance(top_level_comment, MoreComments):
#         continue
#     parent_karma = top_level_comment.ups
#     print(top_level_comment.body)

# Get comment tree in breadth first
# Visit each top node then each bottom node, level by level

# go to bottom of a branch
# see if bottom branch has more karma than parent branch
# once all bottom branches are checked go to next parent branch
"""
    1    2
   / \  / \
  A  B C  D
"""
# Go to A, see if A > 1 then B > 1
# Go to 2, see if C > 2 then D > 2

# http://interactivepython.org/runestone/static/pythonds/Trees/TreeTraversals.html

# Breadthfirst would be perfect. Just check every child has more karma than parent
# submission.comments.list()[0].parent().ups gives the actual post karma lol
# submission.comments.list()[0].parent().body gives AttributeError: 'Submission' object has no attribute 'body'


submission.comments.replace_more(limit=0)
for index, comment in enumerate(submission.comments.list()):
    try:
        catch = comment.parent().body
        if comment.ups > 5 and int(comment.ups*1.5) > comment.parent().ups :
            print('reddit.com' + comment.parent().permalink())
    except AttributeError:
        catch = 0

    # if 'imagine that would be pretty uncomfortable for all the people in Hogwarts that' in comment.body:
    #     print(index)

    # for reply in comment.replies
        # comment.replies for replies
        # comment.ups for karma
        # comment.permalink() for URL
