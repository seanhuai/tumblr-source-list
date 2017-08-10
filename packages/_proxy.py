from urllib import request
import json

class Proxy():

    def __init__(self,hostname,port,requrl):
        self.hostname = hostname
        self.port = port
        self.url = requrl
        self.setProxy()

    def setProxy(self):
        proxy_handler = request.ProxyHandler({'http': 'http://'+self.hostname+':'+self.port+'/'})
        opener = request.build_opener(proxy_handler)
        connect = opener.open(self.url)
        r = connect.read() 
        res = json.loads(r)
        self.res = res

    def getResult(self):
        return self.res