# 修改用户密码
# win10 
mysqld --skip-grant-tables
# 然后新打开一个cmd,就可以免密码登陆MySQL
# 登陆以后输入以下命令
use mysql;
update user set authentication_string=password('this is your password')where user='root';
flush privileges;


# mysql 新建用户
GRANT ALL PRIVILEGES ON *.* TO username@"%" IDENTIFIED BY 'password'
# 在上面，username是新的用户名，password是密码

