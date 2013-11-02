#!/usr/bin/python2
# -*- coding: utf-8 -*-

import match

while True:
    try:
        request = raw_input(" > ")
    except KeyboardInterrupt:
        break
    match.search(request)

print("\nBye !")
