#! /usr/bin/env python3

from mypackage import firstmodule
import argparse
import pandas as pd

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-name", 
                        help="Insert please the name that you want to test")
    parser.add_argument("-g", help="Get the known VIP", action="store_true")                    
    parser.add_argument("-v", help="Be more verbose", action="store_true")

    args = parser.parse_args()
    return args
    
arg=parse_arguments()
name=arg.name
v=arg.v
if v:
    print("Verbosity turned on")
if arg.g:
    firstmodule.print_birthdays()
if name != None:
    firstmodule.return_birthday(name,v)

