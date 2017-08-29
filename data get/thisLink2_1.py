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
import urlparse;#创建绝对路径所需要的模块
import re;
from BeautifulSoup import BeautifulSoup;


#------------------------------------------------------------------------------

def makeDIR(mother_path,dir_name):

    dir_name=os.path.join(mother_path, dir_name)#新建网站文件夹
    if not os.path.isdir(dir_name):
          os.makedirs(dir_name)
    return dir_name
def move_file(site_path,site_dir):
    #链接提取完毕后，将网页源文件移至done目录，以做标识
    src=site_path
    dst=os.path.join(site_dir,"done")
    if not os.path.isdir(dst):
        os.makedirs(dst)
    shutil.move(src, dst)

def MainCore(Userurl):
    
        #主要功能是去除网址头及尾部不必要的标签
        #去掉http头
        mainUrl=Userurl
        if "://" in mainUrl:
            url=UserUrl.split('://',1)
            mainUrl=url[1]
            
        if mainUrl.endswith('/'):
            mainUrl=mainUrl[0:-1];
            
        if mainUrl.startswith('www.'):
            m_url = mainUrl.split('.',1)
            mainUrl=m_url[1] 
          
        return mainUrl

#get:在已下载网页上提取链接
def get(filename,rank,Userurl):#filename:例如，alltype_2_20170805000011_1,
     #depth,爬取的深度，最高是2，从上往下依次递减
     region,zone,timestamp,depth=filename.split('_',3)
     #如果爬取已达最大深度，则停止爬取
     if depth=='0':
         print 'alreay go to the set buttom of the site.'
         return 'Done','alreay go to the set buttom of the site.'
     else:
         #否则，开始爬取网页上的链接
         #获取源文件路径
         dateDir=timestamp[0:8]
         site_path=os.path.join(region,zone)
         site_path=os.path.join(site_path,"more_sites")
         site_dir=os.path.join(site_path,dateDir)
         site_path=os.path.join(site_dir,filename+".txt")

         #创建URL文件路径
         depth=int(depth)-1#每爬取一遍链接，网站的爬取深度就减一
         #深度是0的URL文件仍然可以爬取里面的网站，但是深度是1的site文件就不用爬取自身的链接了
         url_file_name=region+"_"+zone+"_"+timestamp+"_"+str(depth)+"_URL.txt"     
         url_path=os.path.join(region,zone)
         url_path=os.path.join(url_path,"more_urls")
         url_dir=os.path.join(url_path,dateDir)
         if not os.path.isdir(url_dir):
             os.makedirs(url_dir)
         url_path=os.path.join(url_dir,url_file_name)

         #创建URL提取记录，记录所有的a标签，以备以后分析
         urllog_name='ThisLink_urlLog.txt'
         urllog_path=os.path.join(region,zone)
         urllog_path=os.path.join(urllog_path,"more_urls")
         urllog_path=os.path.join(urllog_path,dateDir)
         urllog_path=os.path.join(urllog_path,"err_log")
         if not os.path.isdir(urllog_path):
            os.makedirs(urllog_path)
         urllog_path=os.path.join(urllog_path,urllog_name)


         #创建错误日志路径
         errlog_name='ThisLink_ErrorLog.txt'
         errlog_path=os.path.join(region,zone)
         errlog_path=os.path.join(errlog_path,"more_urls")
         errlog_path=os.path.join(errlog_path,dateDir)
         errlog_path=os.path.join(errlog_path,"err_log")
         if not os.path.isdir(errlog_path):
            os.makedirs(errlog_path)
         errlog_path=os.path.join(errlog_path,errlog_name)


         try:#提取链接的核心代码
             site_file= open(site_path, 'r')#读取源文件
             url_file=open(url_path,'w')#记录链接
             errlog_file=open(errlog_path,'a')#记录异常
             urllog_file=open(urllog_path,'a')#记录url 
             
             soup = BeautifulSoup(site_file)
             #print soup
             i=1
             for link in soup.findAll('a',href=True):#寻找网页上的链接
                 try:#把所有的链接都记下来，以便分析
                     urllog_file.write(filename+'\t'+Userurl+'\t'+link['href']+'\n')
                 except Exception,e:
                     print 'Error',str(e);
                 finally:

                     #处理相对链接
                     if not link['href'].startswith('http'):
                         new_link=urlparse.urljoin("http://"+Userurl,link['href'])
                         url_file.write(new_link+"\t"+Userurl+"\t"+rank+'\n')
                     else:#处理绝对链接
                         if type(link.string)!= type(None):
                             try:
                                 if MainCore(Userurl) in link['href']:#如果是它的子站，则收录；否则放弃。
                                     url_file.write(link['href']+"\t"+Userurl+"\t"+rank+'\n')
                                 else:
                                     print link['href']+" not in " + Userurl + "?"
                                 
                                 
                             except Exception,e:
                                 print 'Error',str(e)
                                 errlog_file.write(filename+'\t'+str(e)+'\n')
                             finally:
                                 i=i+1                             
                         
         except Exception,e:
                    site_file.close()
                    url_file.close()
                    errlog_file.close()
                    urllog_file.close()
                    print 'Error',str(e)
                    return 'Error',str(e)
         else:
                    site_file.close()
                    url_file.close()
                    errlog_file.close()
                    urllog_file.close()
                    print "000000"
                    return url_dir,url_file_name
         
         
            

            
def find_file(region,zone,timestamp):
    #这个函数两个作用：1.是检查database里有没有尚未提取链接的网站，如果没有了，就可以收工了；2.如果有
    #尚未提取链接的网站，提取之。

    file_name=region+"_"+zone+"_"+timestamp+"_database.txt"
    database=os.path.join(region,zone)
    databaseDir=os.path.join(database,"database")
    database=os.path.join(databaseDir,file_name)

     #创建错误日志路径
    error_path = makeDIR(databaseDir,"err_log")
    error_path= os.path.join(error_path,'thisLink_ErrorLog.txt');
    ErrorLog = open(error_path, 'a')#追加记录爬取中的各种错误
    
    f= open(database, 'r+')#读取源文件
    flist=f.readlines( )
    i=0
    over="yes"#标记整体流程是否完毕
    count=1#count统计修改次数
    for i in range(0,len(flist)):
        try:
            line=flist[i].strip()
            if "done" in line:#如果已经提取该网站了，就略过
                continue
            
            if count%100==0:#如果修改的记录超过100条，就统一读写一次
                f.close()
                f=open(database,'w+')
                f.writelines(flist)
                
            filename,rank,Userurl,filetype=line.split('\t',3)
            if filename.endswith("0"):#已经到达末端的底层网页，标记一下即可
                    line=line+"\tdone\n"
                    flist[i]=line
                    print line
                    count =count+1
                    continue
            else:#还未到达底层网页，需要提取页面上的链接
                    get(filename,rank,Userurl)#提取页面上的链接
                    line=line+"\tdone\n"  #标记本行处理完毕
                    flist[i]=line
                    print line
                    count =count+1
                    over="no" #又提取了新一轮链接、有新网站没有处理，说明整体流程还没有完成，所以标记为over=no
        except Exception,e:
             print 'Error',str(e);
             ErrorLog.write(line+'\t'+'Error:'+'\t'+str(e)+'\n');
             
                
                
    f.close( )   
    f=open(database,'w+')    
    f.writelines(flist)    
    f.close( )
    ErrorLog.close( )
    return over
    
                
 
     

 ###############################################################################
if __name__=="__main__":
    region=raw_input("请输入爬虫分布的区域:");
    zone=raw_input("请输入爬虫工作的目录:");
    timestamp=raw_input("Please input the timestamp(20170809 eg.:")
    over=find_file(region,zone,timestamp)
    if over=="yes":
        print "all links are distracted!"
    else:
        print "There are still some websites need to download"
    
    
    

 

