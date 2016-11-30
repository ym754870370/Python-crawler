#coding=utf-8
import urllib #Urllib 模块提供了读取web页面数据的接口
import re

def getHtml(url):
    page = urllib.urlopen(url) #用于打开一个URL地址。
    html = page.read() #用于读取URL上的数据
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext' #筛选图片
    imgre = re.compile(reg) #把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html) #读取html 中包含 imgre（正则表达式）的数据
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x) #将远程数据下载到本地
        x+=1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print getImg(html)