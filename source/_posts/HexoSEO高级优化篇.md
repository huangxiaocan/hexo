---
title: HexoSEO高级优化篇
tags:
  - Hexo
  - SEO
categories: hexo
description: 个人对HEXO搭建博客的SEO优化方案进行总结，从本地的文章结构到定期推送，再到SEO关键词优化做一个全面体系的汇总，如果有更好的方法可以私聊我
abbrlink: ba81
date: 2019-07-05 21:37:26
---
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



