#!/usr/bin/env python
import user_session
from bs4 import BeautifulSoup
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 

class Main(object):
	"""handle the find process"""
	def __init__(self, session, naming):
		super(Main, self).__init__()
		self.session = session
		self.naming = naming
	
	def process(self, page_from =1, page_to = 1):
		crawler = Crawler(session)
		parser = Parser(self.naming)
		for page_num in range(page_from, page_to + 1):
			content = crawler.fetch_content(page_num)
			parser.feed(content, page_num)
		result = parser.get_result()
		print result


class Crawler(object):
	"""fetch content"""
	def __init__(self, session):
		super(Crawler, self).__init__()
		self.URL_TMPL = 'http://www.meituan.com/mis/mobileapp/list/page{page_num}'
		self.session = session

	def fetch_content(self, page_num):
		url = self.URL_TMPL.format(page_num=page_num)
		r = self.session.get(url)
		return r.content
		


class Parser(object):
	"""parse content"""
	def __init__(self, naming):
		super(Parser, self).__init__()
		self.naming = naming
		self.result = []

	def feed(self, content, page_num):
		soup = BeautifulSoup(content)
		for row in soup('tr'):
			cols = row('td')
			if cols:
				id = cols[1]('a')[0].get('href').split('/')[-1]
				name =  cols[10]('a')[0].get('href').split('/')[-1]
				if self.naming == name:
					self.result.append(dict(
						id = id,
						name = name,
						page = page_num
						))

	def get_result(self):
		return self.result


if __name__ == '__main__':
	session = user_session.default_session()
	naming = 'aimovie-70-wandoujia-signed-aligned.apk'
	handler = Main(session, naming)
	handler.process()



	