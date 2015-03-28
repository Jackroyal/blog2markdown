#blog2markdown

用来实现普通blog到markdown的搬家，自动将blog的html转换成HEXO可用的Markdown格式
暂时只做了CSDN

###UPDATE:
2015-03-28 将某些参数改为从配置文件中读取,加入更多异常判断
2014-12-15 优化标签解析功能,添加了标题,tag和category
2014-12-13 实现解析功能,基本完成解析功能
2014-12-10 实现CSDN的抓取，正在实现parse解析过程

###BUG
如果代码中有#和*会被转义成`\\#`和`\\*`
对table的支持不好
中文文件名可能会有问题

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
