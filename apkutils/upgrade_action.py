#!/usr/bin/env python

import user_session
from ConfigParser import SafeConfigParser
import argparse
from pkg_resources import resource_filename

class UpgradeAction:
	URL_TMPLATE_ENABLE = "http://www.meituan.com/mis/mobileapp/enable/{id}"
	URL_TMPLATE_DISABLE = "http://www.meituan.com/mis/mobileapp/delete/{id}"

	def __init__(self, session):
		self.session = session

	def handle_upgrade_action(self, begin_id, end_id, enable=False):
		if enable:
			url_tmplate = self.URL_TMPLATE_ENABLE
		else:
			url_tmplate = self.URL_TMPLATE_DISABLE

		for id in xrange(begin_id, end_id + 1):
			url = url_tmplate.format(id=id)
			self.session.post(url)

def parse_args():
	parser = argparse.ArgumentParser(description='enable or disable upgrade')
	parser.add_argument('begin', action='store', type=int)
	parser.add_argument('end', action='store', type=int)
	parser.add_argument('-e', '--enable', action="store_true", dest='enable_upgrade', default=False)
	args = parser.parse_args()
	return args

def parse_config():
	parser = SafeConfigParser()
	parser.read(resource_filename(__name__, 'config.ini'))
	username =  parser.get('user', 'username')
	password = parser.get('user', 'password')
	return (username, password)

def main():
	(username, password) = parse_config()
	session = user_session.session(username, password)

	args = parse_args()
	action = UpgradeAction(session)
	action.handle_upgrade_action(args.begin, args.end, args.enable_upgrade)


if __name__ == '__main__':
	main()
	


