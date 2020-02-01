# -*- coding: utf-8 -*-
# @Author: mzmmohideen
# @Date:   2019-12-11 09:53:49
# @Last Modified by:   mzmmohideen
# @Last Modified time: 2019-12-11 09:54:12

import os

def list(path):
   f = os.listdir(path)
   for i in f:
     if os.path.isdir(i):
        list(i)
     print(i)

list('/home/mohideen/Desktop')