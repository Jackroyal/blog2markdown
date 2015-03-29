#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ParseBlog.py

from bs4 import BeautifulSoup as bs
from bs4 import UnicodeDammit
import re,os
from bs4 import NavigableString

class ParseBlog:
    """docstring for ParseBlog"""
    def __init__(self, soup):
        self.nodeList = []
        self.soup = soup
        self.nobr = True
        self.title = self.setTitle()
        self.time = self.setTime()
        self.category = self.setCategory()
        self.tag = self.setTag()
        self.content = self.setContent()
        self.path = 'output'
        self.mkdir(self.path)
        self.save2md()

    def setTitle(self):
        return re.sub('[ 　]','_',(self.soup.find('span', class_="link_title").get_text()).strip())
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
    def setHead(self):
        head = ''
        if self.title:
            head += '''title: '%s'\n''' % self.title
        else:
            head += '''title: '%s'\n''' % '无题'
        if self.time:
            head += '''date: %s\n''' % self.time
        if self.tag:
            head += '''tags:\n- %s\n''' % '\n- '.join(self.tag)
        if self.category:
            head += '''categories:\n- %s\n''' % '\n- '.join(self.category)
        head +='---'
        return head
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
                h_text += item.text.strip() + '\n'#加上原来h1的内容
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
                if item.attrs['href'] or item.text:
                    item.replace_with(a_text)
                else:
                    item.unwrap()
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
                    p_text = '<br/>'
                self.comm(item, p_text)
            #<br>
            if item.name.lower() == 'br':
                if self.nobr == False:
                    br_text = '<br/>'
                else:
                    br_text = '\n'
                item.replace_with(br_text)
            #<span
            if item.name.lower() == 'span':
                span_text = ''
                self.comm(item, span_text)
            #<em or <strong
            if item.name.lower() == 'em' or item.name.lower() == 'strong':
                ss = (lambda s : s*(int(['em', 'strong'].index(item.name.lower()))+1))('_')
                strong_text = ss + '%s' + ss
                try:
                    item.replace_with(strong_text % (item.decode_contents()).encode('utf-8'))
                except Exception, e:
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
            #<div
            if item.name.lower() == "div":
                self.parseNode(item)
                item.unwrap()

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

    def unescape_html(self, tt1):
        # while a = re.search('&[amp;]+',tt1) or b = re.search('&gt;',tt1) or c = re.search('&lt;',tt1) or d = re.search('(?<![\\\])\*',tt1):
        while re.search('&[amp;]+',tt1) or re.search('&gt;',tt1) or re.search('&lt;',tt1) or re.search('(?<![\\\])\*',tt1):
            a = re.search('&[amp;]+',tt1)
            b = re.search('&gt;',tt1)
            c = re.search('&lt;',tt1)
            d = re.search('(?<![\\\])\*',tt1)
            if a:
                tt1 = re.sub('&[amp;]+','&',tt1)
            if b:
                tt1 = re.sub('&gt;','>',tt1)
            if c:
                tt1 = re.sub('&lt;','<',tt1)
            if d:
                tt1 = re.sub('(?<![\\\])\*','\*',tt1)
        return tt1

    def mkdir(self, path="output"):
        if os.path.exists(path):
            #如果目录存在,那就什么也不做
            pass
        else:
            try:
                os.makedirs(path)
            except OSError, why:
                print "目录创建Faild: %s " % str(why)
                exit()

    def validateTitle(self, title):
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # 在win中文件名不允许出现'/\:*?"<>|'
        new_title = re.sub(rstr, "", title)
        return new_title

    def save2md(self):
        head = self.setHead()
        filename =  self.validateTitle(self.title) + '.md'
        f = open(self.path + os.path.sep  + filename, 'w+')

        tt = self.soup.find('div', class_="article_content").decode_contents()
        tt = self.unescape_html(tt)
        f.write(head.encode('utf-8') + tt.encode('utf-8'))
        f.close()
        print '%s    转换完毕' % (self.title).encode('utf-8')
