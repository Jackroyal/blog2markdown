#blog2markdown

用来实现普通blog到markdown的搬家，自动将blog的html转换成HEXO可用的Markdown格式
暂时只做了CSDN

###UPDATE:
2015-03-29 添加了打包成exe的程序,修复cmd下乱码,win和ubuntu完美运行
2015-03-29 连夜修复了在win下乱码的问题,删除了冗余代码
2015-03-28 将某些参数改为从配置文件中读取,加入更多异常判断
2014-12-15 优化标签解析功能,添加了标题,tag和category
2014-12-13 实现解析功能,基本完成解析功能
2014-12-10 实现CSDN的抓取，正在实现parse解析过程

###BUG
如果代码中有#和\*会被转义成`\#`和`\*`
对table的支持不好
中文文件名可能会有问题

###依赖库
爬虫使用了`beautifulsoup  4.3.2`
[点我点我](http://www.crummy.com/software/BeautifulSoup/)
你必须安装这个才可以正常使用

###Usage:

#### 首先,编辑配置文件`spider.conf`
格式如下:
```
[blog]
#此处url不需要单引号或者双引号,不然类型识别错误
url=http://blog.csdn.net/jackroyal
[setting]
wait_time=5
```
这里的url地址注意不要加引号,下面的wait_time是指两次抓取的间隔时间,这是为了安全起见,如果高频访问,可能会被封,我设置的5秒,你可以根据自己需要去设置
####  执行
在linux下,首先要给予执行权限
```
chmod a+x spider.py ParseBlog.py
python spider.py
```
然后就可以了,输出文件在output文件夹

在win下,经过修复也可以正常运行了,在idle(在win中你安装了python2.7的话就会有这个编辑器)中是可以完全正常的显示中文,~~在系统自带的cmd里中文显示会有问题,因为cmd中的编码默认是GBK,我程序基本都是utf-8,如果要在cmd显示正常,显示的代码都要加个str.encode('utf-8')才行.
不过抓取是没有问题的,此处就不纠结了哈,能用就好~~
```
#在win下,没有权限的问题,直接执行就好了
python spider.py
```

#win下打包成exe
打包好的程序放在了dist目录下
修改spider.conf文件,执行spider.exe就可以
