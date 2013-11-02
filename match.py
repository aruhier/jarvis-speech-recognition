#!/usr/bin/python2
# -*- coding: utf-8 -*-

import glob
import ConfigParser

## CheckData(fileName)
#
# Check if the file doesn't contain any error


def checkData(aliasFile):
    #config = ConfigParser.ConfigParser(strict = True, comment_prefixes=('#'))
    config = ConfigParser.ConfigParser()
    config.read(aliasFile)

    for section in config.sections():
        error = not config.has_option(section, "action")
        error = error or not config.has_option(section, "req1")
        if error:
            break

    return error


## search(request_to_search, dataFileName)
#
# Search the request in the data file sent in parameter

def searchIn(request, aliasFile):
    if checkData(aliasFile):
        print("Error in the database file : " + aliasFile)
        return -1

    # config = ConfigParser.ConfigParser(strict = True)
    config = ConfigParser.ConfigParser()
    config.read(aliasFile)

    action = ""
    module = ""
    requestLower = request.lower()

    for section in config.sections():
        for req in config.options(section):
            if req.startswith('req'):
                found = True
                for word in config.get(section, req).lower().split():
                    found = found and (requestLower.find(word) != -1)
                if found:
                    module = str(config.get(section, "import"))
                    action = str(config.get(section, "action"))

    if module:
        exec("import " + module)
        print("Module imported")

    if action:
        exec(action)
        print(action)
        print("Action set")


## main(request)
#
# Main function, launches the request search

def search(request):
    aliasFiles = glob.glob('data/*.txt')

    for aliasFile in aliasFiles:
        searchIn(request, aliasFile)
