#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob
import os
import re
import configparser

## CheckData(fileName)
#
# Check if the file doesn't contain any error

def checkData(aliasFile):
    error = False
    config = configparser.ConfigParser(strict = True, comment_prefixes=('#'))
    config.read(aliasFile)

    for section in config.sections() :
        error = error or not config.has_option(section, "action")
        error = error or not config.has_option(section, "req1")

    return error


## search(request_to_search, dataFileName)
#
# Search the request in the data file sent in parameter

def search(request, aliasFile):
    if checkData(aliasFile) :
        print("Error")
        return -1

    config = configparser.ConfigParser(strict = True)
    config.read(aliasFile)

    tempSearch = ""
    action = ""

    for section in config.sections() :
        for req in config.options(section) :
            if req.startswith('req') and \
               config.get(section, req).lower() == request.lower() :
                action = str(config.get(section, "action"))

    if action :
        actions = action.split('\n')
        for line in actions:
            eval(line)


## main(request)
#
# Main function, launches the request search

def main(request):
    aliasFiles = glob.glob('data/*.txt')

    for aliasFile in aliasFiles:
        search(request, aliasFile)
