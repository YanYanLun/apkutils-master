只使用打包的备注
#### 1、将apk文件拷贝到apkutils目录里面
#### 2、在apkutils目录里面使用vim创建一个渠道列表文件:channels
###### 里面内容如下：
###### channel1
###### channel2
###### channel3
#### 3、修改config.ini文件
###### build_dir里面为打包编译目录，可以随意制定一个已存在的目录
###### 如:~/Downloads/apk_build  (确保该文件存在)
###### out_dir里面为打包输出目录，制定一个目录
###### 如：~/Downloads/apks
#### 4、运行命令: python make_apk2.py app-debug.apk channels 
#### 5、使用ChannelReader类去读取渠道号
#### 其他：
###### 1、如果要修改META-INF的渠道文件名字，可以修改make_apk2.py中的META_CHANNEL_FILE_NAME_TEMPLATE以及修改ChannelReader类中的KEY_CHANNEL
###### 2、如果要修改渠道打包的名字，可以直接修改config.ini文件中相关字段以及apk_naming.py


