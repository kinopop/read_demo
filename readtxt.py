from urllib.request import urlopen
import pdfminer

html = urlopen("https://en.wikipedia.org/robots.txt")

print(html.read().decode("utf-8"))