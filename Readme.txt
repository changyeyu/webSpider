

【UI  界面】
	            ==========    RenRen Spider    ==========
	                     
		[1] Login my RenRen account
            	[2] Login and Visit a friend
            	[3] Login and Leave a message to a friend
            	[4] Login and Get all my friends info 
                	and head Image
            	[5] ByeBye


【功    能】
		登录人人帐号
		访问好友主页
		给好友留言（可以是自己）
		统计个人好友,保存所有好友大图到本地
		抓取好友头像并保存头像、好友信息到Excel		



【温馨提示】

		1. 第一次使用时需要输入您的人人网个人账户名密码，之后会保存到
		   \tmp\config目录下，再次使用时，回车跳过账户名和密码即可。
		2. 保存的所有好友大图位于\tmp\photo目录。
		3. 保存的好友Excel表格位于\tmp目录下。
		4. 程序运行时，如删除tmp文件夹可能会无法运行，
		   故请保留tmp目录。

		本程序绝无任何盗取您个人隐私等行为，还请放心使用，有清纯的程序
		源码作证~~
		使用后可通过目录下的“清空程序下载的文件.bat”来清空
		保存的密码、好用图片等。

【软件实现】
		本程序利用python实现，如已安装下方所提到的库，则可直接运行python版
		否则，可运行exe版（py2exe转换为.exe可执行程序），无需安装python及各种库。

		额外用到的python库有（非python自带）：

		requests 	： 网页http协议交互库
		PIL		： 图片处理库
		xlrd		： Excel表格读取库
		xlwt		： Excel表格写入库
		py2exe		： python程序打包为exe软件		


【下载地址】
		
		本程序可以两种版本运行，exe版无需安装各种库，而python则需要安装上面
		所地道的各种库和python软件。

		exe版下载地址：http://pan.baidu.com/s/1pJqLOiZ
		python源码地址：https://github.com/changyeyu/WebSpider

【版权声明】	
		fish @ 深圳
		2014/10/19

