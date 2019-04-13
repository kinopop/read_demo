from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors


#请求URL并把结果用UTF-8编码
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")

#使用Beautifulsoup解析
soup = BeautifulSoup(resp,"html.parser")

#获得所有以/WIKI/开头的a标签的href属性
listUrls = soup.findAll("a",href=re.compile("^/wiki/"))

#输出所有的词条对应的名称和URL
for url in listUrls:
    #过滤一：jpg或JPG结尾的url
    if not re.search("\.(jpg|JPG)$",url["href"]):
        #输出url的文字和对应的链接
        print(url.get_text(),"<---->","https://en.wikipedia.org" + url["href"])
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='1234qwer',
                                     db='wikiurl',
                                     charset='utf8mb4')
        try:
            #获取会话指针
            with connection.cursor() as cursor:
            #创建SQL语句
                sql = "insert into `urls`(`urlname`,`urlhref`)values (%s,%s)"
            #执行SQL语句
                cursor.execute(sql, (url.get_text(), "https://en.wikipedia.org" + url["href"]))
            #提交
                connection.commit()

        finally:
            connection.close()