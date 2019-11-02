#!/bin/bash
git add .
echo "please input the commit information:"
read commit_info
echo -e "\e[31;40m The commited update information is:$commit_info \e[0m"
git commit -m "$commit_info"
git push origin master
echo -e "\e[31;40m Update is commited successfully! \e[0m"
