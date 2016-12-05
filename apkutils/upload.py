#!/usr/bin/env python

class Uploader:
	
	UPLOAD_URL = "http://www.meituan.com/mis/mobileapp/add"

	_app = ['meituan', 'mtcrm', 'merchant', 'other', 'mapdiary', 'movie', 'taste', 'discount', 'mtcard', 'mtcardbiz', 'mtcardbd', 'xm', 'hotel', 'mogu', 'other']
	_platform = ['android', 'ios', 'ipad', 'androidhd']	

	def __init__(self, session):
		self.session = session

	def upload(self, app_name, version_code, version_name, channel, changelog, app_file, platform='android', enabled=True, force_upgrade=0):
		print 'uploading', channel
		data = dict(
			versionid=version_code,
			versionname=version_name,
			channel=channel,
			changelog=changelog,
			status=0,
			needupdate=0
			)

		data['appname'] = self._index(self._app, app_name)
		data['type'] = self._index(self._platform, platform)


		if not enabled:
			data['status'] = 1

		if force_upgrade:
			data['needupdate'] = 1

		import datetime
		data['addtime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		files = {'app': open(app_file, 'rb')}

		self.session.post(self.UPLOAD_URL, files=files, data=data)

	def _index(slef, list, item):
		if item not in list:
			return len(list)
		else:
			return list.index(item) + 1
