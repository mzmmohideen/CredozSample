# -*- coding: utf-8 -*-
# @Author: mzmmohideen
# @Date:   2020-01-12 14:49:48
# @Last Modified by:   mzmmohideen
# @Last Modified time: 2020-01-12 15:02:50
import os

c = os.getcwd()
print(c)

print(os.path.basename(c))
print(os.path.dirname('home/sample/123'))
print('abspath', os.path.abspath('sam/hello'))
print('realpath', os.path.realpath('sam/hello'))
print('relpath', os.path.relpath('sam/hello'))
print(os.path.sep)
print(os.path.join('/home/sample', 'credo.txt'))
print(os.path.splitext('/home/sample/credo.txt'))
print(os.path.isdir('oct_06_os.py'))
print(os.path.isfile('oct_06_os.py'))