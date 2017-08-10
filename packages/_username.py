import os

class Username:
    
    def __init__(self,username,mediatype,pre):
        self.username = username
        self.mediatype = mediatype
        self.pre = pre
        if mediatype == 'photo':
            self.getPics()
        elif mediatype == 'video':
            self.getVideo()
        if pre['response']['blog']['is_adult'] or pre['response']['blog']['is_nsfw']:
            confirm = input('你正在获取的内容不宜于未成年人，如需继续，请输入 Y 确认：')
            if confirm == 'Y':
                self.writeFile()
            else:
                print('已取消')
        else:
            self.writeFile()
            
    def getPics(self):
        pre = self.pre
        context = ''
        for i in range(0,len(pre['response']['posts'])):
            for x in range(0,len(pre['response']['posts'][i]['photos'])):
                context += pre['response']['posts'][i]['photos'][x]['original_size']['url']+'\n'
        self.context = context
    
    def getVideo(self):
        pre = self.pre        
        context = ''
        for i in range(0,len(pre['response']['posts'])):
            if pre['response']['posts'][i]['video_type'] == 'tumblr':
                context += pre['response']['posts'][i]['video_url']+'\n'
        self.context = context
    
    def writeFile(self):
        username = self.username
        mediatype = self.mediatype
        if (os.path.isdir(username) == False):
            os.mkdir(username)
        f = open(username+'/'+username+'_'+mediatype+'.txt','a')
        f.write(str(self.context))
        f.close