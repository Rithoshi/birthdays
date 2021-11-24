#! /usr/bin/env python3

from mypackage import firstmodule
import sys


if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    print("Give me a name to test")
    exit()

firstmodule.return_birthday(name)

