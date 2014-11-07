#!/usr/bin/env python3

import os
from argparse import ArgumentParser

###File with same name already exists?

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

###cleaner
def parlour(path):
    print(path)
    with open(path, "r") as fobj:

        filename = "Hot" + path.split("/")[-1]
        flag = existanceCheck(path, filename)
        
        if (flag == 0):
            return

        for lines in fobj:
            if not ("*" in lines and ("joined" in lines or "quit" in lines or "left" in lines or "known" in lines)):
                with open(filename, "a") as beauty:
                    beauty.write(lines)
    return

# Clening a directory containing log files.
def logDirectory(path):
    newpath = path.rstrip(path.split('/')[-1]) + 'Hot' + path.split('/')[-1]
    os.mkdir(newpath)
    os.chdir(newpath)
    for i in os.listdir(path):
        filepath = path + '/' + i
        parlour(filepath)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-l", dest="FileLocation", help="Location of IRC log file requiring  beauty treatment")
    parser.add_argument("-d", dest="Directory", nargs='?', help="Location directory of IRC log file requiring  beauty treatment")
    args = parser.parse_args()

    if (args.FileLocation):
        parlour(args.FileLocation)

    elif(args.Directory):
        direcpath = args.Directory
        if args.Directory[-1] == '/':
            direcpath = args.Directory.rstrip('/')
        logDirectory(direcpath)

    else:
        print("Address of file/directory please...(try -h option for help)")
