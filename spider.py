#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: spider.py

from bs4 import BeautifulSoup as bs
from bs4 import UnicodeDammit
import urllib2 , re , random , Queue
import sys,time
from ParseBlog import ParseBlog
import ConfigParser,string

# print sys.getdefaultencoding()
class CsdnSpider:
    """docstring for Spider"""
    def __init__(self, url):
        self.url = url #本次抓取的url
        self.crawl()   #抓取一次获取本次的url_list

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
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError:
            print 'url参数请不要加单引号或者双引号'
            exit()
        self.soup = bs((response.read()).decode('utf-8').encode('utf-8'), from_encoding='utf-8')



class BlogSpider:
    """docstring for BlogSpider"""
    qu = Queue.Queue()
    totalNum = 0   #文章总数目
    runNum = 0     #程序执行次数
    flag = 0       #程序游标
    url_list = []   #url_list地址列表
    url_prefix = "http://blog.csdn.net"   #网址前缀
    def __init__(self):
        self.onInit() #参数配置的初始化,从spider.conf中读取
        self.spider = CsdnSpider(self.url)
        self.setNum()   #设定循环次数和总文章数目
        self.getList()  #获取所有的博客地址和文章标题
        print "列表抓取成功，总共获取%d篇文章" % BlogSpider.totalNum
        self.parseBlog()

    def onInit(self):
            cf = ConfigParser.ConfigParser()
            cf.read('spider.conf')
            #此处如果配置文件不存在也不会报错,所以我们判断url能不能读出来,来判断文件存在与否或者配置是否正确
            try:
                self.url = str(cf.get('blog', 'url'))
                self.wait_time = cf.get('setting', 'wait_time')
            except NameError:
                print "你还没有配置你的配置文件,请按照如下示例重新配置spider.conf\r\n[blog]\r\nurl=\"http://blog.csdn.net/jackroyal\"\r\n[setting]\r\nwait_time=10\r\n"
                exit()

    def setNum(self):
        tt = self.spider.soup.find('div', class_="pagelist")
        if tt != None:
            str_total = tt.find('span').get_text()
            pattern = re.compile('^\s+([\d]+)[\D]+?([\d]+)[\D]+')
            match = pattern.findall(str_total)  #match = [(u'370', u'8')]
            BlogSpider.totalNum = int(match[0][0])
            BlogSpider.runNum = int(match[0][1])
        else:
            tt = self.spider.soup.find('div', id="article_list")
            BlogSpider.totalNum = len(tt.find_all('div', class_ = "article_title"))
            BlogSpider.runNum = 1

    def getList(self):
        if BlogSpider.runNum != 0:
            self.parseUrlList()
        if BlogSpider.runNum > 1:
            for x in xrange(2,BlogSpider.runNum+1):
                #此处添加?viewmode=contents可以使每页读取更多的列表，每页50条，不使用这个，每页只能读取20条
                self.spider = CsdnSpider(self.url + str(x) +"?viewmode=contents")
                self.parseUrlList()

        elif BlogSpider.runNum == 0:
            return
    def parseUrlList(self):
        listarr = self.spider.soup.find('div', class_="list_item_new").find_all('span',class_="link_title")
        for ite in listarr:
            BlogSpider.url_list.append((ite.find('a').get_text().strip(), BlogSpider.url_prefix+ite.find('a').get('href')))

    def parseBlog(self):
        if len(BlogSpider.url_list) > 0:
            for x in BlogSpider.url_list:
                print '正在抓取第%d篇 ' % (int(BlogSpider.url_list.index(x)) + 1),
                self.spider = CsdnSpider(x[1])
                self.parse = ParseBlog(self.spider.soup)

                wait_time = random.randint(1,int(self.wait_time))
                print '随机等待%d秒' % wait_time
                time.sleep(wait_time)
            else:
                print "全部%d篇文章抓取完成,有bug请去https://github.com/Jackroyal/blog2markdown提交" % self.totalNum
        else:
            print "博客列表为空，可是列表抓取失败或者新博客无内容"


if __name__ == '__main__':
    blog = BlogSpider()
