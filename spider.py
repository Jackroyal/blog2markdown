#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# Filename: spider.py

from bs4 import BeautifulSoup as bs
import urllib2, re, random, Queue
import sys

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
	totalNum = 0   #文章总次数
	runNum = 0  #程序执行次数
	flag = 0   #程序游标

	def __init__(self, url):
		self.url = url
		self.spider = CsdnSpider(self.url)
		self.setNum()#设定循环次数和总文章数目


	def setNum(self):
		str_total = self.spider.soup.find('div', class_="pagelist").find('span').get_text()
		pattern = re.compile('^\s+([\d]+)[\D]+?([\d]+)[\D]+')
		match = pattern.findall(str_total)  #match = [(u'370', u'8')]
		BlogSpider.totalNum = int(match[0][0])
		BlogSpider.runNum = int(atch[0][1])

	def getList(self):

		if BlogSpider.runNum == 1:


		

	


	def hasNext(self):
		
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
	#print blog.soup.title