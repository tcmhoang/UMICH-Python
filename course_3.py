# import re
# import urllib.request as res

# content = res.urlopen('http://py4e-data.dr-chuck.net/regex_sum_1543969.txt')


# print(sum(map(int, re.findall('\D*(\d+)\D*', content.read().decode()))))


# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')

# mysock.close()


# from bs4 import BeautifulSoup as Soup
# from urllib.request import urlopen
# import re

# wcontent = urlopen('http://py4e-data.dr-chuck.net/comments_1543971.html')
# soup = Soup(wcontent.read().decode(), 'html.parser')
# span_tags = soup.find_all('span', attrs={
#     'class': 'comments'}, string=re.compile('.*(\d+).*'))
# tc = len(span_tags)
# ts = sum([int(i.string.strip()) for i in span_tags])

# print(tc)
# print(ts)


# from urllib.request import urlopen
# from bs4 import BeautifulSoup as Soup
# import re

# url = 'http://py4e-data.dr-chuck.net/known_by_Malecia.html'

# count = 7
# pos = 18

# real_pos = pos - 1


# def getUrls(count, pos, url):
#     if count == 0:
#         return [url]
#     else:
#         soup = Soup(urlopen(url).read().decode(), 'html.parser')
#         la = soup.find_all('a')
#         if pos < len(la):
#             link = la[pos].get('href', None)
#             if(link != None):
#                 res = getUrls(count - 1, pos, link)
#                 res.insert(0, url)
#                 return res
#         return [url]


# print(' '.join([name for name in map(lambda x: re.findall(
#     'known_by_(\w+)\.', x)[0], getUrls(count, real_pos, url))]))


# from urllib.request import urlopen
# import xml.etree.ElementTree as ET

# url = 'http://py4e-data.dr-chuck.net/comments_1543973.xml'

# wcontent = urlopen(url).read().decode()
# xmlcontent = ET.fromstring(wcontent)
# counts = xmlcontent.findall('.//count')
# print(sum([i for i in map(lambda x: int(x.text), counts)]))


# from urllib.request import urlopen
# import json

# url = 'http://py4e-data.dr-chuck.net/comments_1543974.json'
# wcontent = urlopen(url).read().decode()
# parsed_data = json.loads(wcontent)['comments']
# print(sum([int(tupl['count']) for tupl in parsed_data]))

from urllib.request import urlopen
from urllib.parse import urlencode
import json


api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'


while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urlencode(parms)

    print('Retrieving', url)
    uh = urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    place_id = js['results'][0]['place_id']
    print('placea_id', place_id)
