#coding=utf-8

import urllib
import re
import pprint

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg= r'src="(images/content/.+?\.jpg)" '
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    t=0
    urlx='http://www.bift.edu.cn/'
    
    while t<len(imglist):
        imglist[t]=imglist[t].replace('../..','http://www.bift.edu.cn')
        imglist[t]=imglist[t][:0]+urlx+imglist[t][0:]
        t=t+1
    x=3

    for imgxx in imglist:
        urllib.urlretrieve(imgxx,'%x.jpg' %x)
        x=x+1
    return imglist
 

#this url of photo is :
#src="http://imgsrc.baidu.com/forum/w%3d580/sign=d/kfad;osf.jpg" pic_ext
#the method is   r'src="(.+?\.jpg)" pic_ext'

#the url of photo is:
#http://www.bift.edu.cn/images/content/2014-12/20141224092201291409.png
#the method is   r'src="(.+?\.png)" 

html=getHtml("http://www.bift.edu.cn")

pprint.pprint(getImg(html))
