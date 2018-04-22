#!/bin/usr/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Author: lijiancai
# File Name: smtp_demo.py
# Contact: 958000432@qq.com
# Created Time: 2018/4/22 下午11:28
# Version: 1.0
# Description:
#
# Change Activities:
#           2018/4/22:
# ======================================================================================================================

import smtplib
import traceback
import getpass

def main():
    try:
        #smtpObj = smtplib.SMTP('smtp.163.com', 25)
        """
        smtp 使用有三种方式:1是明文使用；2是tls加密；3是ssl加密
        1的使用方法：
            smtpObj = smtplib.SMTP('smtp.163.com', 25)
            smtpObj.ehlo()
        2的使用方法：
            smtpObj = smtplib.SMTP('smtp.163.com', 25)
            smtpObj.ehlo()
            smtpObj.startssl()
        3的使用方法：
            smtpObj = smtplib.SMTP_SSL('smtp.163.com', 465)
            smtpObj.ehlo()
        """

        smtpObj = smtplib.SMTP_SSL('smtp.163.com', 465)

        # 尝试连接一下
        smtpObj.ehlo()

        user = "leejiancai@163.com"

        passwd = getpass.getpass("Input passwd:")

        smtpObj.login(user, passwd)

        # msg 必须是以【Subject: sth \n】开头
        smtpObj.sendmail(from_addr=user, to_addrs=user, msg="Subject: So long\n Dear lee")

        smtpObj.close()

    except Exception as e:
        print(e)
        traceback.print_exc()



if __name__ == '__main__':
    main()