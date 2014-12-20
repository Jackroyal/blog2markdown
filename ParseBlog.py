#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ParseBlog.py

from bs4 import BeautifulSoup as bs
import re, HTMLParser
from bs4 import NavigableString

class ParseBlog:
    """docstring for ParseBlog"""
    def __init__(self, soup):
        print type(soup)
        self.nodeList = []
        self.soup = soup
        self.nobr = True
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
        self.parseNode(content)

        return content
    def parseNode(self, content):
        try:
            if isinstance(content , NavigableString):
                pass
            else:
                for x in content.children:
                    if isinstance(x,NavigableString):
                        pass
                    else:
                        self.parseHTML(x)

        except Exception, e:
            print e

    def parseHTML(self,contentTag):
        # for item in contentTag:
        item = contentTag
        #如果是字符串比如u"\n"那么会直接去到except
        try:
            #'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
            if item.name.lower() in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                h_text = '\n'
                #简单快速的完成#的复制，使用lambda表达式
                h_text += (lambda s : s*(int(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'].index(item.name))+1))('#')
                h_text += item.text + '\n'#加上原来h1的内容
                item.replace_with(h_text)

            #<a
            if item.name.lower() == 'a':
                a_text = ''
                a_text += '['
                if item.string != None:
                    a_text += item.string
                else:
                    a_text += item.get_text()
                a_text = a_text + '](' +item.attrs['href']
                if  item.attrs.get('title',None) != None:
                    a_text += '"' + item.attrs['title'] + '"'
                a_text += ')'
                item.replace_with(a_text)
            #<img
            if item.name.lower() == 'img':
                img_text = ''
                img_text += '!['
                temp_t = item.attrs.get('alt') or item.attrs.get('title')
                if temp_t:
                    img_text += temp_t + '](' + item.attrs['src'] + '"' + temp_t +'")'
                else:
                    img_text += '](' + item.attrs['src'] + ')'
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
                if self.nobr == True:
                    p_text = '\n'
                else:
                    p_text = '<br>'
                self.comm(item, p_text)
            #<br>
            if item.name.lower() == 'br':
                if self.nobr == False:
                    br_text = '<br>'
                else:
                    br_text = '\n'
                item.replace_with(br_text)
            #<span
            if item.name.lower() == 'span':
                span_text = ''
                self.comm(item, span_text)
            #<strong or <em
            if item.name.lower() == 'strong' or item.name.lower() == 'em':
                ss = (lambda s : s*(int(['strong', 'em'].index(item.name.lower()))+1))('*')
                strong_text = ss + '%s' + ss
                try:
                    item.replace_with(strong_text % (item.decode_contents()).encode('utf-8'))
                except Exception, e:
                    print 'from strong'
                    print item.decode_contents()
                    print item
                    print type(e)

            #<ol or <ul
            if item.name.lower() == 'ol' or item.name.lower() == 'ul':
                self.nobr = False
                self.parseNode(item)
                self.nobr = True
                item.replace_with(item.decode_contents())

            #<li
            if item.name.lower() == "li":
                li_text = ''
                if item.parent.name.lower() == "ol":#<ol
                    li_text = '1. '

                if item.parent.name.lower() == "ul":
                    li_text = '+ '
                try:
                    if len(item.contents) == 1 and isinstance(item.contents[0], NavigableString):
                        li_text += item.decode_contents()
                        item.replace_with(li_text)
                    else:
                        self.parseNode(item)
                        item.replace_with('\n' + li_text + item.decode_contents())
                except Exception, e:
                    pass

        except Exception, e:
            print item
            print type(e)

    def comm(self, item, text):
        comm_text = text or ''
        try:
            if len(item.contents) == 1 and isinstance(item.contents[0], NavigableString):
                comm_text += item.decode_contents()
                item.replace_with(comm_text)
            else:
                self.parseNode(item)
                item.replace_with(item.decode_contents())
        except Exception, e:
            pass

    def save2md(self):
        head = '''title: '%s'\ndate: %s\ntags:\n- %s\ncategories:\n- %s\n---''' % (self.title, self.time, '\n- '.join(self.tag), '\n- '.join(self.category))
        f = file((self.title + '.md'), 'w')
        tt = self.soup.find('div', class_="article_content").decode_contents()
        h = HTMLParser.HTMLParser()
        f.write( h.unescape(h.unescape(h.unescape((head + (self.soup.find('div', class_="article_content").decode_contents()))))).encode('utf-8'))
        print type(tt)
        print type(str(self.soup.find('div', class_="article_content")))
        # f.write(str(self.soup.find('div', class_="article_content")))
        f.close()
        print 'save complite---------------------------------------'
