import  urllib
import re

url = "http://www.iydsj.com"
html = urllib.urlopen(url).read()

pic_url = re.findall('img src="(.*?)"', html, re.S)

for each in pic_url:
    if each.find('http') < 0:
        each = url + each
    print each
