# !/user/bin/python
# coding: utf-8
# file: GetLink.py
#
import time #引入时间模块
import os  #新建文件夹要用到的模块
import shutil
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



def get(filename,userUrl,rank,sec=5):
        #filename:URL文件名称，userUrl:待爬取的网址，sec:间隔数
        
        #创建网页的保存路径
        region,zone,timestamp,depth,postex=filename.split('_',4)
        site_path=os.path.join(region,zone)
        site_path=os.path.join(site_path,"more_sites")
        if not os.path.isdir(site_path):
                os.makedirs(site_path)


        #下载爬取的网页
        preex,userUrl=userUrl.split("://",1)
        dir_path,myUrl,filestamp=web4.saveHTM(region,zone,site_path,userUrl,rank,depth,1)#储存网页
        if dir_path!='Error':
                #爬取成功！延时1秒之后继续爬取                
                print  "please wait for "+sec+" seconds"
                sec=float(sec)
                time.sleep(sec);
        else:
                print dir_path,myUrl,filestamp

        


def move_url_file(filename):
        #还原URL文件路径
        region,zone,timestamp,depth,postex=filename.split('_',4)
        url_file_name=filename+".txt"
        url_path=os.path.join(region,zone)
        url_path=os.path.join(url_path,"more_urls")
        dateDir=timestamp[0:8]
        url_path=os.path.join(url_path,dateDir)        
        src_path=os.path.join(url_path,url_file_name)
        dst_path=web4.makeDIR(url_path,"done")
        dst_path=os.path.join(dst_path,url_file_name)

        shutil.move(src_path, dst_path)
              
        print "Now put file "+filename +" into Done directory..."
        
        
        
def find_link(region,url_dir,timestamp,sec):#遍历链接文件所在目录，逐个寻找链接文件并访问

        finish="yes"#下载链接的完成标志，初始默认为yes

        #创建错误日志路径
        error_path = web4.makeDIR(url_dir,"err_log")
        error_path= os.path.join(error_path,'file_web_ErrorLog.txt');
        ErrorLog = open(error_path, 'a')#追加记录爬取中的各种错误

        
        for s in os.listdir(url_dir):
            thisDir=os.path.join(url_dir,s)
            if "done" in thisDir or "err_log" in thisDir:
                #如果遍历遇到err_log目录或done目录则略过
                continue;
            elif thisDir.endswith('URL.txt'):
                #如果碰到链接文件，则读取并下载里面的链接
                print thisDir
                finish="no"
                path,filename=os.path.split(thisDir)#分离路径和文件名
                filename,filetype=os.path.splitext(filename)#分离文件名和扩展名
                        
                #找到链接文件中的每个链接，并以此为种子地址，自动开始下载
                for line in open(thisDir):
                        try:
                                line=line.strip('\n')
                                #print line+","
                                userUrl,fromUrl,rank=line.split('\t',2)                                
                                if not userUrl.startswith('http'):
                                        continue
                                have_a_rest("23:00:00","06:00:00")   #夜间停止下载                             
                                get(filename,userUrl,rank,sec)
                        except  Exception,e:
                                print 'Error',str(e);
                                ErrorLog.write(line+'\t'+'Error:'+'\t'+str(e))
                print "Links in file "+filename +" are done!"
                #将已遍历完的URL文件放进同一层的done目录下
                move_url_file(filename)

        ErrorLog.close()
        return finish
                                
                                

    
    
#print now_time
if __name__ == '__main__':
     while True :
             region=raw_input("请输入爬虫分布的区域:");
             zone=raw_input("请输入爬虫工作的目录:");
             timestamp=raw_input("please input the date name( 20170810 e.g)");
             sec=raw_input("please input the time between 2 visits:");
             
             url_path=web4.makeDIR(region,zone)
             url_path=web4.makeDIR(url_path,"more_urls") #在more_url子目录下进行寻找
             url_path=web4.makeDIR(url_path,timestamp)
                
             #遍历链接文件所在目录，逐个寻找链接文件并访问
             find_link(region,url_path,timestamp,sec)
     print "所有网站处理完毕"
               
                
    






