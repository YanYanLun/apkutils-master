#!/usr/bin/env python

import requests


LOGIN_URL = 'https://sso.sankuai.com/login'

def session(username, password):
	s = requests.Session()
	s.post(LOGIN_URL, dict(username=username, password=password))
	return s

def default_session():
	from config_parser import config
	return session(config.get('user', 'username'), config.get('user', 'password'))


