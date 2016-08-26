#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding:utf-8 -*-
'''
using command in terminal with python3 webgrab.py http://www.baidu.com to test
'''
import urllib.request
import sys
url=sys.argv[1]
response = urllib.request.urlopen(url)
html=response.readline();
print(html)

