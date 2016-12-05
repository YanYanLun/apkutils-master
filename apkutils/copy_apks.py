#!/usr/bin/env python

import shutil

from config_parser import config
import os, os.path
from apk_naming import Naming


OUT_DIR = os.path.expanduser(config.get('build', 'out_dir'))
APKS_DIR  = os.path.join(OUT_DIR, 'apks')


shutil.rmtree(APKS_DIR, ignore_errors=True)
os.mkdir(APKS_DIR)


channel_file_dir = os.path.expanduser(config.get('channel', 'channel_file_dir'))
for channel_file_name in os.listdir(channel_file_dir):
	if channel_file_name == '.DS_Store':
		continue
	dir = os.path.join(APKS_DIR, channel_file_name)
	os.mkdir(dir)

	channel_file = os.path.join(channel_file_dir, channel_file_name)
	with open(channel_file) as f:
		channels  = f.read().strip().splitlines()
		for channel in channels:
			apk_file_name = Naming(channel).signed_aligned()
			src_apk_file = os.path.join(OUT_DIR, apk_file_name)
			dst_apk_file = os.path.join(dir, apk_file_name)
			if os.path.exists(src_apk_file):
				shutil.copy(src_apk_file, dst_apk_file)
			else:
				print src_apk_file, 'not exists'



	

	


