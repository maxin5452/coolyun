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
import urllib2;
import re;
from BeautifulSoup import BeautifulSoup;
import web
import shutil

#------------------------------------------------------------------------------
page_num =0
page =1
def makeDIR(mother_path,dir_name):

    dir_name=os.path.join(mother_path, dir_name)#新建网站文件夹
    if not os.path.isdir(dir_name):
          os.makedirs(dir_name)
    return dir_name

def get(region,site_path,url_path,page):   

     doc = open(site_path, 'r')
     soup = BeautifulSoup(doc)
     #print soup
     #<span class="col-gray">
     Link = re.findall('<span class="col-gray">(.*?)</span>', str(soup));
     Rank = re.findall('<strong class="col-red02">(.*?)</strong>', str(soup));

     addr_file_name=region+"_"+str(page)+"_Top_URL.txt"
     file_path=os.path.join(url_path,addr_file_name)
     addr_file = open(file_path,"a")
     
     if Link:
         for i in range(1,len(Link)):
             #print "website:",Link[i],"\trank:",Rank[i-1];
             addr_file.write(Rank[i-1]+'\t'+Link[i]+'\n')
                          

     addr_file.close( )
             
def find_link(region,site_path,size=1):
    global page_num
    global page
    if os.path.isfile(site_path):
        if not "err_log" in site_path and not "database" in site_path:
                print site_path
                url_path=makeDIR(region,"url") #新建保存目录
                get(region,site_path,url_path,page)
                page_num=page_num+1          
                if page_num% int(size) == 0 :#保存的文件分片，每读取size个页面就新建一个文本文件,同时把旧文件复制到工作目录上
                    addr_file_name=region+"_"+str(page)+"_Top_URL.txt"
                    src_path=os.path.join(url_path,addr_file_name)
                    dst_path=makeDIR(region,str(page))
                    dst_path=makeDIR(dst_path,"url")
                    dst_path=os.path.join(dst_path,addr_file_name)
                    shutil.copyfile(src_path, dst_path) 
                    page=page+1
                 
    elif os.path.isdir(site_path):  
        for s in os.listdir(site_path):
            newDir=os.path.join(site_path,s)
            find_link(region,newDir,size)
     

 ###############################################################################
if __name__=="__main__":
    region=raw_input("请输入爬虫工作区域:");
    site_path=makeDIR(region,"site") #新建保存目录
    #get(region,url_path,timestamp)
    size=raw_input("请输入分片大小:");
    find_link(region,site_path,size)
    
    
    

 

