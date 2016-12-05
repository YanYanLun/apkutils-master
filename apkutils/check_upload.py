#!/usr/bin/env python

import requests
from channel_list import channel_list

class VersionInfo:

	URL_TEMPLATE = "http://www.meituan.com/api/v2/appstatus?channel={channel}&version={version}&name={name}&type={platform}"

	def __init__(self, platform, name, version):
		self.version = version
		self.platform = platform
		self.name = name

	def request_version_info(self, channel):
		url = self.URL_TEMPLATE.format(platform=self.platform, name=self.name, version=self.version, channel=channel)
		r = requests.get(url)
		return r.json['versioninfo']



def check(checked_channel, unchecked_channel_list, version, name='meituan', platform='android'):
	info = VersionInfo(platform, name, version)
	checked_version_info = info.request_version_info(checked_channel)
	checked_versionname = checked_version_info['versionname']
	print "checked channel:{channel}, checked version:{version}".format(channel=checked_channel, version=checked_versionname)
	for channel in unchecked_channel_list:
		if channel == checked_channel:
			continue
		version_info = info.request_version_info(channel)
		versionname = version_info['versionname']

		if versionname != checked_versionname:
			print "unchecked channel:{channel}, unchecked version:{version}".format(channel=channel, version=versionname)





		
if __name__ == '__main__':
	version = 73
	checked_channel = 'meituan'
	channel_list = channel_list()
	check(checked_channel, channel_list, version)

	


