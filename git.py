#git笔记
###添加SSH（给git或者gitte）
1：$ssh-keygen -t rsa -C "youremail@example.com"
2：$cd ~/.ssh
3：复制id_rsa.pub文件到个github->settings->SSH and GPA keys->New SSH key
4：保存（点击Add SSH key）
###远程仓库的PUSH&PULL
1：$git clone some_addr
2: $git pull origin <branch>
3: $git push origin <branch>
4: $git push origin :<branch>  #删除远程分支
###分支建立，删除，合并，切换
1：$git checkout -b <new_branch_name>
2: $git branch -D <branch_name> #删除本地分支
3: $git checkout <branch_name>  #切换分支
4：$git merge --no-ff -m "add merge" <some_branch> #合并分支


