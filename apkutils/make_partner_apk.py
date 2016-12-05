#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
import os.path
from config_parser import config
from apk_naming import Naming
import make_apk
import make_apk2

OUT_DIR = os.path.expanduser(config.get('build', 'out_dir'))

# GRADLE_BUILD_APK_DIR = '/Users/dingzhihu/dev/gerrit/aimeituan_gradle/aimeituan/build/apk'
GRADLE_BUILD_APK_DIR = '/Users/dingzhihu/dev/aimeituan_backup/aimeituan/build/apk'

PARTNERS = {
			'meituan': None,
			# 'meituan': ['xiaomi', 'Oppo1', 'QQguanjia1'], #默认应用名有空格
			'googlePlay': ['market'], #谷歌市场，应用名没有空格
			'wandoujia': ['wandoujia', 'wandoujiatg', 'wandoujiahl', '360anquan', 'baiduyidongsousuo', 'baidumobile'], #应用名为美团团购，有空格
			# 'baidumobile': None, #应用名为美团团购，并且修改了启动图
			# 'hiapk': ['hiapk', '91'], #修改了启动图
			# 'qq': None, #修改了启动图
			# 'sougouzs': None, #修改了启动图
			# 'taobaoruanjian': None, #修改了启动图
			'qihu360': None, #应用名为美团团购，修改了启动图，使用了第三方的精品应用
			'yingyonghui': None, #使用了第三方精品应用
			# 'lenovo': None, #修改了启动图
			'samsung': ['samsung', 'kuaibo1'], #不显示精品应用
			# 'meizu': None #魅族smartbar
			}

def upcase_first_letter(s):
    return s[0].upper() + s[1:]

def gradle_build_apk_file_name(name):
	return 'aimeituan-' + name + '-release.apk'





task = ['gradle', '-p', '/Users/dingzhihu/dev/aimeituan_backup']

task.extend(['assemble'+ upcase_first_letter(p) + 'Release' for p in PARTNERS])

subprocess.call(task)

for p in PARTNERS:
	channels = PARTNERS[p] if PARTNERS[p] else [p]
	apk_file = os.path.join(GRADLE_BUILD_APK_DIR, gradle_build_apk_file_name(p))
	# tmp_p = '__' + p
	# make_apk.make(apk_file, [tmp_p])

	# tmp_apk_file = os.path.join(OUT_DIR, Naming(tmp_p).signed_aligned()) 
	# make_apk2.make(tmp_apk_file, channels)

	# try:
	# 	os.remove(tmp_apk_file)
	# except OSError:
	# 	pass

	make_apk2.make(apk_file, channels)

	
	
		
		
	


