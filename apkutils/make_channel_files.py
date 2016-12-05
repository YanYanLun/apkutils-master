#!/usr/bin/env python

from config_parser import config
import os
import os.path
import xlrd
import re
from collections import OrderedDict

CHANNEL_FILE_DIR = os.path.expanduser(config.get('channel', 'channel_file_dir'))
CHANNEL_SHEET_FILE = os.path.expanduser(config.get('channel', 'channel_sheet_file'))

CONFIG = [
	dict(
	file='market',
	sheet_index=0,
	column_index=4
	),
	dict(
	file='ad',
	sheet_index=1,
	column_index=4
	)
]

if not os.path.exists(CHANNEL_FILE_DIR):
	os.makedirs(CHANNEL_FILE_DIR)

def dedupe(_list):
    return OrderedDict((item,None) for item in _list).keys()

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def read_channels(workbook, sheet_index, column_index):
	channel_list = []
	sheet = workbook.sheets()[sheet_index]
	for i in range(1, sheet.nrows):
		channel = sheet.row_values(i)[column_index].encode('utf-8').strip()
		if not channel:
			continue
		if re.search(r'\s', channel):
			print channel, 'contains space'
			continue
		if not is_ascii(channel):
			print channel
			continue

		channel_list.append(channel)
	return dedupe(channel_list)
	

def save_channels(channels, file_name):
	file_path = os.path.join(CHANNEL_FILE_DIR, file_name)
	with open(file_path, 'w') as f:
		f.write('\n'.join(channels))


def make_channel_files():
	data = xlrd.open_workbook(CHANNEL_SHEET_FILE)
	all_channel_list = []
	for cfg in CONFIG:
		channel_list = read_channels(data, cfg['sheet_index'], cfg['column_index'])
		unique_channel_list = []
		for channel in channel_list:
			if channel not in all_channel_list:
				unique_channel_list.append(channel)
			else:
				print channel, 'already exists in previous channel file'
		save_channels(unique_channel_list, cfg['file'])
		all_channel_list.extend(unique_channel_list)

	print 'channel count:', len(all_channel_list)

if __name__ == '__main__':
	make_channel_files()
	


