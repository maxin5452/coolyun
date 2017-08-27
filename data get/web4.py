# !/user/bin/python
# coding: utf-8
# file: GetLink.py
#
import time #引入时间模块
import os  #新建文件夹要用到的模块
import urllib2;
import codecs
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

def saveDATA(file_stamp,userUrl,rank):#将网站相关信息更新到数据库

    #os.path.exists
    region,zone,timestamp,depth=file_stamp.split('_',3)
    save_path=os.path.join(region,zone)
    save_path=makeDIR(save_path,"database")
    dateDir= timestamp[0:8]
    data_file = os.path.join(save_path,region+"_"+zone+"_"+dateDir+"_database.txt")
    database = open(data_file,"a")        
    database.write(file_stamp+"\t"+str(rank)+"\t"+userUrl+'\t'+region+'\n')
    database.close()

#saveHTM: 从远程下载网页到本地
def saveHTM(region,zone,save_path,userUrl,rank,depth=1,num_retries=1,user_agent='cloud1602'):
    #region:爬取的主题目录，如alltype,sports,financial等等，zone,同一主题下爬取的区域，1，2，3，4，方便多进程同时爬取
    #save_path:爬取网页的保存路径，saveUrl:爬取网页的网址，num_retries:如果失败重试爬取的次数，user_agent:代理名称
    #depth:爬取的深度，最高是3，从上往下依次递减
    today_save_path=today_dir(save_path)#在site目录下新建当日目录
    print 'Downloading:',userUrl
    headers ={'User-agent': user_agent}
    request = urllib2.Request("http://"+userUrl,headers=headers)
    #创建错误日志路径
    error_path = makeDIR(save_path,"err_log")
    error_path= os.path.join(error_path,'saveHTM_ErrorLog.txt');
    ErrorLog = open(error_path, 'a')#追加记录爬取中的各种错误
    #创建描述日志
    desc_path = makeDIR(save_path,"desc_log")
    desc_file= region+"_"+zone+"_"+time.strftime('%Y%m%d',time.localtime(time.time()))+"_DESC.txt"
    desc_path= os.path.join(desc_path,desc_file);
    DescLog = codecs.open(desc_path,'a',"utf-8") #追加记录网站的描述信息
    
    try:
                resp = urllib2.urlopen(request, timeout=7);
                respHtml = resp.read();
                # BeautifulSoup 接受一个字符串参数
                #soup = BeautifulSoup(respHtml)
                soup = BeautifulSoup(respHtml,fromEncoding="gb18030")        
                
                file_stamp= region+"_"+zone+"_"+time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+"_"+str(depth)
                file_name=os.path.join(today_save_path,file_stamp+".txt")
                file = open(file_name,"w")
                file.write(str(soup))
                file.close()

                #以下代码提取网站题目及关键字
                try:
                    DescLog.write("#maxin5452#\t"+file_stamp+"\t"+userUrl+"\t"+region+"\t"+str(rank)+"\n")
                    #获取网站标题
                    #title= soup.title.string
                    title= soup.find('title')
                    if title== None:
                        print title
                        DescLog.write("title\tNone\n")
                    else:
                        print title.string
                        DescLog.write("title\t"+title.string+"\n")
                    
                    #获取网站关键字及描述
                    keywords=soup.find('meta',attrs={"name":"keywords"})
                    if keywords == None: 
                        keywords=soup.find('meta',attrs={"name":"Keywords"})
                    if keywords == None:
                        print keywords
                        DescLog.write("keywords\tNone\n")
                    else:
                        print keywords.get('content')
                        DescLog.write("keywords\t"+keywords.get('content')+"\n")
                    description=soup.find('meta',attrs={"name":"description"})
                    if description == None: 
                        description=soup.find('meta',attrs={"name":"Description"})
                    if description == None:
                        print description
                        DescLog.write("description\tNone\n")
                    else:
                        print description.get('content')
                        DescLog.write("description\t"+description.get('content')+"\n")
                    #Keywords
                except Exception,e:
                    print 'Error',str(e)
                    #des =raw_input("find an error...Continue or not?(y/n)")
                    ErrorLog.write(userUrl+'\t'+"Descrption error:"+str(e)+'\n')
                finally:
                    DescLog.close( )             
    except urllib2.URLError, e :
                print "Download error:", e.reason
                if num_retries >0:
                    print "Trying again..."
                    userUrl="www."+userUrl
                    save_path,userUrl,file_stamp= \
                    saveHTM(region,zone,save_path,userUrl,rank,depth,num_retries-1)
                    return save_path,userUrl,file_stamp
                else:
                    ErrorLog.write(userUrl+'\t'+"Download error:"+str(e)+'\n')
                    ErrorLog.close( )
                    return 'Error','Error',str(e.reason)
    except Exception,e2:
                print 'Error',e2
                if num_retries >0:
                    print "Trying again..."
                    userUrl="www."+userUrl
                    save_path,userUrl,file_stamp= \
                    saveHTM(region,zone,save_path,userUrl,rank,depth,num_retries-1)
                    return save_path,userUrl,file_stamp
                else:
                    ErrorLog.write(userUrl+'\t'+"Other error:"+str(e2)+'\n')
                    ErrorLog.close( )
                    return 'Error','Error',str(e2)
    else:                       
                print "00000"
                ErrorLog.close( )
                #将网站相关信息更新到数据库
                saveDATA(file_stamp,userUrl,rank)
                return save_path,userUrl,file_stamp
    
#print now_time
if __name__ == '__main__':
    while True :
       region=raw_input("请输入爬虫工作区域:")
       zone= raw_input("请输入爬虫工作目录:");
       userUrl =raw_input("请输入不带http前缀的网址（退出请输quit）:");  #PS:这里应该设立两个接口，一个是从终端输入，一个是从文件读取                                                                                            
       if userUrl == "quit":
                    break
       save_path="more_sites"
       save_zone=makeDIR(region,zone)                      
       save_path=makeDIR(save_zone,save_path)
       rank=2
       dir_path,userUrl,filestamp=saveHTM(region,zone,save_path,userUrl,rank,1)#储存网页
       if dir_path!='Error':
           print 'site ok!'
       #可以从这里写提取网站链接的代码
       print  "please wait for 5 seconds"
       time.sleep(5);
    print "所有网站处理完毕"







