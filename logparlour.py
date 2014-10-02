#!/usr/bin/env python3

import os
from argparse import ArgumentParser


def existanceCheck(path, filename):
    name = str(path.split("/")[-1])
    path = path.rstrip(name)

    for content in os.listdir(path):
        if (content == filename):
            choice = input("File already exists...Overright[y/n]: ")

            if (choice == "y"):
                os.remove(path+filename)
                return 1
            else:
                return 0


def parlour(path):

    with open(path, "r") as fobj:

        filename = "Hot" + args.FileLocation.split("/")[-1]
        flag = existanceCheck(path, filename)
        
        if (flag == 0):
            return

        for lines in fobj:
            if not ("*" in lines and ("joined" in lines or "quit" in lines or "left" in lines or "known" in lines)):
                with open(filename, "a") as beauty:
                    beauty.write(lines)
    return



if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-l", dest="FileLocation", help="Location of IRC log file requiring  beauty treatment")
    args = parser.parse_args()

    if (args.FileLocation):
        parlour(args.FileLocation)

    else:
        print("Complete address of the lady please...(try -h option for help)")
