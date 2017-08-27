# !/user/bin/python
# coding: utf-8
# file: GetLink.py
#
import time #引入时间模块
import os  #新建文件夹要用到的模块
import urllib2;
from BeautifulSoup import BeautifulSoup           # HTML
#from BeautifulSoup import BeautifulStoneSoup      # XML
#import BeautifulSoup                              # ALL

def today_dir(path):#新建当日目录
    
    now_time= time.strftime('%Y%m%d',time.localtime(time.time()))
    #path = "site/" #当前路径
    new_dir =now_time #新文件夹名称
    new_path = os.path.join(path, new_dir)
    if not os.path.isdir(new_path):
        os.makedirs(new_path)
    return new_path

def makeDIR(mother_path,dir_name):

    dir_name=os.path.join(mother_path, dir_name)#新建网站文件夹
    if not os.path.isdir(dir_name):
          os.makedirs(dir_name)
    return dir_name

def saveDATA(region,file_name,userUrl):#将网站相关信息更新到数据库

    #os.path.exists
    save_path=os.path.join(region,"site")
    data_file=os.path.join(save_path,region+"_database.txt")
    database = open(data_file,"a")        
    database.write(file_name+"\t"+userUrl+'\n')
    database.close()

#saveHTM: 从远程下载网页到本地
def saveHTM(region,save_path,userUrl,user_agent='cloud1602'):
    today_save_path=today_dir(save_path)#在site目录下新建当日目录
    print 'Downloading:',userUrl
    headers ={'User-agent': user_agent}
    request = urllib2.Request(userUrl,headers=headers)
    #创建错误日志路径
    error_path = makeDIR(save_path,"err_log")
    error_path= os.path.join(error_path,'saveHTM_ErrorLog.txt');
    ErrorLog = open(error_path, 'a')#追加记录爬取中的各种错误
    try:
                resp = urllib2.urlopen(request, timeout=20);
                respHtml = resp.read();
                # BeautifulSoup 接受一个字符串参数
                #soup = BeautifulSoup(respHtml)
                soup = BeautifulSoup(respHtml,fromEncoding="gb18030")        
                
                file_stamp= region+"_"+time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
                file_name=os.path.join(today_save_path,file_stamp+".txt")
                file = open(file_name,"w")
                file.write(str(soup))
                file.close()
                 
    except urllib2.URLError, e :
                print "Download error:", e.reason
                ErrorLog.write(userUrl+'\t'+"Download error:"+str(e)+'\n')
                ErrorLog.close( )
                return 'Error','Error',str(e.reason)
    except Exception,e2:
                print 'Error',e2
                ErrorLog.write(userUrl+'\t'+"Other error:"+str(e2)+'\n')
                ErrorLog.close( )
                return 'Error','Error',str(e2)
    else:                       
                print "00000"
                ErrorLog.close( )
                #将网站相关信息更新到数据库
                saveDATA(region,file_stamp,userUrl)
                return today_save_path,userUrl,file_stamp
    
#print now_time
if __name__ == '__main__':
    while True :
       region= raw_input("请输入爬虫工作目录:");
       userUrl =raw_input("请输入带http前缀的网址（退出请输quit）:");  #PS:这里应该设立两个接口，一个是从终端输入，一个是从文件读取                                                                                            
       if userUrl == "quit":
                    break
       save_path="site"
       save_path=makeDIR(region,save_path)       
       dir_path,userUrl,filestamp=saveHTM(region,save_path,userUrl)#储存网页
       if dir_path!='Error':
           print 'site ok!'
       #可以从这里写提取网站链接的代码
       print  "please wait for 5 seconds"
       time.sleep(5);
    print "所有网站处理完毕"







