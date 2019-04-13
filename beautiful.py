from bs4 import BeautifulSoup as bs
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://exampleScom/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc,"html.parser")

# print(soup.prettify())

# print(soup.title.string)
#The Dormouse's story

# print(soup.title.get_text())
#The Dormouse's story
# print(soup.a)
#<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# print(soup.find(id="link2"))
#<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>

# print(soup.find(id="link2").string)
#Lacie

# print(soup.find(id="link2").get_text())
#Lacie

# print(soup.find_all("a"))
#[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# for link in soup.findAll("a"):
#     print(link.string)
#
#Elsie
#Lacie
#Tillie

# print(soup.find("p",{"class":"story"}).get_text())
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.

# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)
#
# body
# b

data = soup.findAll("a",href = re.compile(r"^http://example.com/"))
print(data)
#
# [<a class="sister" href="http://exampleScom/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# data = soup.findAll("a",href = re.compile(r"^http://example\.com/"))
# print(data)
#
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]








