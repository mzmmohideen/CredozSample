# -*- coding: utf-8 -*-
# @Author: mzmmohideen
# @Date:   2019-12-14 14:39:48
# @Last Modified by:   mzmmohideen
# @Last Modified time: 2019-12-14 14:53:20
a = 10
b = 20
def sum1(*args):
	out = 0
	for i in args:
		out += i
	return out