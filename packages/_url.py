class Url():

    def setUserName(self,username):
        self.username = username
    def setMediaType(self,mediatype):
        self.mediatype = mediatype
    def setTags(self,tags):
        self.tags = tags
    def setAPI(self,api):
        self.api = api
    def setLimit(self,limit):
        self.limit = limit

    def getReqUrl(self):
        url = 'http://api.tumblr.com/v2/blog/'+ self.username +'.tumblr.com/posts/'+ self.mediatype +'?api_key='+ self.api +'&offset='+ self.limit
        return url

    def setPostUrl(self,posturl):
        self.posturl = posturl

    def getPostUrl(self):
        posturl = self.posturl
        postdetail = posturl.split('/')
        self.domain = postdetail[2]
        self.postid = postdetail[4]
        url = 'http://api.tumblr.com/v2/blog/'+ self.domain +'/posts?id='+ self.postid +'&api_key='+ self.api
        return url