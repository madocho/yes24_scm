from bs4 import BeautifulSoup
import requests

BASE_URL = "http://www.yes24.com/_par_/Rss/KNU001001001.xml"

responses = requests.get(BASE_URL)
soup = BeautifulSoup(responses.content, 'lxml-xml')

# 책 제목, 도서코드 찾기
for bookitem in soup.findAll('item'):
  booktitle = bookitem.find('title')
  guid = bookitem.find('guid')

import pymysql

# mysql 연결
conn = pymysql.connect(host="localhost", user="root", password="", db="book_infor", charset="utf8")

curs = conn.cursor(pymysql.cursors.DictCursor)

data = (guid.text, booktitle.text)

# sql 데이터 입력
sql = """insert into book_test(bookcode,bookname)
       values (%s, %s)"""

curs.executemany(sql, [data])

conn.commit()

conn.close()
