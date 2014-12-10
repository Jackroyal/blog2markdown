from bs4 import BeautifulSoup as bs
import urllib2, re, random, Queue


url_list = []
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
# url = 'http://blog.csdn.net/yangzhenping/article/list/2?viewmode=contents'
url = 'http://blog.csdn.net/yangzhenping/article/details/41079223'
# url = 'http://blog.csdn.net/yangzhenping/article/details/41744531'
req = urllib2.Request(url)
# agent = random.choice(user_agents)
agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2236.0 Safari/537.36'
req.add_header('User-Agent',agent)
req.add_header('Host','blog.csdn.net')
req.add_header('Accept','*/*')
req.add_header('Referer',url)
req.add_header('GET',url)
response = urllib2.urlopen(req)
soup = bs(response.read())
bb = soup.find('div', class_="article_content")

print re.match('<p>\s*</p>',(str(bb.p)).decode("utf-8"))
<p> </p>
nodeList = []
def parseNode(content):
    try:
        print content
        print len(content.contents)
    except:
        if content.parent.contents[0] != bb:
            nodeList.insert(0,content.parent)
    else:
        for x in content.children:
            parseNode(x)

f = file('nodelist.txt', 'w')
f.write(''.join([(lambda s : s +'\n')(unicode(x)) for x in nodeList]))
f.close()
# listarr = soup.find('div', class_="list_item_new").find_all('span',class_="link_title")
# for ite in listarr:
#     url_list.append((ite.find('a').get_text(),ite.find('a').get('href')))


# print len(listarr)
