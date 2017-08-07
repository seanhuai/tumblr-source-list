# 0.170807.2
from urllib import request
import os
import json
import contextlib 

def getSource(username,pages,mediatype = 'photo'):

    key = 'AftvLjfZCBi2RoFDX4lzToNvuB4PhnEbymwBJPgK9BHqgh0ZsV'
    url = 'http://api.tumblr.com/v2/blog/'+username+'.tumblr.com/posts/'+str(mediatype)+'?api_key='+key+'&offset='+str(pages*20)

    proxy_handler = request.ProxyHandler({'http': 'http://localhost:1080/'})
    opener = request.build_opener(proxy_handler)
    connect = opener.open(url)
    r = connect.read() 
    pre = json.loads(r)
    
    return pre

def picsUrl(pre,username):

    context = ''
    for i in range(0,len(pre['response']['posts'])):
        for x in range(0,len(pre['response']['posts'][i]['photos'])):
            context += pre['response']['posts'][i]['photos'][x]['original_size']['url']+'\n'

    if (os.path.isdir(username) == False):
        os.mkdir(username)
    f = open(username+'/'+username+'_pics.txt','a')
    f.write(str(context))
    f.close

def tumblr_pics(username,limit):
    pages = int(limit)//20
    if pages == 0:
        picsUrl(getSource(username,pages),username)
    else:
        for i in range(0,(pages+1)):
            #print(i)
            picsUrl(getSource(username,i),username)
    print('download is finished')        


def videoUrl(pre,username):
    context = ''
    for i in range(0,len(pre['response']['posts'])):
        if pre['response']['posts'][i]['video_type'] == 'tumblr':
            context += pre['response']['posts'][i]['video_url']+'\n'
    
    if (os.path.isdir(username) == False):
        os.mkdir(username)
    f = open(username+'/'+username+'_video.txt','a')
    f.write(str(context))
    f.close

def tumblr_video(username,limit):
    pages = int(limit)//20
    if pages == 0:
        videoUrl(getSource(username,pages,'video'),username)
    else:
        for i in range(0,(pages+1)):
            #print(i)
            videoUrl(getSource(username,i,'video'),username)
    print('download is finished')    