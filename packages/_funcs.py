# -*- coding: utf-8 -*-

from packages._proxy import *
from packages._url import *
from packages._Base import *
from packages._mode import *
from packages._tags import *
from packages._profiles import *


def username_list(username,mediatype,limit,apinum = 0):
    u = Url()
    u.setUserName(username)
    u.setMediaType(mediatype)
    u.setAPI(api[apinum])
    resg = []
    for limit in range(int(limit)):
        u.setLimit(limit)
        p = Proxy(hostname,port,u.getReqUrl())
        un = Username([username,mediatype,p.getResult()])
        un.getSource(u.limit)
        resg.extend(un.res)
    un.checkAdult(resg)

def posturl_list(url,apinum = 0):
    u = Url()
    u.setAPI(api[apinum])    
    u.setPostUrl(url)
    p = Proxy(hostname,port,u.getPostUrl())
    pu = Posturl([p.getResult(),u.postid])
    res = []
    pu.getSource()
    pu.checkAdult(pu.res)
    