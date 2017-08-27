# !/user/bin/python
# coding: utf-8
# file: GetLink.py
#
import time #引入时间模块
import os  #新建文件夹要用到的模块
import urllib2;
import math
import web4

def have_a_rest(start_time,end_time ):
        now_time = time.strftime("%H:%M:%S", time.localtime())
        
        while(now_time>=start_time or now_time < end_time):
                time.sleep(60);
                now_time = time.strftime("%H:%M:%S", time.localtime())
                print now_time+" I am sleeping now~ ~"
                
                
        print now_time+":It's time to work now!"
        
def find_link(region,zone,url_dir):
    if os.path.isfile(url_dir):
                if url_dir.endswith('Top_URL.txt') :
                        print url_dir
                        
                        #找到链接文件中的每个链接，并以此为种子地址，自动开始下载
                        for line in open(url_dir):
                                try:
                                        line_content=line.strip('\n')
                                        rank,userUrl=line_content.split('\t')
                                        
                                        have_a_rest("23:00:00","06:00:00")
                                        print "Zone "+zone+":No.",rank," website is downloading: ",userUrl
                                        #result='''
                                        dir_name="more_sites"
                                        save_path=web4.makeDIR(region,zone)
                                        save_path=web4.makeDIR(save_path,dir_name)
                                        #设定网站爬取的深度,排名越靠前，爬取的深度越深
                                        rank=int(rank)
                                        depth=1
                                        
                                        dir_path,myUrl,filestamp=web4.saveHTM(region,zone,save_path,userUrl,rank,depth)#储存网页
                                        if dir_path!='Error':
                                            #爬取成功！延时1秒之后继续爬取
                                            print  "please wait for 1 seconds"
                                            time.sleep(1);
                                            
                                        else:
                                            print dir_path,myUrl,filestamp
                                        #'''
                                except  Exception,e:
                                        print 'Error',str(e);
                                         #创建错误日志路径
                                        error_path = web4.makeDIR(region,zone)
                                        error_path = web4.makeDIR(error_path,"url")
                                        error_path= os.path.join(error_path,'get_start_site_ErrorLog.txt');
                                        ErrorLog = open(error_path, 'a')#追加出现的各种错误
                                        ErrorLog.write(line_content+'\tError:\t'+str(e));
                                        ErrorLog.close( );
                                        
                                
                   
    elif os.path.isdir(url_dir):  
        for s in os.listdir(url_dir):
            newDir=os.path.join(url_dir,s)
            find_link(region,zone,newDir)


    
    
#print now_time
if __name__ == '__main__':
     while True :
                region=raw_input("请输入爬虫工作区域:")
                zone= raw_input("请输入爬虫工作分区:");#zone为同一个region下面的分区，方便开启多进程同时下载
                url_dir=web4.makeDIR(region,zone)
                url_dir=web4.makeDIR(url_dir,"url")
                #遍历链接文件所在目录，逐个寻找链接文件并访问
                find_link(region,zone,url_dir)
     print "所有网站处理完毕"
               
                
    






