# !/user/bin/python
# coding: utf-8
# file: GetLink.py
#
import time #引入时间模块
import os  #新建文件夹要用到的模块
import urllib2;
import math
import web

def have_a_rest(start_time,end_time ):
        now_time = time.strftime("%H:%M:%S", time.localtime())
        
        while(now_time>=start_time or now_time < end_time):
                time.sleep(60);
                now_time = time.strftime("%H:%M:%S", time.localtime())
                print now_time+" I am sleeping now~ ~"
                
                
        print now_time+":It's time to work now!"
        
def find_link(region,url_dir):
    if os.path.isfile(url_dir):
                if url_dir.endswith('Start_URL.txt'):
                        print url_dir
                        
                        #找到链接文件中的每个链接，并以此为种子地址，自动开始下载
                        for line in open(url_dir):
                                userUrl=line.strip('\n')
                                save_path="site"
                                save_path=web.makeDIR(region,save_path)       
                                dir_path,myUrl,filestamp=web.saveHTM(region,save_path,userUrl)#储存网页
                                if dir_path!='Error':
                                    print 'site ok!'
                                    print  "please wait for 5 seconds"
                                    time.sleep(5);
                                    Similar_Site(region,save_path,userUrl)
                                else:
                                    print dir_path,myUrl,filestamp

                                
                   
    elif os.path.isdir(url_dir):  
        for s in os.listdir(url_dir):
            newDir=os.path.join(url_dir,s)
            find_link(region,newDir)

def Similar_Site(region,save_path,userUrl):
    web_addr,web_type=os.path.splitext(userUrl)#分离网页名和网页后缀
    error_count=0
    for i in range(1,1842+1):
        have_a_rest("23:00:00","06:00:00")
        new_addr=web_addr+"_"+str(i)+web_type
        #new_addrhttp://search.top.chinaz.com/top.aspx?p=3&t=all
        dir_path,myUrl,filestamp=web.saveHTM(region,save_path,new_addr)#储存网页
        if dir_path!='Error':
            print 'site ok!'
        else:
            print dir_path,myUrl,filestamp
            error_count=error_count+1
            if error_count == 5 :
                break;
        print  "please wait for 5 seconds"
        time.sleep(5);
    
    
#print now_time
if __name__ == '__main__':
     while True :
                region= raw_input("请输入爬虫工作目录:");
                url_dir=web.makeDIR(region,"url")
                #遍历链接文件所在目录，逐个寻找链接文件并访问
                find_link(region,url_dir)
     print "所有网站处理完毕"
               
                
    






