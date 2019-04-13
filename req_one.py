
from urllib import request

req = request.Request("http://movie.douban.com/top250")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400")
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))

