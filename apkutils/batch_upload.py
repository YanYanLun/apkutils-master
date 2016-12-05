#!/usr/bin/env python

import os.path
import argparse
from config_parser import config
from apk_naming import Naming
import user_session
from upload import Uploader


APP_NAME = config.get('upload', 'app_name')
VERSION_CODE = config.get('app', 'version_code')
VERSION_NAME = config.get('app', 'version_name')
CHANGE_LOG = config.get('app', 'change_log')

def batch_upload(apk_dir, channel_list):
	session = user_session.default_session()
	uploader = Uploader(session)

	for channel in channel_list:
		naming = Naming(channel)
		apk_file = os.path.join(apk_dir, naming.signed_aligned())
		if not os.path.exists(apk_file):
			print '{file} does not exist'.format(file=apk_file)
			continue
			
		uploader.upload(APP_NAME, VERSION_CODE, VERSION_NAME, channel, CHANGE_LOG, apk_file)

def main():
	default_apk_dir = config.get('build', 'out_dir')
	parser = argparse.ArgumentParser(description='batch upload apk to mis')
	parser.add_argument('--dir', action='store' ,dest='apk_dir', default=default_apk_dir)
	parser.add_argument('channel_file', action='store', type=file)
	args = parser.parse_args()
	apk_dir = os.path.expanduser(args.apk_dir)
	channel_list = args.channel_file.read().strip().splitlines()

	batch_upload(apk_dir, channel_list)

if __name__ == '__main__':
	main()
