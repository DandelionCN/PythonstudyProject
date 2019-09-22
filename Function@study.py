#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
def function_1(A):
    print("step6:function_1")
    print("step7:Func1 result is:"+str(A+1))


def function_2(B):
    print("step1:输入参数B为函数function_name()")
    result=B(3)
    print("step4:输出函数引用计算结果:"+str(result))
    print("step5:function_2 is close.")
    return result

t1=time.time()

@function_1
@function_2
def function_name(n):
    print("step2:Hello World ,i am function_name")
    print("step3:return Function:n+5")
    return n+5

t2=time.time()

print("step8:Time cost is:{}ms".format((t2-t1)*1000))

