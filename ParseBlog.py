#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ParseBlog.py

from bs4 import BeautifulSoup as bs
<<<<<<< HEAD
import re
=======
>>>>>>> 3098b0aebda7d0e530bde939a8b9f83d359c9d7a

class ParseBlog:
    """docstring for ParseBlog"""
    def __init__(self, soup):
        print type(soup)
        self.soup = soup
        print type(self.soup)
        print (self.soup.find('span', class_="link_categories"))
        self.title = self.setTitle()
        self.time = self.setTime()
        self.category = self.setCategory()
        self.tag = self.setTag()
        self.content = self.setContent()
<<<<<<< HEAD
        self.save2md()
=======
>>>>>>> 3098b0aebda7d0e530bde939a8b9f83d359c9d7a

    def setTitle(self):
        return (self.soup.find('span', class_="link_title").get_text()).strip()
    def setTime(self):
        return (self.soup.find('span', class_="link_postdate").get_text()).strip()
    def setCategory(self):
<<<<<<< HEAD
        category = []
        try:
            categoryList = self.soup.find('span', class_="link_categories").find_all('a')
            for x in categoryList:
                category.append(x.get_text().strip())
        except:
            category = []
        return category
    def setTag(self):
        tag = []
        try:
            tagList = self.soup.find('div', class_="tag2box").find_all('a')
            for x in tagList:
                tag.append(x.get_text().strip())
        except:
            tag = []
        return tag
    def setContent(self):
        content = self.soup.find('div', class_="article_content")
        f = file('conten.txt', 'w')
        f.write(str(content))
        f.close()
        contentTag = content.find_all('a')  #获取所有article_content里面的子标签
        self.parseHTML(contentTag)
        contentTag = content.find_all('img')  #获取所有article_content里面的子标签
        self.parseHTML(contentTag)
        contentTag = content.find_all('p')  #获取所有article_content里面的子标签
        self.parseHTML(contentTag)
        contentTag = content.find_all('span')  #获取所有article_content里面的子标签
        self.parseHTML(contentTag)
        contentTag = content.find_all('pre')  #获取所有article_content里面的子标签
        self.parseHTML(contentTag)
        contentTag = content.find_all()  #获取所有article_content里面的子标签

        f = file('contentTag.txt', 'w')
        f.write(str(contentTag) + "\nlen %d" % len(contentTag) + '\n%s' % contentTag[0])
        f.close()

        return content

    def parseHTML(self,contentTag):
        for item in contentTag:
            #'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
            if item.name.lower() in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                h_text = '\n'
                #简单快速的完成#的复制，使用lambda表达式
                h_text += (lambda s : s*(int(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'].index(item.name))+1))('#')
                h_text += item.text #加上原来h1的内容
                item.replace_with(h_text)

            #<a
            if item.name.lower() == 'a':
                a_text = '\n'
                a_text += '['
                if item.string != None:
                    a_text += item.string
                a_text = a_text + '](' +item.attrs['href']
                if  item.attrs.get('title',None) != None:
                    a_text += '"' + item.attrs['title'] + '"'
                a_text += ')\n'
                item.replace_with(a_text)
            #<img
            if item.name.lower() == 'img':
                img_text = '\n'
                img_text += '!['
                temp_t = item.attrs.get('alt') or item.attrs.get('title')
                if temp_t:
                    img_text += temp_t + '](' + item.attrs['src'] + '"' + temp_t +'")'
                else:
                    img_text += '](' + item.attrs['src'] + ')\n'
                item.replace_with(img_text)
            #<pre
            if item.name.lower() == 'pre':
                #首先判断它是不是代码区域
                pre_text = '\n'
                if item.attrs.get('name',None) and item.attrs.get('name',None) == 'code':
                    pre_text += '```%s\n%s\n```\n' % (str(item.attrs['class'][0]), item.text)
                item.replace_with(pre_text)
            #<p
            if item.name.lower() == 'p':
                p_text = '\n'
                if re.match('<p\s*>[\W\D]*[<br/?>]*[\W\D]*</p>', str(item)):
                    p_text += ''
                elif re.match('<p[\s\S]*?>.*?[<\w{1,8}]+.*?</p>', str(item)) == None:
                    p_text += str(item) + '\n'
                item.replace_with(p_text)
            #<span
            if item.name.lower() == 'span':
                span_text = '\n'
                if re.match('<span\s*>[\W\D]*</span>', str(item)):
                    span_text += ''
                # elif re.match('<span[\s\S]*?>.*?[<\s*\w{1,8}]+.*?</span>', str(item)) == None:
                #     span_text += item.text + '\n'
                else:
                    span_text += item.text
                    # span_text += str(item) + '\n'
                item.replace_with(span_text)

    def save2md(self):
        f = file('aaaaaaaaa.md', 'w')
        f.write(str(self.content))
        f.close()
        print 'save complite---------------------------------------'
=======
        try:
            category = (self.soup.find('span', class_="link_categories").get_text()).strip()
        except:
            category = ''
        return category
    def setTag(self):
        try:
            tag = (self.soup.find('div', class_="tag2box").get_text()).strip()
        except:
            tag = ''
        return tag
    def setContent(self):
        return (self.soup.find('div', class_="article_content").get_text()).strip()

>>>>>>> 3098b0aebda7d0e530bde939a8b9f83d359c9d7a
