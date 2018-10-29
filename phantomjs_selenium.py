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

#headless无界面的使用方法

##firefox headless模式
from selenium import webdriver
options = webdriver.FirefoxOptions()
options.set_headless()
# options.add_argument(‘-headless‘)
options.add_argument(‘--disable-gpu‘)#‘--disable-gpu‘这句是禁用GPU加速。
driver=webdriver.Firefox(firefox_options=options)
driver.get(‘http://httpbin.org/user-agent‘)
driver.get_screenshot_as_file(‘test.png‘)
driver.close()


##chrome headless模式

from selenium import webdriver
options=webdriver.ChromeOptions()
options.set_headless()
# options.add_argument(‘--headless‘)
options.add_argument(‘--disable-gpu‘)
driver=webdriver.Chrome(options=options)
driver.get(‘http://httpbin.org/user-agent‘)
driver.get_screenshot_as_file(‘test.png‘)
driver.close()





