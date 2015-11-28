#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
"""
"""
#end_pymotw_header

import contextlib


def callback(*args, **kwds):
    print('closing callback(%s, %s)' % (args, kwds))


with contextlib.ExitStack() as stack:
    stack.callback(callback, 'arg1', 'arg2')
    stack.callback(callback, arg3='val3')
