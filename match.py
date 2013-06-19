#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob

def search(request, aliasFile):
    source = open(aliasFile, "r")
    tempSearch = -1
    action = ""
    line = source.readline()

    while tempSearch == -1 and line:
        tempSearch = line.find("req=" + request)
        if tempSearch != -1 and request:
            action = line[tempSearch + len(request) + 2:]
            tempAction = -1
            line = source.readline()
            while tempAction == -1 and line:
                tempAction = line.find("action=")
                action = line.rstrip('\t')[len("    action="):]
                line = source.readline()
        else :
            line = source.readline()

    if action:
        eval(action)
    source.close()


def main(request):
    aliasFiles = glob.glob('data/*.txt')

    for aliasFile in aliasFiles:
        search(request, aliasFile)

main("Bonjour Jarvis")
