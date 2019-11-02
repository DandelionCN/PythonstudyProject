# git basic use method
- git add . "."	 #添加所有文件到仓库中   
- git add "file name" 	#添加指定文件到仓库中   
- git commit -m "备注信息说明" 	#提交备注信息   
- git push -u origin master 	#首次提交数据到远程仓库的origin中   
- git push origin master 	#提交数据到远程仓库的origin中   
- git pull origin 	#从仓库获取跟新到本地   
- git status 	#查看状态   
- git config --list 	#查看配置信息   
- git commit -am '修改 hello.php 文件'   
---
# git commit、git push、git pull、 git fetch、git merge 的含义与区别
 - git commit：是将本地修改过的文件提交到本地库中;   
 - git push：是将本地库中的最新信息发送给远程库；   
 - git pull：是从远程获取最新版本到本地，并自动merge；   
-  git fetch：是从远程获取最新版本到本地，不会自动merge；   
 - git merge：是用于从指定的commit(s)合并到当前分支，用来合并两个分支；   
 - $git merge -b  // 指将 b 分支合并到当前分支   
 - git pull 相当于 git fetch + git merge。
---
# Git 移除文件
1. 要从 Git 中移除某个文件，就必须要从已跟踪文件清单中移除，然后提交。可以用以下命令完成此项工作   
git rm <file>

2. 如果删除之前修改过并且已经放到暂存区域的话，则必须要用强制删除选项 -f   
git rm -f <file>

3. 如果把文件从暂存区域移除，但仍然希望保留在当前工作目录中，换句话说，仅是从跟踪清单中删除，使用 --cached 选项即可   
git rm --cached <file>

4. 可以递归删除，即如果后面跟的是一个目录做为参数，则会递归删除整个目录中的所有子目录和文件：   
git rm –r * 

5. git mv README  README.md   
git mv 命令用于移动或重命名一个文件、目录、软连接。   

# Git brach
-git branch -a 查看所有分支，含远程   
-git branch 查看本地分支   
-git branch -r 查看远程分支   
-git branch newbranch 创建新分支   
-git branch -d oldbranch 删除分支oldbranch   
-git push origin newbranch 把新分支同步到远程仓库   
-git push origin :oldbranch 删除远程oldbranch分支   
-git checkout -b newbranch 切换到另一分支，如果不存在则创建   
-git checkout branch 切换到另一分支   
-git clone 新项目 无论当前项目在什么分支，都是下载默认master分支   
-git checkout master   
-git merge anthorbranch   
-git push origin maste 合并开发分支到master分支   
-git pull尽量少使用，隐含了合并信息   
-get featch 下载远程origin/master更新   
-git diff master origin/master 查看本地和远程库的区别   
-get merge origin/master 合并远端更新到本地    

---
# Git tags
-git tag v1.0 -m "tag v1"  创建一个标签    
-git push origin --tags    把所有标签同步到远程库    
-git checkout v1.0    检出v1.0版本    
-git reset --hard v1.0    使代码重置，回到v1.0。此功能慎用，后开发的代码会丢失    
-git tag -d v1.0    删除标签v1.0    
-git push origin :v1.0    删除远程库里标签    
-git tag -l -n1    查看所有tag    



