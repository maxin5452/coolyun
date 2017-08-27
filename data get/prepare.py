#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
【版本信息】
版本：     v1.0
作者：     crifan

【详细信息】
用于：
【教程】抓取网并网页中所需要的信息 之 Python版 

http://www.crifan.com/crawl_website_html_and_extract_info_using_python/

的示例代码。

-------------------------------------------------------------------------------
"""

#---------------------------------import---------------------------------------
import os;
import shutil
import urllib2;
import re;
from BeautifulSoup import BeautifulSoup;

import get_web_list
import web4
import thisLink3_0


#------------------------------------------------------------------------------
    

        
 
     

 ###############################################################################
if __name__=="__main__":

    #1.下载排行榜网页
    region=raw_input("请输入爬虫分布的领域（mil,sports...):");
    size=raw_input("请输入该领域内每个区域的大小（以页数为单位）:");
    src_dir=web4.makeDIR(region,"url");
    get_web_list.find_link(region,src_dir)
    print "The ChinaZ site already done!"
    #2.提取排行榜上的网站链接
    site_path=web4.makeDIR(region,"site") #新建保存目录    
    thisLink3_0.find_link(region,site_path,size) 

    print "该领域的所有分区已建立，请启动main.py脚本开始多进程下载！"
    
    
    

 

