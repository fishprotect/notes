#设置ssh免密码登录
'''
	#假设有3台机器
	#分别是：192.168.161.74 min2
		 192.168.161.81 min3
		 192.168.161.76 min1
	在3台机器的/etc/hosts 文件中加入以上
	# 在三台机器上分别执行以下命令
	$ ssh-keygen -t rsa
	# 然后在/username/.ssh/下找到id_rsa.pub
	# 新建authorized_keys,将三台机器上的id_rsa.pub复制到里面
	$ scp authorized_keys root@min2:/root/.ssh/authorized_keys
	$ chmod 600 authorized #在三台机器上都要执行
	
'''
