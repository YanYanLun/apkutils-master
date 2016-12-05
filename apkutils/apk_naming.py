#!/usr/bin/env python

from config_parser import config

APP_NAME = config.get('app', 'app_name')
VERSION_CODE = config.get('app', 'version_code')
APP_SUFFIX = config.get('app', 'app_suffix')

class Naming:
	def __init__(self, channel):
		self.channel = channel
		self.base_name = '{app_name}-{version_code}-{channel}'.format(app_name=APP_NAME, version_code=VERSION_CODE, channel=channel)

	def unsigned(self):
		return '{name}.apk'.format(name=self.base_name)

	def signed(self):
		return '{name}-signed.apk'.format(name=self.base_name)

	def signed_aligned(self, suffix=APP_SUFFIX):
		return '{name}-signed-aligned-{suffix}.apk'.format(name=self.base_name, suffix=suffix)


if __name__ == '__main__':

	naming = Naming('testchannel')
	print naming.signed_aligned()
