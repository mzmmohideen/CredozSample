#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: mzmmohideen
# @Date:   2020-01-12 16:35:20
# @Last Modified by:   mzmmohideen
# @Last Modified time: 2020-01-13 09:42:59
# import string


def sum():
	print(1 + 2)


def sub():
	print(10 + 20)
	return 12

print('module name', __name__)
# if __name__ == "__main__":
print(sub())
print(sum())


# # del map
# # from dec_01_map import map, output, fact, toupper, a
# import dec_01_map
# # import sys


# print(dir(dec_01_map))
# # print('output', map(toupper, 'credo'))

# print(''.join(map(dec_01_map.toupper, 'credo@system')))
