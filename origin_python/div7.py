#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# File: div7.py
# Date: 2018-10-11
# Author: gashero

"""
计算最大为n的数字里，可以被7整除的数字的数量
"""

def div7_1(n):
    cnt=0
    for i in range(n):
        if (i+1)%7==0:
            cnt+=1
    return cnt
