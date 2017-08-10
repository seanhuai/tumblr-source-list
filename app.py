#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from packages._funcs import *

def selectfunc(args):
    if args[1] == 'username':
        username_list(args[2],args[3],args[4])
    elif args[1] == 'posturl':
        posturl_list(args[2])
    elif args[1] == 'tags':
        pass
    else:
        print('参数有误')

args = sys.argv
selectfunc(args)
