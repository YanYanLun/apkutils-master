#!/usr/bin/env python

import os.path
from config_parser import config
from apk_naming import Naming
import os
import os.path
import re



def rename_suffix(channel_list, suffix):
	apk_dir = os.path.expanduser(config.get('build', 'out_dir'))
	for channel in channel_list:
		naming = Naming(channel)
		cur_name = naming.signed_aligned()
		renamed_name = naming.signed_aligned(suffix)
		cur_file = os.path.join(apk_dir, cur_name)
		replaced_file = os.path.join(apk_dir, renamed_name)
		os.rename(cur_file, replaced_file)

def delete_apk(channel_list):
	apk_dir = os.path.expanduser(config.get('build', 'out_dir'))
	for channel in channel_list:
		name = Naming(channel).signed_aligned()
		apk_file = os.path.join(apk_dir, name)
		if os.path.exists(apk_file):
			print 'remove', channel
			os.remove(apk_file)
		else:
			print channel, 'not exists'



def check_replace(channel):
	pattern = r'(<meta-data\s+android:name="{channel_attr_name}"\s+android:value=")(\S+)("\s+/>)'.format(channel_attr_name='channel')
	replacement = r"\g<1>{channel}\g<3>".format(channel=channel)
	print replacement
	content = '''<meta-data android:name="channel" android:value="app_name" />'''
	content = re.sub(pattern, replacement, content)
	print content

if __name__ == '__main__':
	pass


