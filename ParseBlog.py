#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ParseBlog.py

from bs4 import BeautifulSoup as bs
import re

class ParseBlog:
    """docstring for ParseBlog"""
    def __init__(self, soup):
        print type(soup)
        self.nodeList = []
        self.soup = soup
        print type(self.soup)
        print (self.soup.find('span', class_="link_categories"))
        self.title = self.setTitle()
        self.time = self.setTime()
        self.category = self.setCategory()
        self.tag = self.setTag()
        self.content = self.setContent()
        self.save2md()

    def setTitle(self):
        return (self.soup.find('span', class_="link_title").get_text()).strip()
    def setTime(self):
        return (self.soup.find('span', class_="link_postdate").get_text()).strip()
    def setCategory(self):
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
        contentTag = content.find_all()  #获取所有article_content里面的子标签
        print 'from setContent'
        self.parseNode(content)
        f = file('contentTag.txt', 'w')
        f.write(str(contentTag) + "\nlen %d" % len(contentTag) + '\n%s' % contentTag[0])
        f.close()

        return content
    def parseNode(self, content):
        try:
            print len(content.contents)
        except Exception, e:
            print e
        else :
            for x in content.children:
                print 'from parseNode'
                self.parseHTML(x)

    def parseHTML(self,contentTag):
        for item in contentTag:
            try:
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
                    try:
                        if len(item.contents):
                            self.parseNode(item)
                            p_text += item.decode_contents()
                            item.replace_with(p_text)
                            item.unwrap()
                    except:
                        p_text += item.get_text()
                        item.replace_with(p_text)
                #<br>
                if item.name.lower() == 'br':
                    br_text = '\n'
                    item.replace_with(br_text)
                #<span
                if item.name.lower() == 'span':
                    span_text = ''
                    #span_text = '\n'
                    try:
                        if len(item.contents):
                            # span_text += item.decode_contents()
                            self.parseNode(item)
                            item.unwrap()
                    except:
                        span_text += item.get_text()
                    else:
                        item.replace_with(span_text)

                # if re.match('<span\s*>[\W\D]*</span>', str(item)):
                #     span_text += ''
                # # elif re.match('<span[\s\S]*?>.*?[<\s*\w{1,8}]+.*?</span>', str(item)) == None:
                # #     span_text += item.text + '\n'
                # else:
                #     span_text += item.text
                #     # span_text += str(item) + '\n'
                #item.replace_with(span_text)

            except Exception, e:
                #print e
                print type(e)


    def save2md(self):
        f = file('aaaaaaaaa.md', 'w')
        f.write(str(self.content))
        f.close()
        print 'save complite---------------------------------------'
