# -*- coding: utf-8 -*-

from urllib import request
import json

class Proxy():

    def __init__(self,hostname,port,requrl):
        self.hostname = hostname
        self.port = port
        self.url = requrl
        self.setProxy()

    def setProxy(self):
        proxy_handler = request.ProxyHandler({'http': 'http://{hostname}:{port}/'.format(hostname = self.hostname, port = self.port)})
        opener = request.build_opener(proxy_handler)
        try:
            connect = opener.open(self.url)
            r = connect.read().decode()
            res = json.loads(r)
        except BaseException as e:
            print(e)
        else:
            self.res = res

    def getResult(self):
        return self.res
