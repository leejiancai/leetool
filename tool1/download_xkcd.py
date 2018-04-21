#!/bin/usr/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Author: lijiancai
# File Name: download_xkcd.py
# Contact: 958000432@qq.com
# Created Time: 2018/4/22 上午12:32
# Version: 1.0
# Description:
#
# Change Activities:
#           2018/4/22:
# ======================================================================================================================

import requests
import os
import bs4


def main():
    url = 'http://xkcd.com'

    os.makedirs('xkcd', exist_ok=True)

    while not url.endswith('#'):
        print("Downloading page {}".format(url))

        res = requests.get(url)

        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        comicElem = soup.select('#comic img')

        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')

            print("Downloading image {}".format(comicUrl))

            res = requests.get(comicUrl)

            res.raise_for_status()

            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

            for chunk in res.iter_content(10000):
                imageFile.write(chunk)

            imageFile.close()

        prevLink = soup.select('a[rel="prev"]')[0]

        url = 'http://xkcd.com' + prevLink.get('href')


if __name__ == '__main__':
    main()



