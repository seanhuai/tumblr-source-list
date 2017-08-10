from packages._proxy import *
from packages._url import *
from packages._username import *
from packages._posturl import *
from packages._tags import *
from packages._profiles import *

apinum = 0

def username_list(username,mediatype,limit):
    u = Url()
    u.setAPI(api[apinum])
    u.setUserName(username)
    u.setMediaType(mediatype)
    u.setLimit(limit)
    p = Proxy(hostname,port,u.getReqUrl())
    Username(username,mediatype,p.getResult()) 

def posturl_list(url):
    u = Url()
    u.setAPI(api[apinum])    
    u.setPostUrl(url)
    p = Proxy(hostname,port,u.getPostUrl())
    Posturl(p.getResult())
    