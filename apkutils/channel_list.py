#!/usr/bin/env python
import os
import os.path
from config_parser import config

def channel_list():
	all = []
	channel_file_dir = os.path.expanduser(config.get('channel', 'channel_file_dir'))
	for channel_file_name in os.listdir(channel_file_dir):
		channel_file = os.path.join(channel_file_dir, channel_file_name)
		if os.path.isfile(channel_file):
			with open(channel_file) as f:
				channels  = f.read().strip().splitlines()
				for channel in channels:
					if channel not in all:
						all.append(channel)
				

	return all


if __name__ == '__main__':
	channel_list()
	# print '\n'.join(channel_list())
