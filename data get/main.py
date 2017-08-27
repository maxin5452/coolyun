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
import get_start_site
import thisLink2_1
import file_web2_1

#------------------------------------------------------------------------------
    

        
 
     

 ###############################################################################
if __name__=="__main__":

   
    region=raw_input("请输入爬虫分布的区域:");
    zone=raw_input("请输入爬虫工作的目录:");
    #zone为同一个region下面的分区，方便开启多进程同时下载
    timestamp=raw_input("Please input the timestamp(20170809 eg.) you want to do:")
    sec=raw_input("please input the time between 2 crawling:");    
    
    root_url_dir=web4.makeDIR(region,zone)
    root_url_dir=web4.makeDIR(root_url_dir,"url")
    #遍历链接文件所在目录，寻找链接文件并访问
    get_start_site.find_link(region,zone,root_url_dir)
    print "All seed webpages are done ! Now begin to download other webpages...s"
    
    while True:
        
        #根据database提取链接，database里面的timestamp和后面file_web2.1的timestamp默认为
        #一个
        over=thisLink2_1.find_file(region,zone,timestamp)
        print over
        
        #根据URL文件下载网页
        #result='''
        print "Now start the new round of crawling..."
        
            
        url_path=web4.makeDIR(region,zone)
        url_path=web4.makeDIR(url_path,"more_urls") #在more_url子目录下进行寻找
        url_path=web4.makeDIR(url_path,timestamp)
        #遍历链接文件所在目录，逐个寻找链接文件并访问
        finish=file_web2_1.find_link(region,url_path,timestamp,sec)
        #'''

        #当分区里的提取链接和文件下载都完成时，程序结束！
        if over=="yes" and finish=="yes":
            break;

    print "ALL DONE !"
    
    
    

 

