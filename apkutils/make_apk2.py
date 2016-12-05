#!/usr/bin/env python

import zipfile
import argparse
import shutil
import os, os.path

from config_parser import config
from apk_naming import Naming

import apkfile

BUILD_DIR = os.path.expanduser(config.get('build', 'build_dir'))
OUT_DIR = os.path.expanduser(config.get('build', 'out_dir'))
META_CHANNEL_FILE_NAME_TEMPLATE = "META-INF/mtchannel_{channel}"


def make(src_apk_path, channel_list):
	tmp_src_apk_path = os.path.join(BUILD_DIR, 'temp.apk')
	shutil.copy(src_apk_path, tmp_src_apk_path)
	channel_files = apkfile.find_channel_files(tmp_src_apk_path, 'META-INF/channel_')
	apkfile.remove_channel_files(tmp_src_apk_path, channel_files)

	if not os.path.exists(OUT_DIR):
		os.makedirs(OUT_DIR)
		
	empty_file_name = 'empty'
	empty_file_path = os.path.join(OUT_DIR, empty_file_name)
	open(empty_file_path, 'w').close()
	for channel in channel_list:
		dst_apk_name = Naming(channel).signed_aligned()
		dst_apk_path = os.path.join(OUT_DIR, dst_apk_name)
		if os.path.isfile(dst_apk_path):
			print dst_apk_name, 'exists'
			continue
		shutil.copy(tmp_src_apk_path, dst_apk_path)
		zipped = zipfile.ZipFile(dst_apk_path, 'a', zipfile.ZIP_DEFLATED) 
		arcname = META_CHANNEL_FILE_NAME_TEMPLATE.format(channel=channel)
		zipped.write(empty_file_path, arcname)

	os.remove(empty_file_path)
	os.remove(tmp_src_apk_path)
		


def main():
	parser = argparse.ArgumentParser(description='make apk')
	parser.add_argument('apk_file', action='store')
	parser.add_argument('channel_file', action='store', type=file)
	args = parser.parse_args()
	channel_list = args.channel_file.read().strip().splitlines()
	make(args.apk_file, channel_list)


if __name__ == '__main__':
	main()