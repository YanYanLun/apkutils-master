#!/usr/bin/env python

import argparse
from config_parser import config
from apk_naming import Naming
import os
import os.path
import shutil
import subprocess
import re

CHANNEL_ATTR_NAME =  config.get('android_manifest', 'channel_attr_name')
KEYSTORE = config.get('keystore', 'keystore')
STOREPASS = config.get('keystore', 'storepass')

BUILD_DIR = os.path.expanduser(config.get('build', 'build_dir'))
OUT_DIR = os.path.expanduser(config.get('build', 'out_dir'))
ANDROID_MANIFEST = os.path.join(BUILD_DIR, 'AndroidManifest.xml')

def get_replace_content(channel, content=None):
	pattern = r'(<meta-data\s+android:name="{channel_attr_name}"\s+android:value=")(\S+)("\s+/>)'.format(channel_attr_name=CHANNEL_ATTR_NAME)
	replacement = r"\g<1>{channel}\g<3>".format(channel=channel)

	if not content:
		content = open(ANDROID_MANIFEST).read()
	return re.sub(pattern, replacement, content)
	

def replace_channel(channel):
	content = get_replace_content(channel)
	f = open(ANDROID_MANIFEST, 'w')
	f.write(content)
	f.close()

def check_channel_replace(channel_list):
	ok = True
	content = get_replace_content('test')
	for channel in channel_list:
		checked_channel = '''android:value="{channel}"'''.format(channel=channel)
		content = get_replace_content(channel, content)
		if checked_channel not in content:
			ok = False
			print channel, 'replace error'
	return ok



def make(apk_file, channel_list):
	shutil.rmtree(BUILD_DIR, ignore_errors=True)
	subprocess.call(['apktool', 'd', apk_file, BUILD_DIR])

	ok = check_channel_replace(channel_list)
	if not ok:
		return

	for channel in channel_list:
		print 'replace', channel
		replace_channel(channel)
		naming = Naming(channel)
		unsigned_apk = os.path.join(OUT_DIR, naming.unsigned())
		subprocess.call(['apktool', 'b', BUILD_DIR, unsigned_apk])

		signed_apk = os.path.join(OUT_DIR, naming.signed())
		subprocess.call(['jarsigner', '-verbose', '-sigalg','MD5withRSA', '-digestalg', 'SHA1', '-keystore', os.path.expanduser(KEYSTORE), '-storepass', STOREPASS, '-signedjar', signed_apk, unsigned_apk, 'sankuai'])

		signed_aligned_apk = os.path.join(OUT_DIR,naming.signed_aligned())
		if not os.path.isfile(signed_aligned_apk):
			subprocess.call(['zipalign', '4', signed_apk, signed_aligned_apk])
		else:
			print signed_aligned_apk, 'exists'

		os.remove(unsigned_apk)
		os.remove(signed_apk)


def main():
	parser = argparse.ArgumentParser(description='make apk by channel')
	parser.add_argument('apk_file', action='store')
	parser.add_argument('channel_file', action='store', type=file)
	args = parser.parse_args()
	channel_list = args.channel_file.read().strip().splitlines()
	make(args.apk_file, channel_list)


if __name__ == '__main__':
	main()
	






