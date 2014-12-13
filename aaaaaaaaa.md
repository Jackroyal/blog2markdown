
建立HBase的集群和HDInsight在Hadoop中使用Hive来查询它们
在本教程中，您将学习如何创建和查询HDInsight使用HiveHadoop的HBase的表。下列步骤描述：
•如何使用提供在Azure门户的HBase的集群。
•如何启用和使用RDP访问HBase的外壳，并使用HBase的外壳创建HBase的示例表，添加行，然后列出表中的行。
•如何创建一个Hive表映射到一个现有的HBase的表，使用HiveQL查询数据在HBase的表。
•如何使用Microsoft HBase的REST客户端库.NET创建一个新的HBase的表，列出您帐户中的HBase的表，以及如何从表添加和检索行。

##什么是HBase的？
HBase的是一种低延迟的NoSQL数据库，让大数据的联机事务处理。 HBase的是提供一个管理的集群集成到Azure的环境。集群被配置为直接在Azure中的Blob存储，这提供了在性能/成本的选择低延迟和增加的弹性存储数据。这使客户能够建立一个大型数据集工作的互动式网站，构建存储传感器和遥测数据，从数以百万计的端点的服务，并分析这些数据与Hadoop作业。关于HBase的，它可以被用于方案的详细信息，请参阅
[HDInsight HBase的](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-overview/)

[概述](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-overview/)
。


&amp;lt;strong&amp;gt;注意：&amp;lt;/strong&amp;gt;

HBase的（版本0.98.0）仅适用于在HDInsight与HDInsight3.1集群的使用（基于Apache Hadoop和YARN2.4.0）。对于版本信息，请查看
[有什么](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-component-versioning/)

[新的由HDInsight提供的Hadoop集群的版本？](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-component-versioning/)

##先决条件：
开始之前本教程中，你必须具备以下条件：
•一个Azure订阅有关获取预订的详细信息，请参阅购买选项，会员优惠或免费试用。
•一个Azure存储帐户有关说明，请参阅如何创建存储帐户。
•与安装了Visual Studio2013的工作站。有关说明，请参阅安装Visual Studio。
•下载微软HBase的REST客户端库.NET。

估计时间来完成：30分钟
##在本教程中的部分
•提供了Azure中门户网站的HBase的集群
•从HBase的外壳创建HBase的示例表
•使用Hive查询的HBase的表
•使用HBase的C＃API从表中创建一个HBase的表和检索数据
•摘要
•下一步是什么？ 
##在Azure门户提供的HBase的集群
本节将介绍如何使用提供在Azure门户的HBase的集群。
 

&amp;amp;lt;strong&amp;amp;gt;注意：&amp;amp;lt;/strong&amp;amp;gt;

本文中的步骤创建使用基本配置设置HDInsight集群。对于其他群集配置设置，例如使用Azure中虚拟网络或metastore用于Hive和Oozie的信息，请参阅
[提供一个HDInsight](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-provision-clusters/)

[群集](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-provision-clusters/)
。
 
为了提供一个HDInsight在Azure中门户网站集群
1。登录到
[Azure管理门户](https://manage.windowsazure.com/)
。

2。点击左侧HDInsight列出集群您的帐户，然后在左下角的+新图标的状态。
![](http://img.blog.csdn.net/20141113145927328?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
3.点击在从左侧和在下一列则HBase的选项的第二列的HDInsight图标。指定群集名称和簇大小，存储帐户的名称，并为新的HBase集群密码的值。
![](http://img.blog.csdn.net/20141113150018826?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
4.单击在较低的检查左侧的图标创建HBase的集群。


##从HBase的外壳创建HBase的示例表
本节介绍如何启用和使用远程桌面协议（RDP）来访问HBase的外壳，然后用它来创建一个HBase的示例表，添加行，然后列出表中的行。

它假定您已经完成了第一部分概述的过程，所以已经成功地创建了一个HBase的集群。

###启用RDP连接到HBase的集群
1.To使到HDInsight集群中的远程桌面连接，选择已创建的HBase的集群，然后单击配置选项卡。点击ENABLE在页面底部遥控按钮启用RDP连接到群集。
2.提供的配置远程桌面向导的凭据和到期日期，点击右下角的检查循环。 （这可能需要几分钟的操作来完成。）
3.To连接到HDInsight集群，点击连接按钮，在配置选项卡的底部。

###打开HBase的壳
1.在你的RDP会话，点击位于桌面上的Hadoop的命令提示符快捷方式。

2.文件夹切换到HBase的主目录：
```plain
cd %HBASE_HOME%\bin
```

 3。打开HBase的外壳：
```plain
hbase shell
```

 创建一个示例表，添加数据和检索数据
1.创建示例表：

```plain
create 'sampletable', 'cf1'
```


2.添加一行到示例表：

```plain
put 'sampletable', 'row1', 'cf1:col1', 'value1'
```


3.列出在示例表中的行：
```plain
scan 'sampletable'
```
 
##使用Hive查询的HBase的表
现在你有一个HBase的集群配置和已经创建了一个表，你可以使用Hive查询。本节将创建一个Hive表映射到HBase的表，并使用该查询中的数据HBase的表。

要打开集群仪表板
1.登录到Azure管理门户。
2.从左侧窗格中点击HDINSIGHT。你会看到创建包括你刚才在上一节中创建的群列表。
3.单击您要运行的Hive作业的群集名称。
4.单击管理CLUSTER从页面底部的疏散星团仪表板。它不同的浏览器选项卡上打开一个网页。

5.输入Hadoop的用户帐户的用户名和密码。默认用户名为admin，密码是您在提供过程中输入的内容。仪表板是这样的：
![](http://img.blog.csdn.net/20141113150501125?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWFuZ3poZW5waW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

###要运行Hive查询
1。 要创建一个Hive表映射到HBase的表，在下面输入HiveQL脚本到Hive控制台窗口，然后点击提交按钮。请确保您已创建使用HBase的壳牌执行该语句之前此处引用的HBase中的sampletable。
```plain
CREATE EXTERNAL TABLE hbasesampletable(rowkey STRING, col1 STRING, col2 STRING)
STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES ('hbase.columns.mapping' = ':key,cf1:col1,cf1:col2')
TBLPROPERTIES ('hbase.table.name' = 'sampletable');
```

 2.要执行一个Hive查询在数据中的HBase的，输入下面的HiveQL脚本到Hive控制台窗口，然后点击提交按钮。
```plain
SELECT count(*) FROM hbasesampletable;
```

 3.要检索Hive查询的结果，请单击当作业完成执行作业会话窗口中查看详细信息链接。


&amp;lt;strong&amp;gt;注：&amp;lt;/strong&amp;gt;HBase的外壳链接切换标签到HBase的外壳。

###浏览输出文件
1.从群集面板，单击文件从顶部。
2.Click普顿 - 求职状态。
3.Click拥有的最后修改时间作业开始时间之前记录下来后，一点点的GUID数。记下此GUID的。你会需要它在下一节。
4，标准输出文件中有你需要在接下来的章节中的数据。您可以单击标准输出，如果你想下载的数据文件的副本。
##使用HBase的REST客户端库.NET C＃API从表中创建一个HBase的表和检索数据
 
微软HBase的REST客户端库.NET项目必须从GitHub的建成使用HBase的.NET SDK项目下载。下面的过程包括用于此任务的指示。
1. Downnload微软HBase的REST客户端库.NET，如果你还没有满足这一前提条件。

2.打开Marlin.sln在Visual Studio中（文件 - &amp;amp;gt;项目/解决方案... - &amp;amp;gt;打开），从它被下载到的位置。选择查看 - &amp;amp;gt;解决方案资源管理器中看到的“马林”的解决方案及其Microsoft.HBase.Client项目。构建马林项目通过在Solution Explorer中右击它并选择生成解决方案。

3.创建一个新的Visual C＃控制台应用程序。检索建（从...\ BIN\调试\ Microsoft.HBase.Client目录）所产生的Microsoft.HBase.Client.dll和protobuf.dll并将它们添加到您的C＃项目：在引用单击鼠标右键，选择添加引用...，浏览到两个组件，并将其上传。 protobuf网是一个.NET实现了谷歌的Protocol Buffers的二进制序列的用于数据通信。

4.添加以下using语句上的文件的顶部：

```plain
using Microsoft.HBase.Client;
using org.apache.hadoop.hbase.rest.protobuf.generated;
```


5.使用群集凭据创建HBase的客户端的新实例和检索集群版本：

```plain
// Create a new instance of an HBase client.
var creds = new ClusterCredentials(new Uri("https://myclustername.azurehdinsight.net"), "myusername", "mypassword");
var client = new HBaseClient(creds);

// Retrieve the cluster version
var version = client.GetVersion();
Console.WriteLine(version);
```


6.要创建一个新的HBase的表，使用此代码：

```plain
// Create a new HBase table.
var testTableSchema = new TableSchema();
testTableSchema.name = "mytablename";
testTableSchema.columns.Add(new ColumnSchema() { name = "d" });
testTableSchema.columns.Add(new ColumnSchema() { name = "f" });
client.CreateTable(testTableSchema);
```



7.将数据与该代码表：

```plain
// Insert data into a table.
var tableName = "mytablename";
var testKey = "content";
var testValue = "the force is strong in this column";
var set = new CellSet();
var row = new CellSet.Row { key = Encoding.UTF8.GetBytes(testKey) };
set.rows.Add(row);

var value = new Cell { column = Encoding.UTF8.GetBytes("d:starwars"), data = Encoding.UTF8.GetBytes(testValue) };
row.values.Add(value);
client.StoreCells(tableName, set);
```



8.要检索的细胞，其键，使用此代码。

```plain
// Retrieve a cell with its key.
var testKey = "content";
var tableName = "mytablename";

var cells = client.GetCells(tableName, testKey);
// get the first value from the row.
.WriteLine(Encoding.UTF8.GetString(cells.rows[0].values[0].data));
// with the previous insert, it should yield: "the force is strong in this column"
```


9.扫描了与下面的代码表中的行：
```plain
//Scan over rows in a table.
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
}
```
 
##总结
在本教程中，你已经学会了如何提供一个HBase的集群，如何创建表，并查看了HBase的外壳这些表中的数据。还学习了如何使用Hive来查询HBase的表和如何使用HBase的C＃API从表中创建一个HBase的表和检索数据的数据。

##下一步是什么？

[HDInsight HBase的概述](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-overview/)
：HBase的是建立在Hadoop的Apache的开源的NoSQL数据库，提供了大量的非结构化和半结构化数据的随机存取和强大的一致性。


[提供HBase的集群在Azure虚拟网络](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-provision-vnet)
：随着虚拟网络集成，HBase的集群可以部署到同一个虚拟网络作为你的应用程序，使应用程序可以直接与HBase的沟通。


[与HBase的在HDInsight分析Twitter的](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-analyze-twitter-sentiment/)

[感悟](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-analyze-twitter-sentiment/)
：学习如何做在HDInsight的Hadoop集群使用HBase的大数据的实时
[情感分析](http://en.wikipedia.org/wiki/Sentiment_analysis)
。本文翻译自Microsoft Azure：
[http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-get-started/](http://azure.microsoft.com/en-us/documentation/articles/hdinsight-hbase-get-started/)

 
