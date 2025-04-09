# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 08:53:51 2021

@author: 苹果香蕉泥
"""

import os
from bs4 import BeautifulSoup
import time
from datetime import datetime

#定义了一个帖子类，方便接下来对帖子对象进行操作
class TZ:
    pass

'''
a=datetime.now()
os.system("wget -c -r -np -k -L -p -nc --no-check-certificate --reject txt,png,gif,jpg,mp4 --exclude-directories images,Out of Plan  https://sora.chat:8000/")
b=datetime.now()
print("备份站下载完成！用时"+str(b-a))
'''
NOW=os.listdir("./")
IP=[]#IP=inpath
OP=[]

for i in NOW:
    if "html" in i:
        print("")
    elif "py" in i:
        print("")
    elif "-" in i or "Out" in i:
        IP.append(i)
    else:
        OP.append(i)
        
#先对外层列表操作

f=open("./index.html","r",encoding=("utf-8"))
con=f.read()
con=con.replace('''					<tr class="file">
						<td></td>
						<td>
							<a href="https://sora.chat:8000/log.txt">
								<svg width="1.5em" height="1em" version="1.1" viewBox="0 0 265 323"><use xlink:href="#file-shortcut"></use></svg>
								<span class="name">log.txt</span>
							</a>
						</td>
						<td data-order="21">21 B</td>
						<td class="hideable"><time datetime="2020-07-26T06:46:11Z">07/26/2020 06:46:11 AM +00:00</time></td>
						<td class="hideable"></td>
					</tr>''',"")     
con=con.replace('''							<a href="index.html@sort=namedirfirst&amp;order=desc" class="icon"><svg width="1em" height=".5em" version="1.1" viewBox="0 0 12.922194 6.0358899"><use xlink:href="#up-arrow"></use></svg></a>
							<a href="index.html@sort=name&amp;order=asc">Name</a>''', '''							<a href="index.html@sort=namedirfirst&amp;order=desc" class="icon"><svg width="1em" height=".5em" version="1.1" viewBox="0 0 12.922194 6.0358899"><use xlink:href="#up-arrow"></use></svg></a>
							<a href="index.html@sort=name&amp;order=asc">帖子名字/备份日期</a>
						</th>
						<th>
						    作者
						</th>''')
con=con.replace('<a href="index.html">/</a>', '<a href="index.html">备份站根目录/</a>')
f=open("./index.html","w",encoding=("utf-8"))
f.write(con)   
f.close()

for name in OP:
    file=open("./"+name+"/index.html",encoding=("utf-8"))
    soup=BeautifulSoup(file,'lxml')
    tz=TZ()#生成一个在TZ类下的对象——tz
    
    tz.title=str(soup.title).replace("<title>","").replace("</title>","")
    #print(tz.title)
    
    tz.author=str(soup.find_all("div",id="write")[0].find_all("div",attrs={"class": "author"})[0]).replace('<div class="author">            1楼 | ',"").split()[0]
    #print(tz.author)
    
    f=open("./index.html","r",encoding=("utf-8"))
    con=f.read()
    con=con.replace('''						<td>
							<a href="'''+name+'''/index.html">
								<svg width="1.5em" height="1em" version="1.1" viewBox="0 0 317 259"><use xlink:href="#folder"></use></svg>
								<span class="name">'''+name+'''</span>
							</a>
						</td>''',''''						<td>
							<a href="'''+name+'''/index.html">
								<svg width="1.5em" height="1em" version="1.1" viewBox="0 0 317 259"><use xlink:href="#folder"></use></svg>
								<span class="name">'''+tz.title+'''</span>
							</a>
						</td>
						<td>'''+tz.author+'''</td>''')
    f.close()
    f=open("./index.html","w",encoding=("utf-8"))
    f.write(con)   
    f.close()
        
#开始套娃
for H1 in IP:
    print("进入"+H1+"目录操作")
    f=open("./"+H1+"/index.html","r",encoding=("utf-8"))
    con=f.read()   
    con=con.replace('''<a href="index.html@sort=name&amp;order=asc">Name</a>''', '''<a href="index.html@sort=name&amp;order=asc">帖子</a>''')
    con=con.replace('''<a href="index.html@sort=size&amp;order=asc">Size</a>''', '''<a href="index.html@sort=size&amp;order=asc">作者</a>''')
    f=open("./"+H1+"/index.html","w",encoding=("utf-8"))
    f.write(con)   
    f.close()
    
    
    process=0
    #H1也就是最上级文件名字
    H2list=[]
    for tmp in os.listdir("./"+H1):
        if "-" in tmp:
            H2list.append(tmp)
    for H2 in H2list:
        process=process+1
        #H2也就是下级文件名
        file=open("./"+H1+"/"+H2+"/index.html",encoding=("utf-8"))
        soup=BeautifulSoup(file,'lxml')
        tz=TZ()#生成一个在TZ类下的对象——tz
        
        tz.title=str(soup.title).replace("<title>","").replace("</title>","")
        #print(tz.title)
        
        tz.author=str(soup.find_all("div",id="write")[0].find_all("div",attrs={"class": "author"})[0]).replace('<div class="author">            1楼 | ',"").split()[0]
        #print(tz.author)
        
        f=open("./"+H1+"/index.html","r",encoding=("utf-8"))
        con=f.read()
        con=con.replace('''								<span class="name">'''+H2+'''</span>
							</a>
						</td>''','''								<span class="name">'''+tz.title+'''</span>
							</a>
						</td>
                        <td>'''+tz.author+'''</td>''')
        f.close()
        f=open("./"+H1+"/index.html","w",encoding=("utf-8"))
        f.write(con)   
        f.close()
        #print("完成"+H2+"进度"+str(process)+"|"+str(len(H2list)))
