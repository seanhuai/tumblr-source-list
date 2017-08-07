# 0.170807.3
import sys
from funcs import tumblr_pics
from funcs import tumblr_video

def getlist(args):
    
    username = args[1]
    if len(args) == 4:
        limit = args[2]
        mediatype = args[3]
    elif len(args) == 3:
        limit = args[2]
        mediatype = 'pics'
    elif len(args) == 2:
        limit = 3
        mediatype = 'pics'

    if mediatype == 'pics':
        tumblr_pics(username,limit)
    elif mediatype == 'video':
        tumblr_video(username,limit)
    elif mediatype == 'both':
        tumblr_pics(username,limit)  
        tumblr_video(username,limit)
    else:
        print("参数有误")

args = sys.argv
getlist(args)