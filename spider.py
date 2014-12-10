#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: spider.py

from bs4 import BeautifulSoup as bs
import urllib2 , re , random , Queue
import sys
from ParseBlog import ParseBlog

# print sys.getdefaultencoding()
class CsdnSpider:
    """docstring for Spider"""
    def __init__(self, url):
        self.url = url #本次抓取的url
        self.crawl()   #抓取一次獲取本次的

        #初始化完成
    def crawl(self):#第一次抓取
        user_agents = [
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
                   ]
        req = urllib2.Request(self.url)
        agent = random.choice(user_agents)
        req.add_header('User-Agent',agent)
        req.add_header('Host','blog.csdn.net')
        req.add_header('Accept','*/*')
        req.add_header('Referer',self.url)
        req.add_header('GET',self.url)
        response = urllib2.urlopen(req)
        self.soup = bs(response.read())


class BlogSpider:
    """docstring for BlogSpider"""
    qu = Queue.Queue()
    totalNum = 0   #文章总数目
    runNum = 0     #程序执行次数
    flag = 0       #程序游标
    url_list = []   #url_list地址列表
    url_prefix = "http://blog.csdn.net"   #网址前缀
    def __init__(self, url):
        self.url = url
<<<<<<< HEAD
        # self.spider = CsdnSpider(self.url)
        # self.setNum()   #设定循环次数和总文章数目
        # self.getList()  #获取所有的博客地址和文章标题
        # print "列表抓取成功，总共获取%d篇文章" % BlogSpider.totalNum
        BlogSpider.url_list = [('建立HBase的集群和HDInsight在Hadoop中使用Hive来查询它们' , 'http://blog.csdn.net/yangzhenping/article/details/41079223')]
=======
        self.spider = CsdnSpider(self.url)
        self.setNum()   #设定循环次数和总文章数目
        self.getList()  #获取所有的博客地址和文章标题
        print "列表抓取成功，总共获取%d篇文章" % BlogSpider.totalNum
>>>>>>> 3098b0aebda7d0e530bde939a8b9f83d359c9d7a
        self.parseBlog()


    def setNum(self):
        str_total = self.spider.soup.find('div', class_="pagelist").find('span').get_text()
        pattern = re.compile('^\s+([\d]+)[\D]+?([\d]+)[\D]+')
        match = pattern.findall(str_total)  #match = [(u'370', u'8')]
<<<<<<< HEAD
        # BlogSpider.totalNum = 1
        # BlogSpider.runNum = 1
=======
>>>>>>> 3098b0aebda7d0e530bde939a8b9f83d359c9d7a
        BlogSpider.totalNum = int(match[0][0])
        BlogSpider.runNum = int(match[0][1])

    def getList(self):
        if BlogSpider.runNum != 0:
            self.parseUrlList()
        if BlogSpider.runNum > 1:
            for x in xrange(2,BlogSpider.runNum+1):
                print "http://blog.csdn.net/yangzhenping/article/list/" + str(x) +"?viewmode=contents"
                print len(BlogSpider.url_list)
                #此处添加?viewmode=contents可以使每页读取更多的列表，每页50条，不使用这个，每页只能读取20条
                self.spider = CsdnSpider("http://blog.csdn.net/yangzhenping/article/list/" + str(x) +"?viewmode=contents")
                self.parseUrlList()
            print "now x is %d" % x
            print len(BlogSpider.url_list)


        elif BlogSpider.runNum == 0:
            return
    def parseUrlList(self):
        listarr = self.spider.soup.find('div', class_="list_item_new").find_all('span',class_="link_title")
        print "list arr is %d" % len(listarr)
        for ite in listarr:
            BlogSpider.url_list.append((ite.find('a').get_text().strip(), BlogSpider.url_prefix+ite.find('a').get('href')))

    def parseBlog(self):
        if len(BlogSpider.url_list) > 0:
            for x in BlogSpider.url_list:
                print BlogSpider.url_prefix + x[1]
                self.spider = CsdnSpider(x[1])
                print self.spider.soup.title
                self.parse = ParseBlog(self.spider.soup)
        else:
            print "博客列表为空，可是列表抓取失败或者新博客无内容"


    def hasNext(self):
        pass








# print agent
# soup = bs(response.read())

# (soup.find('div',class_="list_item_new")).find_all('a', title=False, target=False)

# soup.find_all('a', text=re.compile(U"下一页"))
# #content = urllib2.urlopen('http://blog.csdn.net/yangzhenping?viewmode=contents').read()
# #print content

# time.sleep(10)
# print soup.find_all('a')[10].get_text()

if __name__ == '__main__':
    url = "http://blog.csdn.net/yangzhenping?viewmode=contents"
    blog = BlogSpider(url)
    #print blog.url_list
    #print BlogSpider.url_list
    #print blog.soup.title
