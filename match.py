#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob
import os
import re

## CheckData(fileName)
#
# Check if the file doesn't contain any error

def checkData(aliasFile):
    source = open(aliasFile, "r")
    line = source.readline()
    error = False
    checkReqAction = False
    action = False
    req = False
    tempBracket = 0
    currentLineNb = 1

    while line and not error :
        bo = line.find('{')
        bc = line.find('}')

        if checkReqAction :
            error = action and re.match("^\s*action=", line)
            action = action or bool(re.match("^\s*action=", line))
            req = req or bool(re.match("^\s*req=", line))

        elif bo != -1 :
            error = (tempBracket == 1)
            tempBracket = 1
            checkReqAction = True

        elif bc != -1 :
            error = (tempBracket == 0)
            error = error or not action or not req
            tempBracket = 0
            checkReqAction = False

        line = source.readline()
        currentLineNb += 1

    if error:
        print("Error in file " + aliasFile + ", line %s.\n" %(currentLineNb-1))

    return error


## search(request_to_search, dataFileName)
#
# Search the request in the data file sent in parameter

def search(request, aliasFile):
    if checkData(aliasFile) :
        return -1

    source = open(aliasFile, "r")
    tempSearch = ""
    action = ""
    line = source.readline()

    while not tempSearch and line:
        tempSearch = re.match("^\s*req=" + request, line)

        if tempSearch and request :
            tempAction = ""
            while not tempAction and line and line.find("}") == -1 :
                line = source.readline()
                tempAction = re.match("^\s*action=", line)
            action = line.rstrip('\t')[len(tempAction.group(0)):]

        else :
            line = source.readline()

    if action:
        eval(action)
    source.close()


## main(request)
#
# Main function, launches the request search

def main(request):
    aliasFiles = glob.glob('data/*.txt')

    for aliasFile in aliasFiles:
        search(request, aliasFile)

main("Salut Jarvis")
