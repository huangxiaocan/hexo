---
title: hexo安装教程及插件介绍
tags:
  - hexo plugin
categories: hexo
abbrlink: 7b7e
date: 2019-06-19 12:15:08
---
参考博文：[Hexo搭建技术博客使用与常见问题详细讲解](https://code.skyheng.com/post/50982.html，'一切随缘').   
hexo的使用，请参考上面的博文，今天我主要分享hexo的插件。

<!--less-->  

## 文章置顶插件  

	npm install hexo-generator-index-pin-top –save
	npm uninstall hexo-generator-index –save
参考文档：[点我](https://blog.csdn.net/qwerty200696/article/details/79010629,'文章置顶插件')
## 文章字数+阅读时长统计

	npm i –save hexo-wordcount
参考文档：[点我](https://blog.csdn.net/ganzhilin520/article/details/79048036,'文章字数+阅读时长统计')
## 百度链接主动推送

	npm install hexo-baidu-url-submit –save
参考文档：[点我](https://hui-wang.info/2016/10/23/Hexo%E6%8F%92%E4%BB%B6%E4%B9%8B%E7%99%BE%E5%BA%A6%E4%B8%BB%E5%8A%A8%E6%8F%90%E4%BA%A4%E9%93%BE%E6%8E%A5/,'百度链接主动推送')
## hexo上传至FTP服务器

	npm install hexo-deployer-ftpsync –save
参考文档：[点我](https://hexo.io/zh-cn/docs/deployment.html#FTPSync,'hexo上传至FTP服务器')
## hexo上传至腾讯云COS

	npm install hexo-deployer-cos –save
参考文档：[点我](https://github.com/sdlzhd/hexo-deployer-cos#user-content-options,'hexo上传至腾讯云COS')
## hexo上传至阿里云

	npm install hexo-deployer-aliyun –save
参考文档：[点我](https://github.com/yedaodao/hexo-deployer-aliyun,'hexo上传至阿里云')
## hexo管理插件

	npm install –save hexo-admin
参考文档：[点我](https://github.com/jaredly/hexo-admin,'hexo管理插件')
## hexo文章加密码


参考文档：[点我](https://github.com/MikeCoder/hexo-blog-encrypt/blob/master/ReadMe.zh.md,'hexo文章加密码')
## IP计数统计


参考文档：[点我](https://www.jianshu.com/p/8a8f880f40c0,'IP计数统计')
## Valine评论

	npm install leancloud-storage –save
参考文档：[点我](https://valine.js.org/quickstart.html#npm,'Valine评论')
## Valine评论提醒   

参考文档：[点我](http://www.zhaojun.im/hexo-valine-admin/,'Valine评论提醒')

## 优化链接
在 Hexo 博客根目录，执行 

	npm install hexo-abbrlink --save

在 _config.yml 配置文件写入

	# abbrlink config
	abbrlink:
	  alg: crc16 #support crc16(default) and crc32
	  rep: hex    #support dec(default) and hex
	
	# 更改 permalink 值
	permalink: p/:abbrlink.html 
## 手动设置文章概要

	npm install --save hexo-less

举例说吧，我想让这篇文章在主页列表中，只显示一张美图

	---
	title: 推荐两个 Hexo 插件：短地址与封面模式
	date: 2018-08-07 20:29:12
	categories: 网站建设
	tags: Hexo
	---
	
	![封面](http://xxxxx.jpeg)
	
	<!--less-->

## 萌妹子添加

	npm install --save hexo-helper-live2d

在站点的 _config.yml 下配置

	live2d:
    enable: true
    scriptFrom: local
    model:
    use: live2d-widget-model-wanko
    display:
    position: right
    width: 150
    height: 300
    mobile:
    show: true
## 网站运行时间添加
实时展示你的博客已经运行了多长时间了，我还是蛮喜欢这个功能的，随着时间的增长，和你的博客访问量形成照样，成就感也会增添不少。  
在 hexo/themes/[your theme]/layout 文件夹下找到你的 footer 文件，即脚布局文件，在对应的位置添加一下代码。

    <span id="timeDate">载入天数...</span><span id="times">载入时分秒...</span>
    <script>
    var now = new Date(); 
    function createtime() { 
        var grt= new Date("02/14/2018 12:49:00");//此处修改你的建站时间或者网站上线时间 
        now.setTime(now.getTime()+250); 
        days = (now - grt ) / 1000 / 60 / 60 / 24; dnum = Math.floor(days); 
        hours = (now - grt ) / 1000 / 60 / 60 - (24 * dnum); hnum = Math.floor(hours); 
        if(String(hnum).length ==1 ){hnum = "0" + hnum;} minutes = (now - grt ) / 1000 /60 - (24 * 60 * dnum) - (60 * hnum); 
        mnum = Math.floor(minutes); if(String(mnum).length ==1 ){mnum = "0" + mnum;} 
        seconds = (now - grt ) / 1000 - (24 * 60 * 60 * dnum) - (60 * 60 * hnum) - (60 * mnum); 
        snum = Math.round(seconds); if(String(snum).length ==1 ){snum = "0" + snum;} 
        document.getElementById("timeDate").innerHTML = "本站已安全运行 "+dnum+" 天 "; 
        document.getElementById("times").innerHTML = hnum + " 小时 " + mnum + " 分 " + snum + " 秒"; 
    } 
    setInterval("createtime()",250);
    </script>


参考博客：
[hexo 博客小功能添加-评论、萌妹纸、相册、字数统计...](https://blog.csdn.net/qq_22656383/article/details/79393146,'')