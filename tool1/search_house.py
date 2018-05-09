# -*- coding: utf-8 -*-

import requests
import json
import traceback
import re

g_key = '8fd06ddb39f6343537fe973f3a0170'
g_address = '大厦'
g_city = '广州'
DEBUG = True


class GetLocationMan(object):
    def __init__(self, key, address, city):
        self.key =  key
        self.city = city
        self.loc = None
        self.address = address
        self.re_filters = []
        self.re_filters.append(
            re.compile(ur'\(.*\)')
        )
        self.re_filters.append(
            re.compile(ur'（.*）')
        )
        self.re_filters.append(
            re.compile(ur'花园')
        )
        self.re_filters.append(
            re.compile(ur'小区')
        )
        self.re_filters.append(
            re.compile(ur'社区')
        )

    @staticmethod
    def get_dic_from_url(url):
        try:
            res = requests.get(url)

            res.raise_for_status()

            if DEBUG:
                print(res.text)

            res_dic = json.loads(res.text)

            status = res_dic['status']

            if status != '1':
                print("Get loction status is not 1")
                return None

            return res_dic

        except Exception as e:
            traceback.print_exc()
            print(e)
            return None

    def get_location(self, address, city):

        url = 'http://restapi.amap.com/v3/geocode/geo?key={key}&address={address}&city={city}'.format(
            key=g_key, address=address, city=city
        )

        dic = self.get_dic_from_url(url)
        if not dic:
            return None

        try:
            return dic['geocodes'][0]['location']

        except Exception as e:
            traceback.print_exc()
            print(e)
            return None

    @classmethod
    def get_near_districts(cls, loc, radius):

        names = []
        first = True
        page = 1
        count = 0
        while True:

            url = 'http://restapi.amap.com/v3/place/around?key={key}&location={loc}&output=json&radius={radius}&types' \
                  '=小区&offset=25&page={page}'.format(key=g_key, loc=loc, radius=radius, page=page)

            dic = cls.get_dic_from_url(url)

            # 第一次获取的时候，先获取一下有多少个结果
            while first:
                first = False
                count = dic.get('count', 25)
                count = int(count)
            if not dic:
                return None

            try:
                pois = dic['pois']

                for pos in pois:
                    print(pos['name'])
                    names.append(pos['name'])
                # todo 减少调用次数，先返回第一页
                return names

            except Exception as e:
                traceback.print_exc()
                print(e)
                return names

            count -= 25

            if count <= 0:
                return names

            page += 1

    def district_clen(self, pos):

        for ref in self.re_filters:
            pos = ref.sub(ur'', pos)

        return pos

    def get_loc(self):
        self.loc = self.get_location(self.address, self.city)
        if not self.loc:
            return None

        districts = self.get_near_districts(self.loc, 2000)

        output = map(self.district_clen, districts)

        return output


def main():

    locMan = GetLocationMan(g_key, g_address, g_city)

    output = locMan.get_loc()

    print("after clean")
    for i in output:
        print(i)



if __name__ == '__main__':
    main()
