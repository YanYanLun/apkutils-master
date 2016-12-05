import zipfile
import subprocess

def find_channel_files(apk_file_path, channel_prefix):
	zipped = zipfile.ZipFile(apk_file_path, 'r', zipfile.ZIP_DEFLATED)
	namelist = zipped.namelist()
	channel_files = [f for f in namelist if channel_prefix in f]
	zipped.close()
	return channel_files




def remove_channel_files(apk_file_path, channel_files):
	for f in channel_files:
		subprocess.call(['zip', '-d', apk_file_path, f])


