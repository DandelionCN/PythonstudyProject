#!/bin/bash
git add .
echo "please input the commit information:"
read commit_info
#read -p "please input your name and age:" commit_info

#echo "The commited update information is:$commit_info"
echo -e "\e[31;40m The commited update information is:$commit_info \e[0m"

git commit -m "$commit_info"
git push origin master

#echo "Update is commited successfully!"
echo -e "\e[31;40m Update is commited successfully! \e[0m"

#以 \e[前景颜色;背景颜色m  开头，中间为内容，然后以 \e[0m结束;
#0m表示将颜色恢复为默认的颜色，如果不加0m，则之后的所有输出都将使用前面的设置;
#其中使用字母m来分隔转义字符和内容。同时输出的时候，因为有转义字符，所以要加-e参数;
#\e可以使用八进制的\033代替。
#字体颜色:黑30	红31	绿32	棕33	蓝34	紫35	青36	白37;
#背景颜色:黑40	红41	绿42	棕43	蓝44	紫45	青46	白47
