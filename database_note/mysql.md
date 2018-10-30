#mysql配置文件位置：
/etc/mysql/mysql.conf.d/mysqlld.cnf
#root账号的密码：
dongyuhong_fish_0938
#免密码登录：
#免密码登录账号：yuhongd
在配置文件最后加上:skip-grant-tables
然后需要重新启动mysql服务


#更新root账号密码（由于mysql新版的账号要求比较严格，所以必须设置一定复杂程度的密码，不然只能在计算机root账户下登录mysql）
>> update mysql.user set authentication_string=PASSWORD('dongyuhong_fish_0938'), plugin='mysql_native_password' where user='root';


#新建账号密码(在计算机的root权限下，登录mysql的root‘)
>> grant all privileges on *.* to 'mysql'@'%' identified by '123' with grant option；
>> flush privileges;
#注：上述第一句命令中，%表示所有地址都可以登录

#python3使用mysql
$pip3 install pymysql
#python2使用Mysql
$pip install Python-MYSQL   #(更加熟悉的名字是MySQLdb)
