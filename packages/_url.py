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
        url = 'http://api.tumblr.com/v2/blog/{username}.tumblr.com/posts/{mediatype}?api_key={api}&offset={limit}'.format(username = self.username, mediatype = self.mediatype, api = self.api, limit = int(self.limit)*20)
        return url

    def setPostUrl(self,posturl):
        self.posturl = posturl

    def getPostUrl(self):
        posturl = self.posturl
        postdetail = posturl.split('/')
        self.domain = postdetail[2]
        self.postid = postdetail[4]
        url = 'http://api.tumblr.com/v2/blog/{domain}/posts?id={postid}&api_key={api}'.format(domain = self.domain, postid = self.postid, api = self.api)
        return url