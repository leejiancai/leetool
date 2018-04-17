#!/bin/env python
from __future__ import absolute_import
from tool1.printer import Printer

def main():
    p = Printer("lijiancai")
    p.my_print()

if __name__ == '__main__':
    main()