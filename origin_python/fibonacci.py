#! /usr/bin/env python
#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# File: fibonacci.py
# Date: 2018-10-11
# Author: gashero

"""
calculate fibonacci number
"""

def fib_recursive(x):
    """递归算法"""
    if x<=1:
        return 1
    else:
        return fib_recur(x-1)+fib_recur(x-2)
    return

def fib_recurrence(x):
    """递推算法"""
    return
