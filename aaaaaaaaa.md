<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<script charset="utf-8" src="http://csdnimg.cn/pubfooter/js/tracking.js" type="text/javascript"></script>
<script type="text/javascript">
        var protocol = window.location.protocol;
        document.write('<script type="text/javascript" src="' + protocol + '//csdnimg.cn/pubfooter/js/repoAddr2.js?v=' + Math.random() + '"></' + 'script>');
    </script>
<script charset="utf-8" id="allmobilize" src="http://a.yunshipei.com/46aae4d1e2371e4aa769798941cef698/allmobilize.min.js"></script>
<meta content="no-siteapp" http-equiv="Cache-Control"/><link href="#" media="handheld" rel="alternate"/>
<title>建立HBase的集群和HDInsight在Hadoop中使用Hive来查询它们 - 每一天都有新的希望
        - 博客频道 - CSDN.NET</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="建立HBase的集群和HDInsight在Hadoop中使用Hive来查询它们在本教程中，您将学习如何创建和查询HDInsight使用HiveHadoop的HBase的表。下列步骤描述：•如何使用提供在Azure门户的HBase的集群。•如何启用和使用RDP访问HBase的外壳，并使用HBase的外壳创建HBase的示例表，添加行，然后列出表中的行。•如何创建一个Hive表映射到一个现有的HBase的表，使用HiveQL查询数据在HBase的表。•如何使用Microsoft HBase的REST客户端库.NET创建一个新的HBase的表，列出您帐户中的HBase的表，以及如何从表添加和检索行。" name="description"/>
<script src="http://static.blog.csdn.net/scripts/jquery.js" type="text/javascript"></script>
<script src="http://static.blog.csdn.net/scripts/ad.js?v=1.1" type="text/javascript"></script>
<!--new top-->
<link href="http://static.csdn.net/public/common/toolbar/css/index.css" rel="stylesheet"/> <!--new top-->
<link href="http://static.blog.csdn.net/skin/default/css/style.css?v=1.1" rel="Stylesheet" type="text/css"/>
<link href="/yangzhenping/rss/list" id="RSSLink" rel="alternate" title="RSS" type="application/rss+xml"/>
<link href="http://csdnimg.cn/public/favicon.ico" rel="shortcut icon"/>
<link href="http://static.blog.csdn.net/scripts/SyntaxHighlighter/styles/default.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<!--new top-->
<script fixed="true" id="toolbar-tpl-scriptId" prod="blog" skin="black" src="http://static.csdn.net/public/common/toolbar/js/html.js" type="text/javascript"></script>
<!--new top-->
<div id="container">
<div id="header">
<div class="header">
<div id="blog_title">
<h2>
<a href="http://blog.csdn.net/yangzhenping">每一天都有新的希望</a></h2>
<h3>雕像重生</h3>
<div class="clear">
</div>
</div>
<div class="clear">
</div>
</div>
</div>
<div id="navigator">
<div class="navigator_bg">
</div>
<div class="navigator">
<ul>
<li id="btnContents"><a href="http://blog.csdn.net/yangzhenping?viewmode=contents"><span onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_mulu'])">
<img src="http://static.blog.csdn.net/images/ico_list.gif"/>目录视图</span></a></li>
<li id="btnView"><a href="http://blog.csdn.net/yangzhenping?viewmode=list"><span onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_zhaiyao'])">
<img src="http://static.blog.csdn.net/images/ico_summary.gif"/>摘要视图</span></a></li>
<li id="btnRss"><a href="http://blog.csdn.net/yangzhenping/rss/list"><span onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_RSS'])">
<img src="http://static.blog.csdn.net/images/ico_rss.gif"/>订阅</span></a></li>
</ul>
</div>
</div>
<script type="text/javascript">
    var username = "yangzhenping";
    var _blogger = username;
    var blog_address = "http://blog.csdn.net/yangzhenping";
    var static_host = "http://static.blog.csdn.net";
    var currentUserName = "";  
</script>
<div id="body">
<div id="main">
<div class="main">
<div class="ad_class">
<div class="notice tracking-ad" data-mod="popu_3">
<a href="http://bbs.csdn.net/topics/390812950?page=5#post-398523062" target="_blank">
<font color="blue">博客专家福利
</font></a>
   

<a href="http://blog.csdn.net/csdnproduct/article/details/41806091">
<font color="red">C币兑换平台上线</font></a>

    

<a href="http://blog.csdn.net/blogdevteam/article/details/41079173">
<font color="blue">10月推荐文章汇总
</font></a>
    

<a href="http://blog.csdn.net/blogdevteam/article/details/41842837">
<font color="red">有奖征文--我亲历的京东发展史
</font></a>
    



</div> </div>
<link href="http://static.blog.csdn.net/css/comment1.css" rel="stylesheet" type="text/css"/>
<link href="http://static.blog.csdn.net/css/style1.css" rel="stylesheet" type="text/css"/>
<script language="JavaScript" src="http://download.csdn.net/js/jquery.cookie.js" type="text/javascript"></script>
<script src="http://csdnimg.cn/rabbit/search-service/main.js" type="text/javascript"></script>
<script type="text/ecmascript">
      window.quickReplyflag = true;
    </script>
<div class="details" id="article_details">
<div class="article_title">
<span class="ico ico_type_Translated"></span>
<h1>
<span class="link_title"><a href="/yangzhenping/article/details/41079223">
        建立HBase的集群和HDInsight在Hadoop中使用Hive来查询它们
        </a></span>
</h1>
</div>
<div class="article_manage">
<span class="link_categories">
        分类：
            <a href="/yangzhenping/article/category/2700209" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_fenlei']);">Hadoop</a>
<a href="/yangzhenping/article/category/2700207" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_fenlei']);">HDInsight</a>
<a href="/yangzhenping/article/category/2700315" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_fenlei']);">HBase</a>
<a href="/yangzhenping/article/category/2700217" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_fenlei']);">Hive</a>
</span>
<span class="link_postdate">2014-11-13 15:19</span>
<span class="link_view" title="阅读次数">462人阅读</span>
<span class="link_comments" title="评论次数"><a href="#comments" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_pinglun'])">评论</a>(0)</span>
<span class="link_collect"><a href="javascript:void(0);" onclick="javascript:_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_shoucang']);collectArticle('建立HBase的集群和HDInsight在Hadoop中使用Hive来查询它们','41079223');return false;" title="收藏">收藏</a></span>
<span class="link_report"><a href="#report" onclick="javascript:_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_jubao']);report(41079223,2);return false;" title="举报">举报</a></span>
</div>
<div class="tag2box"><a href="http://www.csdn.net/tag/hive" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_tag']);" target="_blank">hive</a><a href="http://www.csdn.net/tag/hbase" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_tag']);" target="_blank">hbase</a><a href="http://www.csdn.net/tag/yarn" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_tag']);" target="_blank">yarn</a><a href="http://www.csdn.net/tag/azure" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_tag']);" target="_blank">azure</a><a href="http://www.csdn.net/tag/%e5%a4%a7%e6%95%b0%e6%8d%ae" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_tag']);" target="_blank">大数据</a></div>

<p>建立HBase的集群和HDInsight在Hadoop中使用Hive来查询它们</p><span class="alt-edited"></span><p>
在本教程中，您将学习如何创建和查询HDInsight使用HiveHadoop的HBase的表。下列步骤描述：
•如何使用提供在Azure门户的HBase的集群。
•如何启用和使用RDP访问HBase的外壳，并使用HBase的外壳创建HBase的示例表，添加行，然后列出表中的行。
•如何创建一个Hive表映射到一个现有的HBase的表，使用HiveQL查询数据在HBase的表。
•如何使用Microsoft HBase的REST客户端库.NET创建一个新的HBase的表，列出您帐户中的HBase的表，以及如何从表添加和检索行。
</p><h2>什么是HBase的？</h2><p>
HBase的是一种低延迟的NoSQL数据库，让大数据的联机事务处理。 HBase的是提供一个管理的集群集成到Azure的环境。集群被配置为直接在Azure中的Blob存储，这提供了在性能/成本的选择低延迟和增加的弹性存储数据。这使客户能够建立一个大型数据集工作的互动式网站，构建存储传感器和遥测数据，从数以百万计的端点的服务，并分析这些数据与Hadoop作业。关于HBase的，它可以被用于方案的详细信息，请参阅
[](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-overview/)
<a href="http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-overview/" target="_blank">概述</a>。


<strong>注意：</strong>

HBase的（版本0.98.0）仅适用于在HDInsight与HDInsight3.1集群的使用（基于Apache Hadoop和YARN2.4.0）。对于版本信息，请查看
[有什么](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-component-versioning/)

[](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-component-versioning/)
</p><h2>先决条件：</h2><span></span><p>
开始之前本教程中，你必须具备以下条件：
•一个Azure订阅有关获取预订的详细信息，请参阅购买选项，会员优惠或免费试用。
•一个Azure存储帐户有关说明，请参阅如何创建存储帐户。
•与安装了Visual Studio2013的工作站。有关说明，请参阅安装Visual Studio。
•下载微软HBase的REST客户端库.NET。

估计时间来完成：30分钟</p><h2><span>在</span>本教程中的部分</h2><span></span><p>
•提供了Azure中门户网站的HBase的集群
•从HBase的外壳创建HBase的示例表
•使用Hive查询的HBase的表
•使用HBase的C＃API从表中创建一个HBase的表和检索数据
•摘要
•下一步是什么？</p><p> </p><h2><span>在Azure</span>门户提供的HBase的集群</h2><p><span></span>
本节将介绍如何使用提供在Azure门户的HBase的集群。
 

<strong>注意：</strong>

本文中的步骤创建使用基本配置设置HDInsight集群。对于其他群集配置设置，例如使用Azure中虚拟网络或metastore用于Hive和Oozie的信息，请参阅
[](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-provision-clusters/)

[群集](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-provision-clusters/)
。
 
为了提供一个HDInsight在Azure中门户网站集群
1。登录到
[Azure管理门户](https://manage.windowsazure.com/)
。

2。点击左侧HDInsight列出集群您的帐户，然后在左下角的+新图标的状态。</p><p>
![](http://img.blog.csdn.net/20141113145927328?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
</p><p>3.点击在从左侧和在下一列则HBase的选项的第二列的HDInsight图标。指定群集名称和簇大小，存储帐户的名称，并为新的HBase集群密码的值。</p><p>
![](http://img.blog.csdn.net/20141113150018826?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
</p><p>4.单击在较低的检查左侧的图标创建HBase的集群。

</p><h2>从HBase的外壳创建HBase的示例表</h2><span></span><p>
本节介绍如何启用和使用远程桌面协议（RDP）来访问HBase的外壳，然后用它来创建一个HBase的示例表，添加行，然后列出表中的行。

它假定您已经完成了第一部分概述的过程，所以已经成功地创建了一个HBase的集群。
</p><h3>启用RDP连接到HBase的集群</h3><span></span><p>
1.To使到HDInsight集群中的远程桌面连接，选择已创建的HBase的集群，然后单击配置选项卡。点击ENABLE在页面底部遥控按钮启用RDP连接到群集。
2.提供的配置远程桌面向导的凭据和到期日期，点击右下角的检查循环。 （这可能需要几分钟的操作来完成。）
3.To连接到HDInsight集群，点击连接按钮，在配置选项卡的底部。
</p><h3>打开HBase的壳</h3><span></span><p>
1.在你的RDP会话，点击位于桌面上的Hadoop的命令提示符快捷方式。

2.文件夹切换到HBase的主目录：</p><span></span><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_1_9083592">cd %HBASE_HOME%\bin</pre><p>
 </p><p>3。打开HBase的外壳：</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_2_8150429">hbase shell</pre><p>
 </p><p>创建一个示例表，添加数据和检索数据
1.创建示例表：
</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_3_6462739">create 'sampletable', 'cf1'</pre><p>

2.添加一行到示例表：
</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_4_7009522">put 'sampletable', 'row1', 'cf1:col1', 'value1'</pre><p>

3.列出在示例表中的行：</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_5_6368608">scan 'sampletable'</pre><p> </p><h2>使用Hive查询的HBase的表</h2><span></span><p>
现在你有一个HBase的集群配置和已经创建了一个表，你可以使用Hive查询。本节将创建一个Hive表映射到HBase的表，并使用该查询中的数据HBase的表。

要打开集群仪表板
1.登录到Azure管理门户。
2.从左侧窗格中点击HDINSIGHT。你会看到创建包括你刚才在上一节中创建的群列表。
3.单击您要运行的Hive作业的群集名称。
4.单击管理CLUSTER从页面底部的疏散星团仪表板。它不同的浏览器选项卡上打开一个网页。

5.输入Hadoop的用户帐户的用户名和密码。默认用户名为admin，密码是您在提供过程中输入的内容。仪表板是这样的：</p><p><img alt="" src="http://img.blog.csdn.net/20141113150501125?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center"/></p><h3><span>要运行</span>Hive查询</h3><p><span></span>
1。 要创建一个Hive表映射到HBase的表，在下面输入HiveQL脚本到Hive控制台窗口，然后点击提交按钮。请确保您已创建使用HBase的壳牌执行该语句之前此处引用的HBase中的sampletable。</p><span></span><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_6_1931901">CREATE EXTERNAL TABLE hbasesampletable(rowkey STRING, col1 STRING, col2 STRING)
STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES ('hbase.columns.mapping' = ':key,cf1:col1,cf1:col2')
TBLPROPERTIES ('hbase.table.name' = 'sampletable');</pre><p>
 </p><p>2.要执行一个Hive查询在数据中的HBase的，输入下面的HiveQL脚本到Hive控制台窗口，然后点击提交按钮。</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_7_9306119">SELECT count(*) FROM hbasesampletable;</pre><p>
 </p><p>3.要检索Hive查询的结果，请单击当作业完成执行作业会话窗口中查看详细信息链接。


<strong>注：</strong>HBase的外壳链接切换标签到HBase的外壳。
</p><h3>浏览输出文件</h3><span></span><p>
1.从群集面板，单击文件从顶部。
2.Click普顿 - 求职状态。
3.Click拥有的最后修改时间作业开始时间之前记录下来后，一点点的GUID数。记下此GUID的。你会需要它在下一节。
4，标准输出文件中有你需要在接下来的章节中的数据。您可以单击标准输出，如果你想下载的数据文件的副本。</p><h2><span>使用</span>HBase的REST客户端库.NET C＃API从表中创建一个HBase的表和检索数据</h2><p> </p><span></span><p>
微软HBase的REST客户端库.NET项目必须从GitHub的建成使用HBase的.NET SDK项目下载。下面的过程包括用于此任务的指示。
1. Downnload微软HBase的REST客户端库.NET，如果你还没有满足这一前提条件。

2.打开Marlin.sln在Visual Studio中（文件 - &gt;项目/解决方案... - &gt;打开），从它被下载到的位置。选择查看 - &gt;解决方案资源管理器中看到的“马林”的解决方案及其Microsoft.HBase.Client项目。构建马林项目通过在Solution Explorer中右击它并选择生成解决方案。

3.创建一个新的Visual C＃控制台应用程序。检索建（从...\ BIN\调试\ Microsoft.HBase.Client目录）所产生的Microsoft.HBase.Client.dll和protobuf.dll并将它们添加到您的C＃项目：在引用单击鼠标右键，选择添加引用...，浏览到两个组件，并将其上传。 protobuf网是一个.NET实现了谷歌的Protocol Buffers的二进制序列的用于数据通信。

4.添加以下using语句上的文件的顶部：
</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_8_7311627">using Microsoft.HBase.Client;
using org.apache.hadoop.hbase.rest.protobuf.generated;</pre><p>

5.使用群集凭据创建HBase的客户端的新实例和检索集群版本：
</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_9_6637694">// Create a new instance of an HBase client.
var creds = new ClusterCredentials(new Uri("https://myclustername.azurehdinsight.net"), "myusername", "mypassword");
var client = new HBaseClient(creds);

// Retrieve the cluster version
var version = client.GetVersion();
Console.WriteLine(version);</pre><p>

6.要创建一个新的HBase的表，使用此代码：
</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_10_8787659">// Create a new HBase table.
var testTableSchema = new TableSchema();
testTableSchema.name = "mytablename";
testTableSchema.columns.Add(new ColumnSchema() { name = "d" });
testTableSchema.columns.Add(new ColumnSchema() { name = "f" });
client.CreateTable(testTableSchema);</pre><p>


7.将数据与该代码表：
</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_11_7905983">// Insert data into a table.
var tableName = "mytablename";
var testKey = "content";
var testValue = "the force is strong in this column";
var set = new CellSet();
var row = new CellSet.Row { key = Encoding.UTF8.GetBytes(testKey) };
set.rows.Add(row);

var value = new Cell { column = Encoding.UTF8.GetBytes("d:starwars"), data = Encoding.UTF8.GetBytes(testValue) };
row.values.Add(value);
client.StoreCells(tableName, set);</pre><p>


8.要检索的细胞，其键，使用此代码。
</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_12_3120611">// Retrieve a cell with its key.
var testKey = "content";
var tableName = "mytablename";

var cells = client.GetCells(tableName, testKey);
// get the first value from the row.
.WriteLine(Encoding.UTF8.GetString(cells.rows[0].values[0].data));
// with the previous insert, it should yield: "the force is strong in this column"</pre><p>

9.扫描了与下面的代码表中的行：</p><pre class="plain" code_snippet_id="517747" name="code" snippet_file_name="blog_20141113_13_8335239">//Scan over rows in a table.
var creds = new ClusterCredentials(new Uri("https://myclustername.azurehdinsight.net"), "myusername", "mypassword");
var client = new HBaseClient(creds);

var tableName = "mytablename";

// assume the table has integer keys and we want data between keys 25 and 35
var scanSettings = new Scanner()
{
    batch = 10,
    startRow = BitConverter.GetBytes(25),
    endRow = BitConverter.GetBytes(35)
};

var scannerInfo = client.CreateScanner(tableName, scanSettings);
CellSet next = null;
while ((next = client.ScannerGetNext(scannerInfo)) != null)
{
    foreach (var row in next.rows)
    {
        // ... read the rows
    }
}</pre><p> </p><h2>总结</h2><p>
在本教程中，你已经学会了如何提供一个HBase的集群，如何创建表，并查看了HBase的外壳这些表中的数据。还学习了如何使用Hive来查询HBase的表和如何使用HBase的C＃API从表中创建一个HBase的表和检索数据的数据。
</p><h2>下一步是什么？</h2><span></span><p>

[](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-overview/)
：HBase的是建立在Hadoop的Apache的开源的NoSQL数据库，提供了大量的非结构化和半结构化数据的随机存取和强大的一致性。


[](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-provision-vnet)
：随着虚拟网络集成，HBase的集群可以部署到同一个虚拟网络作为你的应用程序，使应用程序可以直接与HBase的沟通。


[](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-analyze-twitter-sentiment/)
<a href="http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-analyze-twitter-sentiment/" target="_blank">感悟</a>：学习如何做在HDInsight的Hadoop集群使用HBase的大数据的实时<a href="http://en.wikipedia.org/wiki/Sentiment_analysis" target="_blank">情感分析</a>。</p><p>本文翻译自Microsoft Azure：
[http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-get-started/](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-get-started/)
</p><p> </p>

<!-- Baidu Button BEGIN -->
<div class="bdsharebuttonbox" style="float: right;">
<a class="bds_more" data-cmd="more" href="#" style="background-position:0 0 !important; background-image: url(http://bdimg.share.baidu.com/static/api/img/share/icons_0_16.png?v=d754dcc0.png) !important"></a>
<a class="bds_qzone" data-cmd="qzone" href="#" style="background-position:0 -52px !important" title="分享到QQ空间"></a>
<a class="bds_tsina" data-cmd="tsina" href="#" style="background-position:0 -104px !important" title="分享到新浪微博"></a>
<a class="bds_tqq" data-cmd="tqq" href="#" style="background-position:0 -260px !important" title="分享到腾讯微博"></a>
<a class="bds_renren" data-cmd="renren" href="#" style="background-position:0 -208px !important" title="分享到人人网"></a>
<a class="bds_weixin" data-cmd="weixin" href="#" style="background-position:0 -1612px !important" title="分享到微信"></a>
</div>
<script>window._bd_share_config = { "common": { "bdSnsKey": {}, "bdText": "", "bdMini": "1", "bdMiniList": false, "bdPic": "", "bdStyle": "0", "bdSize": "16" }, "share": {} }; with (document) 0[(getElementsByTagName('head')[0] || body).appendChild(createElement('script')).src = 'http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion=' + ~(-new Date() / 36e5)];</script>
<!-- Baidu Button END -->
<!--192.168.100.35-->
<ul class="article_next_prev">
<li class="prev_article"><span onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_shangyipian']);location.href='/yangzhenping/article/details/41079065';">上一篇</span><a href="/yangzhenping/article/details/41079065" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_shangyipian'])">有人试图登录我的账号5次！</a></li>
<li class="next_article"><span onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_xiayipian']);location.href='/yangzhenping/article/details/41212101';">下一篇</span><a href="/yangzhenping/article/details/41212101" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_xiayipian'])">分享下今天研究的流量上限DDos攻击分析和解决方案</a></li>
</ul>
<!-- Baidu Button BEGIN -->
<script data="type=tools&amp;uid=1536434" id="bdshare_js" type="text/javascript"></script>
<script id="bdshell_js" type="text/javascript"></script>
<script type="text/javascript">
    document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date()/3600000)
</script>
<!-- Baidu Button END -->
<div articleid="41079223" id="digg">
<dl class="digg digg_disable" id="btnDigg">
<dt onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_ding'])">顶</dt>
<dd>0</dd>
</dl>
<dl class="digg digg_disable" id="btnBury">
<dt onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_cai'])">踩</dt>
<dd>0</dd>
</dl>
</div>
</div>
<dl class="blog-associat-tag">
<dt>主题推荐</dt>
<dd>
<a class="blog-tage-red" href="http://www.csdn.net/tag/hadoop" target="_blank">hadoop</a>
<a class="blog-tage-red" href="http://www.csdn.net/tag/集群" target="_blank">集群</a>
<a class="blog-tage-red" href="http://www.csdn.net/tag/hive" target="_blank">hive</a>
<a class="blog-tage-red" href="http://www.csdn.net/tag/hadoop集群" target="_blank">hadoop集群</a>
<a class="blog-tage-red" href="http://www.csdn.net/tag/解决方案" target="_blank">解决方案</a>
</dd>
</dl>
<dl class="blog-ass-articl tracking-ad" data-mod="popu_36" id="res-relatived">
<dt><span>猜你在找</span></dt>
</dl>
<script type="text/javascript">
    var searchtitletags = '建立HBase的集群和HDInsight在Hadoop中使用Hive来查询它们' + ',' + 'hadoop,集群,hive,hadoop集群,解决方案';
    searchService({
        index: 'blog',
        query: searchtitletags,
        from: 10,
        size: 10,
        appendTo: '#res-relatived',
        url: 'recommend',
        his: 2,
        client: "blog_cf_enhance",
        tmpl: '<dd style="background:url(http://static.blog.csdn.net/skin/default/images/blog-dot-red3.gif) no-repeat 0 10px;"><a href="#{ url }" title="#{ title }" strategy="#{ strategy }">#{ title }</a></dd>'
    });

 </script>
<div id="ad_cen">
<script type="text/javascript">
              new Ad(4, 'ad_cen');
          </script>
</div>
<div class="comment_class">
<div class="panel_head" id="comment_title">
<span class="see_comment">查看评论</span><a name="comments"></a></div>
<div id="comment_list">
</div>
<div id="comment_bar">
</div>
<div id="comment_form">
</div>
<div class="announce">
        * 以上用户言论只代表其个人观点，不代表CSDN网站的观点或立场<a name="reply"></a><a name="quote"></a></div>
</div>
<script type="text/javascript">
    var fileName = '41079223';
    var commentscount = 0;
    var islock = false
</script>
<script src="http://static.blog.csdn.net/scripts/comment.js" type="text/javascript"></script>
<div id="ad_bot">
</div>
<script type="text/javascript">
    new Ad(5, 'ad_bot');
    </script>
<div id="report_dialog">
</div>
<div id="d-top" style="bottom:60px;">
<a class="btn btn-top q-reply" id="quick-reply" style="display:none;" title="快速回复">
<img alt="快速回复" src="http://static.blog.csdn.net/images/blog-icon-reply.png"/>
</a>
<a class="btn btn-top backtop" id="d-top-a" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_huidaodingbu'])" style="display: none;" title="返回顶部">
<img alt="TOP" src="http://static.blog.csdn.net/images/top.png"/>
</a>
</div>
<script type="text/javascript">
    $(function ()
    {
        $("#ad_frm_0").height("90px");
        
        setTimeout(function(){
            $("#ad_frm_2").height("200px");
        },1000);
        
        /*
        if($("#comment_content").length>0)
        {
            $("#quick-reply").show();

            $("#quick-reply").click(function(){
                setEditorFocus();
            });
        }       
     
        var d_top = $('#d-top-a');

        document.onscroll = function ()
        {
            var scrTop = (document.body.scrollTop || document.documentElement.scrollTop);
            if (scrTop > 500)
            {
                d_top.show();
            } else
            {
                d_top.hide();
            }
        }
        $('#d-top-a').click(function ()
        {
            scrollTo(0, 0);
            this.blur();
            return false;
        });
        */
    });
  
</script>
<style type="text/css">
    .tag_list
    {
        background: none repeat scroll 0 0 #FFFFFF;
        border: 1px solid #D7CBC1;
        color: #000000;
        font-size: 12px;
        line-height: 20px;
        list-style: none outside none;
        margin: 10px 2% 0 1%;
        padding: 1px;
    }
    .tag_list h5
    {
        background: none repeat scroll 0 0 #E0DBD3;
        color: #47381C;
        font-size: 12px;
        height: 24px;
        line-height: 24px;
        padding: 0 5px;
        margin: 0;
    }
    .tag_list h5 a
    {
        color: #47381C;
    }
    .classify
    {
        margin: 10px 0;
        padding: 4px 12px 8px;
    }
    .classify a
    {
        margin-right: 20px;
        white-space: nowrap;
    }
</style>
<div class="tag_list">
<h5>
<a href="http://www.csdn.net/tag/" target="_blank">核心技术类目</a></h5>
<div class="classify">
<a href="http://www.csdn.net/tag" onclick="LogClickCount(this,336);" target="_blank" title="全部主题">全部主题</a>
<a href="http://g.csdn.net/5272865" onclick="LogClickCount(this,336);" target="_blank" title="Hadoop">Hadoop</a>
<a href="http://g.csdn.net/5272866" onclick="LogClickCount(this,336);" target="_blank" title="AWS">AWS</a>
<a href="http://g.csdn.net/5272870" onclick="LogClickCount(this,336);" target="_blank" title="移动游戏">移动游戏</a>
<a href="http://g.csdn.net/5272871" onclick="LogClickCount(this,336);" target="_blank" title="Java">Java</a>
<a href="http://g.csdn.net/5272872" onclick="LogClickCount(this,336);" target="_blank" title="Android">Android</a>
<a href="http://g.csdn.net/5272873" onclick="LogClickCount(this,336);" target="_blank" title="iOS">iOS</a>
<a href="http://g.csdn.net/5272868" onclick="LogClickCount(this,336);" target="_blank" title="Swift">Swift</a>
<a href="http://g.csdn.net/5272869" onclick="LogClickCount(this,336);" target="_blank" title="智能硬件">智能硬件</a>
<a href="http://g.csdn.net/5272867" onclick="LogClickCount(this,336);" target="_blank" title="Docker">Docker</a>
<a href="http://g.csdn.net/5272925" onclick="LogClickCount(this,336);" target="_blank" title="OpenStack">OpenStack</a>
<a href="http://www.csdn.net/tag/vpn" onclick="LogClickCount(this,336);" target="_blank" title="VPN">VPN</a>
<a href="http://g.csdn.net/5272924" onclick="LogClickCount(this,336);" target="_blank" title="Spark">Spark</a>
<a href="http://www.csdn.net/tag/erp" onclick="LogClickCount(this,336);" target="_blank" title="ERP">ERP</a>
<a href="http://www.csdn.net/tag/ie10" onclick="LogClickCount(this,336);" target="_blank" title="IE10">IE10</a>
<a href="http://www.csdn.net/tag/eclipse" onclick="LogClickCount(this,336);" target="_blank" title="Eclipse">Eclipse</a>
<a href="http://www.csdn.net/tag/crm" onclick="LogClickCount(this,336);" target="_blank" title="CRM">CRM</a>
<a href="http://www.csdn.net/tag/javascript" onclick="LogClickCount(this,336);" target="_blank" title="JavaScript">JavaScript</a>
<a href="http://www.csdn.net/tag/数据库" onclick="LogClickCount(this,336);" target="_blank" title="数据库">数据库</a>
<a href="http://www.csdn.net/tag/ubuntu" onclick="LogClickCount(this,336);" target="_blank" title="Ubuntu">Ubuntu</a>
<a href="http://www.csdn.net/tag/nfc" onclick="LogClickCount(this,336);" target="_blank" title="NFC">NFC</a>
<a href="http://www.csdn.net/tag/wap" onclick="LogClickCount(this,336);" target="_blank" title="WAP">WAP</a>
<a href="http://www.csdn.net/tag/jquery" onclick="LogClickCount(this,336);" target="_blank" title="jQuery">jQuery</a>
<a href="http://www.csdn.net/tag/bi" onclick="LogClickCount(this,336);" target="_blank" title="BI">BI</a>
<a href="http://www.csdn.net/tag/html5" onclick="LogClickCount(this,336);" target="_blank" title="HTML5">HTML5</a>
<a href="http://www.csdn.net/tag/spring" onclick="LogClickCount(this,336);" target="_blank" title="Spring">Spring</a>
<a href="http://www.csdn.net/tag/apache" onclick="LogClickCount(this,336);" target="_blank" title="Apache">Apache</a>
<a href="http://www.csdn.net/tag/.net" onclick="LogClickCount(this,336);" target="_blank" title=".NET">.NET</a>
<a href="http://www.csdn.net/tag/api" onclick="LogClickCount(this,336);" target="_blank" title="API">API</a>
<a href="http://www.csdn.net/tag/html" onclick="LogClickCount(this,336);" target="_blank" title="HTML">HTML</a>
<a href="http://www.csdn.net/tag/sdk" onclick="LogClickCount(this,336);" target="_blank" title="SDK">SDK</a>
<a href="http://www.csdn.net/tag/iis" onclick="LogClickCount(this,336);" target="_blank" title="IIS">IIS</a>
<a href="http://www.csdn.net/tag/fedora" onclick="LogClickCount(this,336);" target="_blank" title="Fedora">Fedora</a>
<a href="http://www.csdn.net/tag/xml" onclick="LogClickCount(this,336);" target="_blank" title="XML">XML</a>
<a href="http://www.csdn.net/tag/lbs" onclick="LogClickCount(this,336);" target="_blank" title="LBS">LBS</a>
<a href="http://www.csdn.net/tag/unity" onclick="LogClickCount(this,336);" target="_blank" title="Unity">Unity</a>
<a href="http://www.csdn.net/tag/splashtop" onclick="LogClickCount(this,336);" target="_blank" title="Splashtop">Splashtop</a>
<a href="http://www.csdn.net/tag/uml" onclick="LogClickCount(this,336);" target="_blank" title="UML">UML</a>
<a href="http://www.csdn.net/tag/components" onclick="LogClickCount(this,336);" target="_blank" title="components">components</a>
<a href="http://www.csdn.net/tag/windowsmobile" onclick="LogClickCount(this,336);" target="_blank" title="Windows Mobile">Windows Mobile</a>
<a href="http://www.csdn.net/tag/rails" onclick="LogClickCount(this,336);" target="_blank" title="Rails">Rails</a>
<a href="http://www.csdn.net/tag/qemu" onclick="LogClickCount(this,336);" target="_blank" title="QEMU">QEMU</a>
<a href="http://www.csdn.net/tag/kde" onclick="LogClickCount(this,336);" target="_blank" title="KDE">KDE</a>
<a href="http://www.csdn.net/tag/cassandra" onclick="LogClickCount(this,336);" target="_blank" title="Cassandra">Cassandra</a>
<a href="http://www.csdn.net/tag/cloudstack" onclick="LogClickCount(this,336);" target="_blank" title="CloudStack">CloudStack</a>
<a href="http://www.csdn.net/tag/ftc" onclick="LogClickCount(this,336);" target="_blank" title="FTC">FTC</a>
<a href="http://www.csdn.net/tag/coremail" onclick="LogClickCount(this,336);" target="_blank" title="coremail">coremail</a>
<a href="http://www.csdn.net/tag/ophone " onclick="LogClickCount(this,336);" target="_blank" title="OPhone ">OPhone </a>
<a href="http://www.csdn.net/tag/couchbase" onclick="LogClickCount(this,336);" target="_blank" title="CouchBase">CouchBase</a>
<a href="http://www.csdn.net/tag/云计算" onclick="LogClickCount(this,336);" target="_blank" title="云计算">云计算</a>
<a href="http://www.csdn.net/tag/iOS6" onclick="LogClickCount(this,336);" target="_blank" title="iOS6">iOS6</a>
<a href="http://www.csdn.net/tag/rackspace " onclick="LogClickCount(this,336);" target="_blank" title="Rackspace ">Rackspace </a>
<a href="http://www.csdn.net/tag/webapp" onclick="LogClickCount(this,336);" target="_blank" title="Web App">Web App</a>
<a href="http://www.csdn.net/tag/springside" onclick="LogClickCount(this,336);" target="_blank" title="SpringSide">SpringSide</a>
<a href="http://www.csdn.net/tag/maemo" onclick="LogClickCount(this,336);" target="_blank" title="Maemo">Maemo</a>
<a href="http://www.csdn.net/tag/compuware" onclick="LogClickCount(this,336);" target="_blank" title="Compuware">Compuware</a>
<a href="http://www.csdn.net/tag/大数据" onclick="LogClickCount(this,336);" target="_blank" title="大数据">大数据</a>
<a href="http://www.csdn.net/tag/aptech" onclick="LogClickCount(this,336);" target="_blank" title="aptech">aptech</a>
<a href="http://www.csdn.net/tag/perl" onclick="LogClickCount(this,336);" target="_blank" title="Perl">Perl</a>
<a href="http://www.csdn.net/tag/tornado" onclick="LogClickCount(this,336);" target="_blank" title="Tornado">Tornado</a>
<a href="http://www.csdn.net/tag/ruby" onclick="LogClickCount(this,336);" target="_blank" title="Ruby">Ruby</a>
<a href="http://www.csdn.net/hibernate" onclick="LogClickCount(this,336);" target="_blank" title="Hibernate">Hibernate</a>
<a href="http://www.csdn.net/tag/thinkphp" onclick="LogClickCount(this,336);" target="_blank" title="ThinkPHP">ThinkPHP</a>
<a href="http://www.csdn.net/tag/hbase" onclick="LogClickCount(this,336);" target="_blank" title="HBase">HBase</a>
<a href="http://www.csdn.net/tag/pure" onclick="LogClickCount(this,336);" target="_blank" title="Pure">Pure</a>
<a href="http://www.csdn.net/tag/solr" onclick="LogClickCount(this,336);" target="_blank" title="Solr">Solr</a>
<a href="http://www.csdn.net/tag/angular" onclick="LogClickCount(this,336);" target="_blank" title="Angular">Angular</a>
<a href="http://www.csdn.net/tag/cloudfoundry" onclick="LogClickCount(this,336);" target="_blank" title="Cloud Foundry">Cloud Foundry</a>
<a href="http://www.csdn.net/tag/redis" onclick="LogClickCount(this,336);" target="_blank" title="Redis">Redis</a>
<a href="http://www.csdn.net/tag/scala" onclick="LogClickCount(this,336);" target="_blank" title="Scala">Scala</a>
<a href="http://www.csdn.net/tag/django" onclick="LogClickCount(this,336);" target="_blank" title="Django">Django</a>
<a href="http://www.csdn.net/tag/bootstrap" onclick="LogClickCount(this,336);" target="_blank" title="Bootstrap">Bootstrap</a>
</div>
</div>
<div id="pop_win" style="display:none ;position: absolute; z-index: 10000; border: 1px solid rgb(220, 220, 220); top: 222.5px; left: 630px; opacity: 1; background: none 0px 0px repeat scroll rgb(255, 255, 255);">
</div>
<div id="popup_mask"></div>
<style>
    #popup_mask
    {
        position: absolute;
        width: 100%;
        height: 100%;
        background: #000;
        z-index: 9999;
        left: 0px;
        top: 0px;
        opacity: 0.3;
        filter: alpha(opacity=30);
        display: none;
    }

</style>
<script type="text/javascript">
    $(function(){
        setTimeout(function(){
            $(".comment_body:contains('回复')").each(function(index,item){
                var u=$(this).text().split('：')[0].toString().replace("回复","")
                var thisComment=$(this);
                if(u)
                {
                    $.getJSON("https://passport.csdn.net/get/nick?callback=?", {users: u}, function(a) {
                        if(a!=null&&a.data!=null&&a.data.length>0)
                        {
                            nick=a.data[0].n; 
                            if(u!=nick)
                            {
                                thisComment.text(thisComment.text().replace(u,nick));  
                            }
                        }       
                    });  
                }
            });
        },200);  
        
        setTimeout(function(){
            $("a img[src='http://js.tongji.linezing.com/stats.gif']").parent().css({"position":"absolute","left":"50%"});
        },300);
    });

    function loginbox(){
        var $logpop=$("#pop_win");
        $logpop.html('<iframe src="https://passport.csdn.net/account/loginbox?service=http://static.blog.csdn.net/callback.htm" frameborder="0" height="600" width="400" scrolling="no"></iframe>');

        $('#popup_mask').css({
            opacity: 0.5,
            width: $( document ).width() + 'px',
            height:  $( document ).height() + 'px'
        });
        $('#popup_mask').css("display","block");
 
        $logpop.css( {
            top: ($( window ).height() - $logpop.height())/ 2  + $( window 
       ).scrollTop() + 'px',
            left:($( window ).width() - $logpop.width())/ 2
        } );
 
        setTimeout( function () {
            $logpop.show();
            $logpop.css( {
                opacity: 1
            } );
        }, 200 );
 
        $('#popup_mask').unbind("click");
        $('#popup_mask').bind("click", function(){
            $('#popup_mask').hide();
            var $clopop = $("#pop_win");
            $("#common_ask_div_sc").css("display","none");
            $clopop.css( {
                opacity: 0
            } );
            setTimeout( function () {
                $clopop.hide();
            }, 350 );
            return false;
        });
    }    

</script>
<div class="clear">
</div>
</div>
</div>
<div id="side">
<div class="side">
<div class="panel" id="panel_Profile">
<ul class="panel_head"><span>个人资料</span></ul>
<ul class="panel_body profile">
<div id="blog_userface">
<a href="http://my.csdn.net/yangzhenping" target="_blank">
<img src="http://avatar.csdn.net/F/E/0/1_yangzhenping.jpg" style="max-width:90%" title="访问我的空间"/>
</a>
<br/>
<span><a class="user_name" href="http://my.csdn.net/yangzhenping" target="_blank">yangzhenping</a></span>
</div>
<div class="interact">
<a class="attent" href="javascript:void(0);" id="span_add_follow" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_guanzhu'])" title="[加关注]"></a>
<a class="letter" href="javascript:void(0);" onclick="window.open('http://msg.csdn.net/letters/model?receiver=yangzhenping','_blank','height=350,width=700');_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_sixin'])" title="[发私信]"></a>
</div>
<div id="blog_medal">
<div class="ico_expert" style="width:54px;height:60px;background:url('http://csdnimg.cn/jifen/images/xunzhang/xunzhang/bokezhuanjiamiddle.png') no-repeat" title="CSDN认证专家"></div>
<div id="bms_box">
<a target="_blank">
<img alt="2" onmouseout="m_out_m()" onmouseover="m_over_m(this,2)" src="http://csdnimg.cn/jifen/images/xunzhang/xunzhang/zhuanlandaren.png"/>
</a>
<a target="_blank">
<img alt="1" onmouseout="m_out_m()" onmouseover="m_over_m(this,4)" src="http://csdnimg.cn/jifen/images/xunzhang/xunzhang/chizhiyiheng.png"/>
</a>
</div>
</div>
<ul id="blog_rank">
<li>访问：<span>140902次</span></li>
<li>积分：<span>4908</span> </li>
<li>等级： <span style="position:relative;display:inline-block;z-index:1">
<img alt="" id="leveImg" src="http://csdnimg.cn/jifen/images/xunzhang/jianzhang/blog5.png" style="vertical-align: middle;"/>
<div id="smallTittle" style=" position: absolute;  left: -24px;  top: 25px;  text-align: center;  width: 101px;  height: 32px;  background-color: #fff;  line-height: 32px;  border: 2px #DDDDDD solid;  box-shadow: 0px 2px 2px rgba (0,0,0,0.1);  display: none;   z-index: 999;">
<div style="left: 42%;  top: -8px;  position: absolute;  width: 0;  height: 0;  border-left: 10px solid transparent;  border-right: 10px solid transparent;  border-bottom: 8px solid #EAEAEA;"></div>
            积分：4908 </div>
</span> </li>
<li>排名：<span>第1828名</span></li>
</ul>
<ul id="blog_statistics">
<li>原创：<span>316篇</span></li>
<li>转载：<span>3篇</span></li>
<li>译文：<span>41篇</span></li>
<li>评论：<span>26条</span></li>
</ul>
</ul>
</div>
<div class="panel" id="custom_column_25862659">
<ul class="panel_head"><span>个人简介</span></ul>
<ul class="panel_body">

专注于微软System Center和微软公有云，私有云系列产品，主要使用C#.net和php进行个人爱好开发。<br/>
曾参与Windows Azure Integration Pack for Orchestrator in System Center 2012 SP1的开发和测试。

</ul>
</div><div class="panel" id="panel_Search">
<ul class="panel_head"><span>文章搜索</span></ul>
<ul class="panel_body">
</ul><form action="http://so.csdn.net/search" class="form_search" id="frmSearch" target="_blank">
<span><input class="blogsearch" id="inputSearch" title="请输入关键字" type="text"/></span>
<input id="btnSubmit" title="search in blog" type="button" value="搜索"/>
<input id="inputQ" name="q" type="hidden"/>
<input name="t" type="hidden" value="blog"/>
<a id="btnSearchBlog" target="_blank"></a>
</form>
</div>
<script type="text/javascript">
    $(function () {
        $("#btnSubmit").click(function () {           
            search();
        });

        $("#frmSearch").submit(function () {
            search();
            return false;
        });

        function search()
        {
            var url = "http://so.csdn.net/so/search/s.do?q=" + encodeURIComponent($("#inputSearch").val()) + "&u=" + username + "&t=blog";
            window.location.href = url;
        }   
    });
</script>
<div class="panel" id="custom_column_22449642">
<ul class="panel_head"><span>友情链接</span></ul>
<ul class="panel_body">
<a href="http://qq.ihaonet.com/" title="点击进入全球最大QQ聊天交友网">全球最大QQ聊天交友网 </a><br/>
<a href="http://weixin.ihaonet.com/" title="点击进入微信（易信，新浪）二维码交友">微信（易信，新浪）二维码交友</a>
<br/>
<a href="http://health.ihaonet.com/" title="点击进入餐前健康测试网">每餐餐前健康测试 </a><br/>
</ul>
</div><div class="panel" id="panel_Category">
<ul class="panel_head"><span>博客专栏</span></ul>
<ul class="panel_body" id="sp_column">
<table cellpadding="0" cellspacing="0"><tr>
<td style="padding:10px 10px 0 0;">
<a href="http://blog.csdn.net/column/details/bigdatahdinsight.html" target="_blank"><img src="http://avatar.csdn.net/blogpic/20141110164133187.jpg" style="width:75px;height:75px;"/></a>
</td>
<td style="padding:10px 0; vertical-align:top;">
<a href="http://blog.csdn.net/column/details/bigdatahdinsight.html" target="_blank">微软大数据HDInsight-Hadoop实战</a>
<p>文章：5篇</p>
<span>阅读：1842</span>
</td>
</tr></table>
<table cellpadding="0" cellspacing="0"><tr>
<td style="padding:10px 10px 0 0;">
<a href="http://blog.csdn.net/column/details/clouddesignpattern.html" target="_blank"><img src="http://avatar.csdn.net/blogpic/20141104165323359.jpg" style="width:75px;height:75px;"/></a>
</td>
<td style="padding:10px 0; vertical-align:top;">
<a href="http://blog.csdn.net/column/details/clouddesignpattern.html" target="_blank">云计算设计模式</a>
<p>文章：24篇</p>
<span>阅读：6729</span>
</td>
</tr></table>
</ul>
</div>
<div class="panel" id="panel_Category">
<ul class="panel_head"><span>文章分类</span></ul>
<ul class="panel_body">
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/670097" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">.net</a><span>(36)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/712982" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">ASP.NET</a><span>(13)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/734448" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">C#</a><span>(35)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/541607" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">c++</a><span>(17)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/732062" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">Computer</a><span>(6)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/541606" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">c语言</a><span>(9)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/549155" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">java</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/656234" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">linux实验</a><span>(8)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/729927" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">PowerShell</a><span>(14)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/557794" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">UML</a><span>(9)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/729922" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">Work</a><span>(0)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/665764" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">WPF</a><span>(17)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/502063" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">其他</a><span>(16)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/656546" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">发布小工具</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/658831" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">套接字编程</a><span>(9)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/543178" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">娱乐</a><span>(5)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/671190" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">弱者求强</a><span>(16)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/671193" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">弱者求强</a><span>(15)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/502218" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">数据库</a><span>(3)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/541611" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">数据结构</a><span>(7)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/656235" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">数据结构课程设计</a><span>(9)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/624948" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">数论</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/546896" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">研究源码</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/727826" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">程序人生</a><span>(19)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/502044" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">算法</a><span>(11)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/655728" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">经济生活</a><span>(19)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/543839" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">网络</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/540506" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">考研</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/712983" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">面试参考</a><span>(23)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/588148" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">项目</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1172658" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">敏捷建模</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1280869" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">System Center Orchestrator</a><span>(5)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1299302" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">System Center VMM</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1299303" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">System Center OM</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1299304" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">System Center SM</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1299306" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">System Center CM</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1299307" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">System Center DPM</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1299308" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">System Center App Controller</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1299309" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">Windows Azure</a><span>(5)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1360272" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">MS SQL Server</a><span>(6)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1543189" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">PHP</a><span>(4)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1661347" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">Linq</a><span>(3)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1661483" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">MVC</a><span>(8)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1669675" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">域名</a><span>(28)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1676845" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">SQL</a><span>(9)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1740007" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">论坛</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1756847" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">搜索引擎</a><span>(4)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/1842337" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">互联网</a><span>(13)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2136055" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">网络支付</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2136057" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">支付安全</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2148409" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">比特币</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2618411" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">云计算</a><span>(43)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2657825" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">大数据</a><span>(8)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2663541" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">service bus</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2663543" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">aliyun</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2663545" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">ONS</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2683177" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">架构</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2683179" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">设计</a><span>(23)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2685787" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">设计模式</a><span>(24)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2700207" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">HDInsight</a><span>(5)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2700209" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">Hadoop</a><span>(7)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2700211" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">YARN</a><span>(3)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2700215" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">Pig</a><span>(3)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2700217" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">Hive</a><span>(5)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2700219" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">HDFS</a><span>(3)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2700221" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">MapReduce</a><span>(2)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2700315" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">HBase</a><span>(5)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2719223" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">网站安全</a><span>(7)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2719225" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">黑客攻击</a><span>(5)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2752665" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">docker</a><span>(5)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2752667" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">CoreOS</a><span>(1)</span>
</li>
<li>
<a href="http://blog.csdn.net/yangzhenping/article/category/2754853" onclick="_gaq.push(['_trackEvent','function', 'onclick', 'blog_articles_wenzhangfenlei']); ">Fedora</a><span>(1)</span>
</li>
</ul>
</div><div class="panel" id="panel_Archive">
<ul class="panel_head"><span>文章存档</span></ul>
<ul class="panel_body">
<div id="archive_list">
<!--归档统计-->
<li><a href="http://blog.csdn.net/yangzhenping/article/month/2014/12">2014年12月</a><span>(10)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2014/11">2014年11月</a><span>(36)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2014/10">2014年10月</a><span>(12)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2014/07">2014年07月</a><span>(3)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2014/06">2014年06月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2014/04">2014年04月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2014/03">2014年03月</a><span>(10)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2014/02">2014年02月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2014/01">2014年01月</a><span>(2)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/12">2013年12月</a><span>(6)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/11">2013年11月</a><span>(4)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/10">2013年10月</a><span>(16)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/09">2013年09月</a><span>(21)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/08">2013年08月</a><span>(8)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/07">2013年07月</a><span>(3)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/06">2013年06月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/05">2013年05月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/04">2013年04月</a><span>(4)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/03">2013年03月</a><span>(2)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/02">2013年02月</a><span>(2)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2013/01">2013年01月</a><span>(7)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2012/12">2012年12月</a><span>(2)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2012/11">2012年11月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2012/10">2012年10月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2012/08">2012年08月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2012/06">2012年06月</a><span>(3)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2012/04">2012年04月</a><span>(3)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2012/03">2012年03月</a><span>(2)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2012/02">2012年02月</a><span>(3)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2011/06">2011年06月</a><span>(23)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/12">2010年12月</a><span>(2)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/11">2010年11月</a><span>(6)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/10">2010年10月</a><span>(5)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/09">2010年09月</a><span>(23)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/08">2010年08月</a><span>(3)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/07">2010年07月</a><span>(28)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/06">2010年06月</a><span>(9)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/05">2010年05月</a><span>(2)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/04">2010年04月</a><span>(12)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/03">2010年03月</a><span>(12)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2010/02">2010年02月</a><span>(59)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2009/12">2009年12月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2009/11">2009年11月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2009/10">2009年10月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2009/09">2009年09月</a><span>(4)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2009/07">2009年07月</a><span>(1)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2009/06">2009年06月</a><span>(10)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2009/05">2009年05月</a><span>(2)</span></li><li><a href="http://blog.csdn.net/yangzhenping/article/month/2008/08">2008年08月</a><span>(1)</span></li>
</div>
</ul>
</div>
</div>
<div class="clear">
</div>
</div>
<div class="clear">
</div>
</div>
<script src="http://csdnimg.cn/rabbit/cnick/cnick.js" type="text/javascript"></script>
<script src="http://static.blog.csdn.net/scripts/newblog.min.js" type="text/javascript"></script>
<script src="http://medal.blog.csdn.net/showblogmedal.ashx?blogid=260656" type="text/javascript"></script>
<script src="http://static.blog.csdn.net/scripts/JavaScript1.js" type="text/javascript"></script>
<script src="http://passport.csdn.net/content/loginbox/login.js" type="text/javascript"></script>
<script type="text/javascript">document.write("<img src=http://counter.csdn.net/pv.aspx?id=24 border=0 width=0 height=0>");</script>
<script src="http://www.csdn.net/ui/scripts/Csdn/counter.js" type="text/javascript"></script>
<script src="http://ad.csdn.net/scripts/ad-blog.js" type="text/javascript"></script>
<script src="http://zz.csdn.net/js/count.js" type="text/javascript"></script>
<script type="text/javascript">
    $(function () {
        function __get_code_toolbar(snippet_id) {
            return $("<a href='https://code.csdn.net/snippets/"
                    + snippet_id
                    + "' target='_blank' title='在CODE上查看代码片' style='text-indent:0;'><img src='https://code.csdn.net/assets/CODE_ico.png' width=12 height=12 alt='在CODE上查看代码片' style='position:relative;top:1px;left:2px;'/></a>"
                    + "<a href='https://code.csdn.net/snippets/"
                    + snippet_id
                    + "/fork' target='_blank' title='派生到我的代码片'  style='text-indent:0;'><img src='https://code.csdn.net/assets/ico_fork.svg' width=12 height=12 alt='派生到我的代码片' style='position:relative;top:2px;left:2px;'/></a>");
        }
        
        $("[code_snippet_id]").each(function () {
            __s_id = $(this).attr("code_snippet_id");
            if (__s_id != null && __s_id != "" && __s_id != 0 && parseInt(__s_id) > 70020) {
                __code_tool = __get_code_toolbar(__s_id);
                $(this).prev().find(".tools").append(__code_tool);
            }
        });
    });
</script>
</div>
<!--new top-->
<script btnid="header_notice_num" count="5" id="csdn-toolbar-id" src="http://static.csdn.net/public/common/toolbar/js/toolbar.js" subcount="5" type="text/javascript" wrapid="note1"></script> <!--new top-->
<link href="http://csdnimg.cn/comm_ask/css/ask_float_block.css" rel="stylesheet" type="text/css"/>
<script language="JavaScript" src="http://csdnimg.cn/comm_ask/js/libs/wmd.js" type="text/javascript"></script>
<script language="JavaScript" src="http://csdnimg.cn/comm_ask/js/libs/showdown.js" type="text/javascript"></script>
<script language="JavaScript" src="http://csdnimg.cn/comm_ask/js/libs/prettify.js" type="text/javascript"></script>
<script language="JavaScript" src="http://csdnimg.cn/comm_ask/js/apps/ask_float_block.js" type="text/javascript"></script>
</body>
</html>
