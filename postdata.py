from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://movie.douban.com/top250")

#form data内
postData = parse.urlencode([
    ("startstion",""),
    ("endstation",""),
    ("searchdate","")
]
)
req.add_header("Host","movie.douban.com")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400")
resp = urlopen(req,data = postData.encode("utf-8"))

print(resp.read().decode("utf-8"))
