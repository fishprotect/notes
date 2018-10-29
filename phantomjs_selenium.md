#安装Phantomjs
#在官网下载phantomjs
$tar -xf  phantomjs-2.1.1-linux-x86_64.tar.bz2
$cd  phantomjs-2.1.1-linux-x86_64.tar.bz2/bin
$cp phantomjs /usr/bin


#安装selenium
$pip3 install selenium

#如果要使用无界面的firefox或者chrome,则需要
#本地需要geckodriver驱动器文件，本地需要geckodriver驱动器文件
#安装方法
url:https://github.com/mozilla/geckodriver/releases#下载对应的版本以后
$tar -axvf geckodriver-v0.23.0-linux64.tar.gz
$mv geckodriver /usr/bin/

