#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    try:
        import pocketsphinx as ps
        import sphinxbase

    except:
        print("""Pocket sphinx and sphixbase is not installed
        in your system. Please install it with package manager.""")

    hmmd = "/usr/share/pocketsphinx/hmm/fr_FR/"
    lmd = "/usr/share/pocketsphinx/lm/fr_FR/"
    dictp = "/usr/share/pocketsphinx/lm/fr_FR/"
    speechRec = ps.Decoder(hmm = hmmd, lm = lmdir, dict = dictp)
