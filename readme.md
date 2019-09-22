# git basic use method

git add . "."	 #添加所有文件到仓库中

git add "file name" 	#添加指定文件到仓库中

git commit -m "备注信息说明" 	#提交备注信息

git push -u origin master 	#首次提交数据到远程仓库的origin中

git push origin master 	#提交数据到远程仓库的origin中

git pull origin 	#从仓库获取跟新到本地

git status 	#查看状态

git config --list 	#查看配置信息

git commit -am '修改 hello.php 文件'


git commit、git push、git pull、 git fetch、git merge 的含义与区别

 git commit：是将本地修改过的文件提交到本地库中；
 git push：是将本地库中的最新信息发送给远程库；
 git pull：是从远程获取最新版本到本地，并自动merge；
 git fetch：是从远程获取最新版本到本地，不会自动merge；
 git merge：是用于从指定的commit(s)合并到当前分支，用来合并两个分支；
$ git merge -b  // 指将 b 分支合并到当前分支
git pull 相当于 git fetch + git merge。


要从 Git 中移除某个文件，就必须要从已跟踪文件清单中移除，然后提交。可以用以下命令完成此项工作

git rm <file>

如果删除之前修改过并且已经放到暂存区域的话，则必须要用强制删除选项 -f

git rm -f <file>
如果把文件从暂存区域移除，但仍然希望保留在当前工作目录中，换句话说，仅是从跟踪清单中删除，使用 --cached 选项即可

git rm --cached <file>

可以递归删除，即如果后面跟的是一个目录做为参数，则会递归删除整个目录中的所有子目录和文件：

git rm –r * 

git mv README  README.md
git mv 命令用于移动或重命名一个文件、目录、软连接。
