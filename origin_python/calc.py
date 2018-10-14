#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# File: calc.py
# Date: 2018-10-11
# Author: gashero

"""
各种耗时间的计算
"""

import time
import threading

import numpy as np

def avgn1(n):
    """单线程计算1到N的平均数"""
    total=0.0
    for i in xrange(n):
        total+=(i+1)
    return total/n

def primecount1(n):
    """寻找N以内的质数数量，用最蠢的算法"""
    #计算10万以内质数的数量，纯Python的primecount1，耗时42.749秒
    cnt=0
    for i in range(1,n):
        v=i+1
        for j in range(2,v/2+1):
            if v%j==0:
                break
        else:
            #print 'prime',v
            cnt+=1
        #print 'v=',v,'cnt=',cnt
    return cnt

def primecount_numpy(n):
    """使用numpy的4线程版本"""
    cnt=0
    nn=np.array(range(1,n+1),dtype=np.uint32)
    return cnt

def primecount_ctypes(n):
    #TODO
    return

def primecount_cython(n):
    #TODO
    return

def test_numpy():
    """测试numpy计算FFT的多线程占用"""
    def _calc_fft(n):
        for i in range(n):
            a1=np.random.rand(65536)
            a2=np.fft.fft(a1)
    thrdlist=[]
    for i in range(4):
        thrd=threading.Thread(target=_calc_fft,args=(4096,))
        thrd.start()
        thrdlist.append(thrd)
    for thrd in thrdlist:
        thrd.join()
    return
