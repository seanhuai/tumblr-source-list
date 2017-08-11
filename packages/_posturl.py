# -*- coding: utf-8 -*-

import os

class Posturl:

    def __init__(self,pre):
        self.pre = pre
        self.id = pre['response']['posts'][0]['id']
        self.type = pre['response']['posts'][0]['type']
        if self.type == 'photo':
            self.getPhoto()
        else:
            self.getVideo()
        if pre['response']['blog']['is_adult'] or pre['response']['blog']['is_nsfw']:
            confirm = input('你正在获取的内容不宜于未成年人，如需继续，请输入 Y 确认：')
            if confirm == 'Y':
                self.writeFile()
            else:
                print('已取消')
        else:
            self.writeFile()        

    def getVideo(self):
        pre = self.pre        
        if pre['response']['posts'][0]['video_type'] == 'tumblr':
            context = pre['response']['posts'][0]['video_url']
        self.context = context

    def getPhoto(self):
        pre = self.pre
        context = ''
        for x in range(0,len(pre['response']['posts'][0]['photos'])):
            context += pre['response']['posts'][0]['photos'][x]['original_size']['url']+'\n'
        self.context = context
    
    def writeFile(self):
        pre = self.pre
        f = open(str(self.id)+'_'+self.type+'.txt','a')
        f.write(str(self.context))
        f.close