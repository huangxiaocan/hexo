---
title: hexo-seo-高级-优化篇
tags:
  - Hexo
  - SEO
categories: hexo
description: 个人对HEXO搭建博客的SEO优化方案进行总结，从本地的文章结构到定期推送，再到SEO关键词优化做一个全面体系的汇总，如果有更好的方法可以私聊我
abbrlink: ba81
date: 2019-07-05 21:37:26
---
文章出处：https://blog.csdn.net/lzy98/article/details/81140704  
## 本地文章优化
首先给你的文章生成sitemap文件

	cnpm install hexo-generator-sitemap --save #sitemap.xml适合提交给谷歌搜素引擎
	cnpm install hexo-generator-baidu-sitemap --save #baidusitemap.xml适合提交百度搜索引擎

如果执行命令出现以下问题

	You must install peer dependencies yourself

说明npm 版本太低，更新npm版本即可

	npm install -g npm	

然后在站点配置文件_config.yml中添加以下代码

	# 自动生成sitemap
	sitemap:
	   path: sitemap.xml
    baidusitemap:
	   path: baidusitemap.xml

最后修改站点配置文件_config.yml

	# URL
	## If your site is put in a subdirectory, set url as 'http://yoursite.com/child' and root as '/child/'
	url: http://你的网站

每次hexo g后都会在/public目录下生成sitemap.xml和baidusitemap.xml，这就是你的站点地图。

## 优化结构

seo搜索引擎优化认为，网站的最佳结构是用户从首页点击三次就可以到达任何一个页面，但是我们使用hexo编译的站点打开文章的url是：sitename/year/mounth/day/title四层的结构，这样的url结构很不利于seo，爬虫就会经常爬不到我们的文章，于是，我们可以将url直接改成sitename/title的形式，并且title最好是用英文，在根目录的配置文件下修改permalink如下：

	url: http://你的网站
	root: /
	permalink: :title.html
	permalink_defaults:

## 首页标题优化

### 安装nofollow插件  
减少出站链接能够有效防止权重分散，hexo有很方便的自动为出站链接添加nofollow的插件

	npm install hexo-autonofollow --save

该插件会将博客中的出站链接自动加上nofollow属性，例外请在站点配置文件_config.xml中添加如下字段

	nofollow:
    enable: true
    exclude:
    - www.boyumanong.top
    - 友链地址 

这样，例外的链接将不会被加上nofollow属性。

### robots.txt文件
在source文件夹中新建文件robots.txt，可以参考我的

	User-agent: * Allow: /
	Allow: /archives/
	Disallow: /vendors/
	Disallow: /categories/


	Sitemap: http://www.boyumanong.top/sitemap.xml
	Sitemap: http://www.boyumanong.top/baidusitemap.xml

## 开启SEO优化选项

## 开启压缩文件
因为hexo生成的文件是静态html，里面占用了大量的空白符。使用gulp进行压缩接口提高访问速度并且降低内存。

使用命令

	npm install gulp -g
	npm install gulp-minify-css gulp-uglify gulp-htmlmin gulp-htmlclean gulp --save
	npm install gulp-concat
	npm install gulp-imagemin

在hexo blog文件夹下创建gulpfile.js:

	var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    cssmin = require('gulp-minify-css'),
    imagemin = require('gulp-imagemin'),
    htmlmin = require('gulp-htmlmin'),
    htmlclean = require('gulp-htmlclean');
    concat = require('gulp-concat');
	//JS压缩
	gulp.task('uglify', function() {
    return gulp.src(['./public/js/**/.js','!./public/js/**/*min.js'])//只是排除min.js文件还是不严谨，一般不会有问题，根据自己博客的修改我的修改为return gulp.src(['./public/**/*.js','!./public/zuoxi/**/*.js',,'!./public/radio/**/*.js'])
        .pipe(uglify())
        .pipe(gulp.dest('./public/js'));//对应修改为./public即可
	});
	//public-fancybox-js压缩
	gulp.task('fancybox:js', function() {
    return gulp.src('./public/vendors/fancybox/source/jquery.fancybox.js')
        .pipe(uglify())
        .pipe(gulp.dest('./public/vendors/fancybox/source/'));
	});
	// 合并 JS
	gulp.task('jsall', function () {
    return gulp.src('./public/**/*.js')
    // 压缩后重命名
        .pipe(concat('app.js'))
        .pipe(gulp.dest('./public'));
	});
	//public-fancybox-css压缩
	gulp.task('fancybox:css', function() {
    return gulp.src('./public/vendors/fancybox/source/jquery.fancybox.css')
        .pipe(cssmin())
        .pipe(gulp.dest('./public/vendors/fancybox/source/'));
	});
	//CSS压缩
	gulp.task('cssmin', function() {
    return gulp.src(['./public/css/main.css','!./public/css/*min.css'])   
        .pipe(cssmin())
        .pipe(gulp.dest('./public/css/'));
	});
	//图片压缩
	gulp.task('images', function() {
    gulp.src('./public/uploads/*.*')
        .pipe(imagemin({
            progressive: false
        }))
        .pipe(gulp.dest('./public/uploads/'));
	});
	// 压缩 public 目录 html文件 public/**/*.hmtl 表示public下所有文件夹中html，包括当前目录
    gulp.task('minify-html', function() {
      return gulp.src('./public/**/*.html')
        .pipe(htmlclean())
        .pipe(htmlmin({
             removeComments: true,
             minifyJS: true,
             minifyCSS: true,
             minifyURLs: true,
        }))
        .pipe(gulp.dest('./public'))
    });
	gulp.task('build', ['uglify', 'cssmin', 'fancybox:js', 'fancybox:css', 'jsall','images']);

在根目录下的package.json文件中生成写入scripts:

	"scripts":{
	"build":"hexo clean && hexo g && gulp build"},

这样每次输入npm run build就会自动清理上次生成的文件，然后生成新的文件，最后压缩文件。  

执行npm run build,报错如下：

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_seo_1.png)

解决办法如下，执行命令：

	gulp -v

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_seo_2.png)

版本不一致的原因，所以我们要统一版本
修改hexo根目录的文件package.json,gulp的版本如下：

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_seo_3.png)

然后执行命令：

	npm install

在执行

	gulp -v

版本已经改过来了  
继续执行npm run build,又报了另外一个错误

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_seo_4.png)

无奈，我暂时没解决掉，有会的兄弟不？留言评论，大家讨论下....

## 站内优化
这里就真正的涉及到SEO的相关知识了，对你的文章的结构，描述，关键词进行优化  
### title优化
搜索引擎在抓取网页时，最先读取的就是网页标题，所以title是否正确设置极其重要。title一般不超过80个字符，而且词语间要用英文“-”隔开，因为计算机只对英语的敏感性较高，对汉语的敏感性不高。  

	用法：<title>网站标题</title>

注意点

1，首页title写法：首页的title写法格式一般是“总标题-特别重要的关键词或者一句话含有特别重要关键词的描述”。注意这里的“-”是英文，要问我为什么呢?这个因为互联网不是我们国内开发的，汉语不是标准，计算机只对英语敏感性较高，而对汉语敏感性不太高。  

2，栏目页title写法：栏目页title的写法有两种，关键词名称命名写法是“栏目名称-总名称”，非关键词命名写法是：“栏目名称 栏目关键词-总名称”。  

3，分类列表页的title写法：用关键词为这个栏目起名，然后按照下列顺序填写便可了“分类列表页名称-栏目名称-总名称”。

注意事项：

1,每个标题应该是根据当前内容设置的独特不重复的。

2,字数限制。不能太长，要不然搜索引擎结果列表会显示不全。最好不超过 25 个中文字。最好是在 10~20 之间。

3,切勿堆砌关键词。这是很多人常犯的错误

4,关键词最好出现在最前面

5,标题有吸引力。毕竟有吸引力的标题才能让用户点击

6,连词符的使用。可以使用 |->

7,不要使用没有意义的句子

### keywords优化
主要作用是告诉搜索引擎，这个网站内容是什么。因为，好多站长在keywords堆砌关键词，所以好多搜索引擎不太重视keywords了。建议大家还是认真填写keywords，有的搜索引擎还是很重视的，由于现在词频和密度对于 SEO 影响不大，所以只要保持你的正文中出现 4~6 次关键词就可以了。千万不能堆砌关键词。

注意点：

1,首页keywords写法：首页keywords按照选定的栏目名称，在首页的keywords中加入总名称、栏目名称和一两个关键词。  

2,栏目keywords写法：栏目的keywords其栏目下所有分类列表的名称列出，加上栏目关键字，写法是“栏目名称,栏目关键字,栏目分类列表名称”

3,分类列表页keywords写法：将你这个栏目中的主要关键字写入

### Description优化

功能让搜索引擎是判断整个页面内容的，当中要写入的内容是你页面内容的简介。description一般不超过100个字符。对于个人站点而言，描述标签最好是一句通顺的句子，如果不能的话，则宁可不要。

注意点：

1,首页description写法：description的写法就是将首页的标题、关键词和一些特殊栏目的内容融合到里面，写成简单的介绍形式，不要只写关键词。

2,栏目description写法：将栏目的标题、关键字、分类列表名称，尽量的写入description中，仍是尽量写成介绍形式。

3,分类description写法：是将你这个栏目中的主要关键字写入

### H标签优化
H 标签的重要性可能是仅次与页面标签。H1->H6 的重要性依次降低

所以建议在页面的 H1 和 H2 标签中混入关键词

### 图片 ALT 文字优化
插入图片的时候会提示输入文字，这个不能敷衍。图片 ALT 文字出现的关键词对页面相关性也有一定的影响。同样的，也不要在 ALT 上堆砌关键词

### 内部链接及锚文字优化
内部链接对于爬行和收录具有很重要的意义。内部链接对页面关键词相关性也有影响，最主要的就是在内部链接中使用锚文字。

锚文字是告诉搜索引擎被链接页面主题内容的最重要依据之一。我们有时候可能无法控制外部链接的锚文字，但是对于站内的内部链接锚文字我们可以控制。不过有几点需要注意：

1，适当出现匹配关键词的锚文字

2，锚文字不能集中导航或者页尾，要分散在正文中

3，不要过度优化锚文字，要不然有可能会被搜索引擎惩罚

 









