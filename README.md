apkutils
===
一些和apk相关的工具，包括替换渠道，批量上传mis后台，批量上架，批量下架等

Prerequisite
===
1. requests (http请求)
2. xlrd (读excel)
3. apktool(apk解包打包), jarsigner(签名), zipalign(混淆)
4. BeautifulSoup4 (解析html)

Usage
===
* 编辑config.ini文件，修改相应的配置
* 用户登录: user_session.py
* 根据渠道生成apk: make_apk.py
* 上传到mis后台，批量上下架: upload.py, batch_upload.py, upgrade_action.py
* 从excel解析生成渠道文件: make_channel_files.py
* 把生成的apk根据渠道文件放到不同的文件夹下: copy_apks.py
* 通过在META-INF文件夹下新建文件的方式生成apk: make_apk2.py


Example
===
### 根据渠道列表文件生成apk
	python make_apk.py apk_file channel_list_file
### 在META-INF文件夹下新建空白文件生成apk
	python make_apk2.py apk_file channel_list_file
### 批量上传到mis后台
	python batch_upload.py channel_list_file
### 批量下架
	python upgrade_action.py begin_id end_id
### 批量上架
	python upgrade_action.py begin_id --enable



只使用打包的备注(夜风)
1、将apk文件拷贝到apkutils目录里面
2、在apkutils目录里面使用vim创建一个渠道列表文件:channels
	里面内容如下：
	channel1
	channel2
	channel3
3、修改config.ini文件
	build_dir里面为打包编译目录，可以随意制定一个已存在的目录
	如:~/Downloads/apk_build  (确保该文件存在)
	out_dir里面为打包输出目录，制定一个目录
	如：~/Downloads/apks
4、运行命令: python make_apk2.py app-debug.apk channels 
5、使用ChannelReader类去读取渠道号
其他：
1、如果要修改META-INF的渠道文件名字，可以修改make_apk2.py中的META_CHANNEL_FILE_NAME_TEMPLATE
	以及修改ChannelReader类中的KEY_CHANNEL
2、如果要修改渠道打包的名字，可以直接修改config.ini文件中相关字段以及apk_naming.py


