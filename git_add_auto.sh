#!/bin/bash
git add .
echo -n "please input the commit information:"
read commit_info
echo "the commit update information is $commit_info"
git commit -m "$commit_info"
git push origin master
