#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ParseBlog.py

from bs4 import BeautifulSoup as bs

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

    def setTitle(self):
        return (self.soup.find('span', class_="link_title").get_text()).strip()
    def setTime(self):
        return (self.soup.find('span', class_="link_postdate").get_text()).strip()
    def setCategory(self):
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

