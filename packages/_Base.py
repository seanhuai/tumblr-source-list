# -*- coding: utf-8 -*-

import os

class Base:
    
    def __init__(self,args):
        pass

    def getSource(self, limit = 0):
        posts, mediatype = self.pre['response']['posts'], self.mediatype
        res = []
        z = []
        for x in posts:
            if mediatype == 'photo':
                for y in x['photos']:                 
                    res.append(y['original_size']['url'])
            else:
                if x['video_type'] == 'tumblr':
                    res.append(x['video_url'])
        self.res = res
    
    def checkAdult(self,res):
        pre = self.pre
        if pre['response']['blog']['is_adult'] or pre['response']['blog']['is_nsfw']:
            confirm = input('你正在获取的内容不宜于未成年人，如需继续，请输入 Y 确认：')
            if confirm == 'Y':
                self.writeFile(res)
            else:
                print('已取消')
        else:
            self.writeFile(res)

    def writeFile(self,res):
        username, mediatype = self.username, self.mediatype
        with open('{username}_{mediatype}.txt'.format(username = username, mediatype = mediatype),'a') as f:
            for x in res:
                f.write(x+'\n')