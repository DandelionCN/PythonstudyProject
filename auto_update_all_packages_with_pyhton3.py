#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pip

from pip._internal.utils.misc import get_installed_distributions

from subprocess import call

from time import sleep

i=1
for dist in get_installed_distributions():
    print("Current updating Package is Num:{}/total:{}".format(i,len(get_installed_distributions())))
    call("pip3 install --user -U " + dist.project_name, shell=True)
    i+=1
