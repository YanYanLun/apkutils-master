try:
	from setuptools import setup, find_packages
except:
	from distutils.core import setup

config = {
    'name': 'apkutils',
    'version': '0.1',
    'author': 'dingzhihu',
    'author_email': 'dingzhihu@gmail.com',
    'description': 'meituan apk utils',
    'log_description': open('README.md').read(),
    'packages': find_packages(),
    'install_requires': ['requests', 'xlrd'],
    'entry_points': {
        'console_scripts':[
             'upgrade_action = apkutils.upgrade_action:main',
             'make_apk = apkutils.make_apk:main',
             'batch_upload = apkutils.batch_upload:main',
             'make_channel_files = apkutils.make_channel_files:make_channel_files',
             'main = apkutils.main:main'
        ]
    },
    'include_package_data': True
    
}

setup(**config)