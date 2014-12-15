title: HDInsight-Hadoop实战（一）网站日志分析
date: 2014-12-15 18:03
tags:
- 
categories:
- Hive
- Hadoop
- 大数据
- 云计算
- HDInsight
---

#HDInsight-Hadoop实战（一）网站日志分析
 
##简介 

在此示例中，你将使用分析网站日志文件的 HDInsight 查询来深入了解客户使用网站的方式。借助此分析，你可查看外部网站一天内对该网站的访问频率以及用户体验的网站错误总结。 
在此教程中，你将学习如何使用 HDInsight： <ul type="disc"><li>连接到包含网站日志文件的 Azure Storage Blob </li><li>创建配置单元表以查询这些日志 </li><li>创建配置单元查询以分析数据 </li><li>使用 Microsoft Excel 连接到 HDInsight（使用 ODBC 连接）以检索已分析的数据 </li></ul>
##先决条件 

已使用群集配置你完成脚本和查询所需的所有内容。要将已分析的数据导出到 Microsoft Excel，你必须满足以下要求： <ul type="disc"><li>必须安装了 <strong>Microsoft Excel 2010</strong> 或 <strong>Microsoft     Excel 2013</strong>。 </li><li>你必须具有 <a href="http://www.microsoft.com/en-us/download/details.aspx?id=40886" target="_blank"><span style="color:blue;">Microsoft </span><span style="color:blue;">配置单元</span><span style="color:blue;"> ODBC </span><span style="color:blue;">驱动程序</span></a>才能将数据从配置单元导入 Excel 中。基于 <strong>Microsoft     Excel</strong> 的版本选择 32 位或 64 位版本。 </li></ul>
##已加载到 Windows Azure 存储 Blob 的网站日志数据 
以下是此示例使用的网站日志数据位置。你可从此页顶部的**文件浏览器**选项卡访问此数据。也可以在 **[default storage account]/[defaultcontainer]/HdiSamples/WebsiteLogSampleData/SampleLog** 路径下访问此示例的数据。  网站日志数据 wasb://yzphadoop01@byshdinsight.blob.core.chinacloudapi.cn/HdiSamples/WebsiteLogSampleData/SampleLog/
##正在创建配置单元表以查询网站日志数据 

以下配置单元语句创建了一个外部表，允许配置单元查询存储在 Azure Blob 存储中的数据。外部表以初始文件格式保留数据，同时允许配置单元针对文件内的数据执行查询。 配置单元语句通过描述文件内的字段、字段间的界定符以及  Azure Blob 存储中文件的位置创建了名为**网络日志**的新表。在此教程的**创建配置单元查询以分析数据**章节，你将针对存储在此表中的数据执行查询。 CreateExternal Table weblogs
DROP TABLE IFEXISTS weblogs; 
 
--create tableweblogs on space-delimited website log data
CREATE EXTERNALTABLE IF NOT EXISTS weblogs(s_date date, s_time string, s_sitename string,cs_method string, cs_uristem string, 
cs_uriquerystring, s_port int, cs_username string, c_ip string, cs_useragent string, 
cs_cookiestring, cs_referer string, cs_host string, sc_status int, sc_substatus int,
sc_win32statusint, sc_bytes int, cs_bytes int, s_timetaken int ) 
ROW FORMATDELIMITED FIELDS TERMINATED BY ' '
STORED ASTEXTFILE LOCATION'wasb://yzphadoop01@byshdinsight.blob.core.chinacloudapi.cn/HdiSamples/WebsiteLogSampleData/SampleLog/'
TBLPROPERTIES('skip.header.line.count'='2'); 
##创建配置单元查询以分析数据 
以下配置单元查询基于**网络日志**表上运行的查询创建了两个新表。新表名为 **clienterrors** 和 **refersperday**。 **clienterrors** 的查询从介于 400 到 500 之间的 HTTP 状态代码的网络日志表中提取数据，并且按遭遇这些错误的用户以及错误代码类型对其进行分组。状态代码的范围介于 400 到 500 之间，通过网络日志表中的 &amp;lt;em&amp;gt;sc_status&amp;lt;/em&amp;gt; 列表示，对应访问网站时客户端遭遇的错误。然后，提取的数据按每个错误代码的发生次数进行排序并写入 **clienterrors** 表。 **refersperday** 的查询从引用此网站的所有外部网站的网络日志表中提取数据。外部网站信息从网络日志表的 **cs_referer** 列中提取。为了确保引用链接不遭遇错误，表仅显示返回 200 到 300 之间的 HTTP 状态代码的页面数据。然后，提取的数据将写入 **refersperday** 表。 DROP TABLE IFEXISTS ClientErrors;  --create tableClientErrors for storing errors users experienced and their frequenciesCREATE EXTERNALTABLE ClientErrors(sc_status int, cs_referer string, cs_page string, cnt int)ROW FORMATDELIMITED FIELDS TERMINATED BY ','; --populate tableClientErrors with data from table weblogsINSERT OVERWRITETABLE ClientErrors SELECT sc_status,cs_referer,                                 concat(cs_uristem,'?',regexp_replace(cs_uriquery,'X-ARR-LOG-ID=[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',''))cs_page,                                count(distinctc_ip) as cnt FROM weblogs WHERE sc_status&amp;amp;gt;=400 and sc_status &amp;amp;lt; 500GROUP BYsc_status, cs_referer, concat(cs_uristem,'?',regexp_replace(cs_uriquery,'X-ARR-LOG-ID=[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',''))ORDER BY cnt;-------------------------------------------------------------------------------------------DROP TABLE IFEXISTS RefersPerDay; --create tableRefersPerDay for storing references from external websitesCREATE EXTERNALTABLE IF NOT EXISTS RefersPerDay(year int, month int, day int, cs_refererstring, cnt int)ROW FORMATDELIMITED FIELDS TERMINATED BY ','; --populate tableRefersPerDay with data from the weblogs tableINSERT OVERWRITETABLE RefersPerDaySELECTyear(s_date), month(s_date), day(s_date), cs_referer, count(distinct c_ip) ascntFROM weblogsWHERE sc_status&amp;amp;gt;=200 and sc_status &amp;amp;lt;300GROUP BY s_date,cs_refererORDER BY cntdesc;------------------------------------------------------------------------------------------- 
##正在执行查询 
单击**提交**以运行先前章节中显示的查询。查询执行以下任务： <ol start="1" type="a"><li>从 HDInsight 群集关联的 Azure     Blob 存储中的原始网站日志数据创建<strong>网络日志</strong>表。 </li><li>创建并填充先前章节中描述的 <strong>clienterrors</strong> 和 <strong>refersperday</strong> 表。 </li></ol>运行查询时，你可单击**查看详细信息**来获取有关后台运行任务的更多信息。在页底所有作业都处于**已完成**状态后，继续执行 **将数据加载到 Excel**。 
DROP TABLE IFEXISTS weblogs; 
 
--create tableweblogs on space-delimited website log data
CREATE EXTERNALTABLE IF NOT EXISTS weblogs(s_date date, s_time string, s_sitename string,cs_method string, cs_uristem string, 
                                    cs_uriquerystring, s_port int, cs_username string, c_ip string, cs_useragent string, 
                                    cs_cookiestring, cs_referer string, cs_host string, sc_status int, sc_substatus int,
                                    sc_win32statusint, sc_bytes int, cs_bytes int, s_timetaken int ) 
ROW FORMATDELIMITED FIELDS TERMINATED BY ' '
STORED ASTEXTFILE LOCATION 'wasb://yzphadoop01@byshdinsight.blob.core.chinacloudapi.cn/HdiSamples/WebsiteLogSampleData/SampleLog/'
TBLPROPERTIES('skip.header.line.count'='2');
 
DROP TABLE IFEXISTS ClientErrors; 
 
--create tableClientErrors for storing errors users experienced and their frequencies
CREATE EXTERNALTABLE ClientErrors(sc_status int, cs_referer string, cs_page string, cnt int)
ROW FORMATDELIMITED FIELDS TERMINATED BY ',';
 
--populatetable ClientErrors with data from table weblogs
INSERTOVERWRITE TABLE ClientErrors 
SELECTsc_status, cs_referer, 
                        concat(cs_uristem,'?',regexp_replace(cs_uriquery,'X-ARR-LOG-ID=[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',''))cs_page,
                        count(distinct c_ip) ascnt 
FROM weblogs 
WHERE sc_status&gt;=400 and sc_status &lt; 500
GROUP BYsc_status, cs_referer, concat(cs_uristem,'?', regexp_replace(cs_uriquery,'X-ARR-LOG-ID=[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',''))
ORDER BY cnt;
 
DROP TABLE IFEXISTS RefersPerDay;
 
--create tableRefersPerDay for storing references from external websites
CREATE EXTERNALTABLE IF NOT EXISTS RefersPerDay(year int, month int, day int, cs_refererstring, cnt int)
ROW FORMATDELIMITED FIELDS TERMINATED BY ',';
 
--populatetable RefersPerDay with data from the weblogs table
INSERTOVERWRITE TABLE RefersPerDay
SELECTyear(s_date), month(s_date), day(s_date), cs_referer, count(distinct c_ip) ascnt
FROM weblogs
WHERE sc_status&gt;=200 and sc_status &lt;300
GROUP BYs_date, cs_referer
ORDER BY cntdesc;
 
&lt;input type="submit" value="提交"/&gt;
作业会话<table border="0" cellpadding="0" width="100%"><thead><tr><td><p align="center"><strong>查询名称</strong></p></td><td><p align="center"><strong>日期</strong></p></td><td><p align="center"><strong>ID</strong></p></td><td><p align="center"><strong>操作</strong></p></td><td><p align="center"><strong>状态</strong></p></td></tr></thead><tbody><tr><td colspan="5" valign="top"><p>表中无可用数据</p></td></tr></tbody></table>
## 

##正在将数据加载到 Excel 
创建配置单元表之后，你可使用 [Microsoft 配置单元 ODBC 驱动器](http://www.microsoft.com/en-us/download/details.aspx?id=40886)将数据从配置单元导入到 Excel。安装驱动程序后，请使用以下步骤连接到表。 
1. 打开 Excel 并创建空白的工作表。 2. 从**数据**选项卡中，选择**来自其他源**，然后选择**来自 Microsoft 查询**。 
![](http://img.blog.csdn.net/20141215175957452?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
3. 提示**选择数据源**时，选择**示例 Microsoft 配置单元 DSN**。 
![](http://img.blog.csdn.net/20141215180016687?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
4. 在 **Microsoft 配置单元 ODBC 驱动器连接**对话框中，输入以下值，然后单击“确定”。 <ul type="disc"><li><strong>主机</strong> - HDInsight 群集的主机名。例如，mycluster.azurehdinsight.net </li><li><strong>用户名</strong> - HDInsight 群集的管理员名称 </li><li><strong>密码</strong> - 管理员密码 </li></ul>
所有其它字段均为默认值。 
![](http://img.blog.csdn.net/20141215180015031?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
5. 在查询向导中，选择 **refersperday** 表，然后选择 **&amp;amp;gt;** 按钮。 
![](http://img.blog.csdn.net/20141215180058043?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
6. 单击**下一步**继续查看向导，直到到达带有**完成**按钮的对话框。单击**完成**。 7. 出现**导入数据**对话框后，单击**确定**以接受默认值。完成查询后，数据将显示在 Excel 中。 
![](http://img.blog.csdn.net/20141215180132690?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

##摘要 
在本教程中，你了解了如何使用 Azure HDInsight 分析使用 Apache Hive 的网站日志数据。你浏览了一个流程，了解原始数据如何先上载到  Azure 存储空间 Blob 再加载到配置单元表以便执行查询。最后，你了解了如何将配置单元查询的结果导入到 Microsoft Excel。如果你具有本教程或其他示例方面的反馈，请使用上面的**帮助 + 反馈**链接。 
使用以下链接继续了解如何将配置单元和 Excel 与 HDInsight 一同使用。 <ul type="disc"><li><a href="http://azure.microsoft.com/en-us/documentation/articles/hdinsight-use-hive/" target="_blank"><span style="color:blue;">将配置单元和</span><span style="color:blue;"> HDInsight </span><span style="color:blue;">中</span><span style="color:blue;"> Hadoop </span><span style="color:blue;">一同使用</span></a> </li><li><a href="http://azure.microsoft.com/en-us/documentation/articles/hdinsight-analyze-twitter-data/" target="_blank"><span style="color:blue;">使用</span><span style="color:blue;"> HDInsight </span><span style="color:blue;">中</span><span style="color:blue;"> Hadoop </span><span style="color:blue;">分析</span><span style="color:blue;"> Twitter </span><span style="color:blue;">数据</span></a> </li><li><a href="http://azure.microsoft.com/en-us/documentation/articles/hdinsight-connect-excel-hive-odbc-driver/" target="_blank"><span style="color:blue;">使用</span><span style="color:blue;"> Microsoft </span><span style="color:blue;">配置单元</span><span style="color:blue;"> ODBC </span><span style="color:blue;">驱动程序将</span><span style="color:blue;"> Excel </span><span style="color:blue;">连接到</span><span style="color:blue;"> Hadoop</span></a> </li></ul> **转载请注明出处：**[http://blog.csdn.net/yangzhenping](http://blog.csdn.net/yangzhenping)**， 谢谢！**
