#!/bin/usr/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Author: lijiancai
# File Name: .py
# Contact: 958000432@qq.com
# Created Time: 2018/4/20 下午11:29
# Version: 1.0
# Description:
#
# Change Activities:
#           2018/4/20:
# ======================================================================================================================

import argparse
import sys
import os


# Decorator for cli-args
def args(*args, **kwargs):
    def _decorator(func):
        # Because of the sematics of decorator composition if we just append
        # to the options list positional options will appear to be backwards.
        func.__dict__.setdefault('arguments', []).insert(0, (args, kwargs))
        return func
    return _decorator


class Shell(object):

    def __init__(self, module):
        self.module = module
        self.submodule_parsers = {}

    def run(self, argv):
        base_parser = self.get_base_parser()

        option, unparsed = base_parser.parse_known_args(argv)

        try:
            parser = self.submodule_parsers[option.submodule]

            sub_module = self._load_submodule(option.submodule)

            sub_parsers = parser.add_subparsers()

            for (action, action_func) in self._mothods_of_obj(sub_module):
                sub_parser = sub_parsers.add_parser(action)
                sub_parser.set_defaults(action_func=action_func)

                # 添加参数
                for each_args, each_kwargs in getattr(action_func, 'arguments', []):
                    sub_parser.add_argument(*each_args, **each_kwargs)

            option = base_parser.parse_args(argv)

            option.action_func(option)


        except Exception as e:
            print(e)
            base_parser.print_help()


    def _mothods_of_obj(self, obj):
        methods = []
        for i in dir(obj):
            attr = getattr(obj, i)
            if callable(attr) and not i.startswith('_'):
                methods.append((i, attr))

        return methods

    def _load_submodule(self, submodule):
        import_path = self.module.__name__ + '.' + submodule
        __import__(import_path)
        return sys.modules[import_path]

    def _find_actions(self, sub):
        pass

    def get_module_submodules(self):
        submodules = []
        files = os.listdir(os.path.dirname(os.path.realpath(self.module.__file__)))
        for f in files:
            if f.endswith(".py"):
                submodules.append(f.replace(".py", ''))

        try:
            submodules.remove('__init__')
        except ValueError as e:
            print(e)

        return submodules

    def get_base_parser(self):
        base_parser = argparse.ArgumentParser()
        sub_parsers = base_parser.add_subparsers()

        for submodule in self.get_module_submodules():
            sub_parser = sub_parsers.add_parser(submodule)

            sub_parser.set_defaults(submodule=submodule)

            self.submodule_parsers[submodule] = sub_parser

        return base_parser


if __name__ == '__main__':
    import tool1
    shell = Shell(tool1)
    shell.run("printer my_print -q 1 1 2".split())