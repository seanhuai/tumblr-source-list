from packages._Base import *

class Username(Base):

    def __init__(self,args):
        self.username, self.mediatype, self.pre = args[0], args[1], args[2]


class Posturl(Base):

    def __init__(self,args):
        self.pre, self.pid = args[0], args[1] 
        self.mediatype = self.pre['response']['posts'][0]['type']
    
    def writeFile(self,res):
        pid, mediatype = self.pid, self.mediatype
        with open('{pid}_{mediatype}.txt'.format(pid = pid, mediatype = mediatype),'a') as f:
            for x in res:
                f.write(x+'\n')