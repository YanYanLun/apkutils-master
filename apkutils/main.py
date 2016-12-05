#!/usr/bin/env python

from make_channel_files import make_channel_files
from config_parser import config
from make_apk import make
from batch_upload import batch_upload
import os.path
import argparse
from channel_list import channel_list

def main():
	APK_DIR = os.path.expanduser(config.get('build', 'out_dir'))

	parser = argparse.ArgumentParser()
	parser.add_argument('apk_file', action='store')
	args = parser.parse_args()

	make_channel_files()

	channels = channel_list()

	# make apks
	make(args.apk_file, channels)

	# upload apks
	batch_upload(APK_DIR, channels)




if __name__ == '__main__':
	main()





