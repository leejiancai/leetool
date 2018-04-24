#!/bin/usr/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Author: lijiancai
# File Name: test_re.py
# Contact: 958000432@qq.com
# Created Time: 2018/4/24 下午11:28
# Version: 1.0
# Description:
#
# Change Activities:
#           2018/4/24:
# ======================================================================================================================

import re

def dashrepl(matchobj):
    if matchobj.group(0) == '-':
        return ' '
    else:
        return '-'



def main():

    # group name 的使用;(?P<name>...)
    m = re.search(r'(?P<name>\w+) (?P<age>\d+)', 'lee 99')
    print("all group " + m.group())
    print("group 1: " + m.group(1))
    print("group [name]:" + m.group('name'))
    print('start of age: ' + str(m.start('age')))

    # group name在pattern中的使用；这句话的意思是重新匹配name在字符串的后面
    m = re.search(r'(?P<name>\w+) (?P<age>\d+) (?P=name)', 'lee 99 lee')
    print(m.group())

    # (?P<name>)的替换使用
    print("before sub")

    # sub的语义是替换在str中符合该pattern的成repl
    print(re.sub(r'(?P<name>\w{3}) (?P<age>\d+)', r'b \g<name>  a \2', 'lee 9988 lee'))

    # sub还支持函数作为repl
    print(re.sub(r'-{1,2}', dashrepl, 'pro----gram-files'))

    m = re.search(r'(?P<name>\w+) (?P<age>\d+) (?P=name)', 'lee 99 xxx')
    print(m and m.group())

    # (?=...) 一定要存在一个这样的模式在最后面 lookahead assertion

    m = re.search(r'\w{3} (?=\d+)', 'lee 99')

    print(m.group())

    m = re.search(r'\w{3} (?=\d+) \d', 'lee 99 c')

    assert not m

    # (?!...) negative lookahead assertion;字符串后面肯定不会出现该模式
    m = re.search(r'\w{3} (?!\d{3,})', 'lee 99')

    print(m.group())

    # (?<=...) lookbehind assertion 当前的字符串以该模式出现

    m = re.search(r'(?<=\d{3}) (\w+)', '234 lee 99')

    print(m.groups())

    # (?<!...) negative lookbehind assertion 当前的字符串不该以模式出现

    m = re.search(r'(?<!ccc) (\d+) (\d+)', 'aaa 99 22')

    print(m.group())

    # (?(id/name)yes-pattern|no-pattern) 条件匹配；即前面指定的id或name出现了才执行改匹配

    m = re.search(r'(?P<name><) (\d+) (?(name)>|\d)', '< 3222 >')

    print(m.groups())

    m = re.search(r'(<)? (\d+) ((?(1)>|\d))', r' 3222 3')

    print(m.groups())

    m = re.search(r'(<)? (\d+) ((?(1)>|\d))', r'< 3222 >')

    print(m.groups())



if __name__ == '__main__':
    main()