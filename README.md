# Task-of-Social-Network-Analysis

BUPT 2019-2020 社会网络分析与算法研究 大作业

# 项目说明

**微博爬虫** 可爬取个人信息 关注列表 粉丝列表 微博及其相关信息

**python画图程序** 绘制分布图像

# 使用方法

## 环境准备

本项目Python版本为Python3.6.8

IDE：Pycharm 画图软件：Gephi

需要MongoDB数据库，可视化软件可选NoSQL，同时便于导出数据

python库：selenium Scrapy pymongo Pillow lxml pylab pandas

**注：**
使用Pycharm需要额外下载mongodb可视化插件，最新版本Pycharm可能不兼容可视化插件

Pycharm可能不兼容pip安装的库 需要在软件内重新下载  ~~记得换豆瓣源~~

Scrapy库需要C++ build tools框架支持

Gephi需要Java8框架支持

## 替换Cookie
Chrome/Firefox浏览器打开开发者模式

访问 https://weibo.cn/ 并登录

在Netwok中找到weibo.cn标签 右侧找到cookie 注意关闭ADBlock等插件和油猴脚本

**将cookie粘贴至setting.py相关位置**

***如果爬虫报错403/302，说明账号被封/cookie失效，请重新替换cookie***

## 运行程序

用Pycharm打开sina工程文件夹

在sina/spider/weibo_spider.py中 点击运行按钮（绿色三角）


