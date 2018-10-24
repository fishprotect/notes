安装
1:$sudo apt-get install zsh
2:$wget --no-check-certificate https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
3:$chsh -s /bin/zsh #将默认的shell从bash改为zsh
4:$sudo reboot
主题
/*
1:主题的路径在~/.oh-my-zsh/themes, 使某一主题生效的文件为~/.zshrc文件，找到ZSH_THEME="robbyrussell"一行（大概11行左右），把其注释掉，在下面添一行ZSH_THEME="ys"，之后关闭终端，再重启就好了
2:注意：在=符号右边一定不要有空格，否则会报错找不到此主题，我就是在这里困了半个多小时。
*/
插件
/*
1：比较好用的是last-working-dir，此插件的作用是下一次打开终端时定位到之前的目录下，是一个很好用的插件。
2：使用方法同上，不同的是找到plugins=(git)这一行，改为plugins=(git last-working-dir)，也是重启终端后生效。

*/
