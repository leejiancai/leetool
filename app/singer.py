from __future__ import absolute_import
import tool1
from app.shell import Shell
import sys

def main():
    shell = Shell(tool1)
    shell.run(sys.argv[1:])


if __name__ == '__main__':
    main()