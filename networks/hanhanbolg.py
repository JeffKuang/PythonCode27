#coding:utf-8
#!/usr/bin/env python
import urllib2
import re
from __builtin__ import isinstance

#韩寒博客首页地址
url = 'http://blog.sina.com.cn/twocold'
#韩寒博客目录第一页
url1 = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'

def getURLList(str):
    return 

def getCatalog(str):
    m = urllib2.urlopen(str).read()
    pattern = r'<a href=".+">*?</a>'
    regex = re.compile(pattern)
    res = re.findall(regex, m)
    print res
    return res
    
def getAllURLs(url):
    urls = []
    cnt = 0
    

getCatalog(url)