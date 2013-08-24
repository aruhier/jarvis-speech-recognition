#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import dbus

BUS = dbus.SessionBus()

def next() :
    banshee = BUS.get_object("org.bansheeproject.Banshee", "/org/bansheeproject/Banshee/PlaybackController")
    banshee.Next(True)

def pause():
    banshee = BUS.get_object("org.bansheeproject.Banshee", "/org/bansheeproject/Banshee/PlayerEngine")
    banshee.Pause()

def play():
    banshee = BUS.get_object("org.bansheeproject.Banshee", "/org/bansheeproject/Banshee/PlayerEngine")
    banshee.Play()

def previous() :
    banshee = BUS.get_object("org.bansheeproject.Banshee", "/org/bansheeproject/Banshee/PlaybackController")
    banshee.Previous(True)

def read(music):
    banshee = BUS.get_object("org.bansheeproject.Banshee", "/org/bansheeproject/Banshee/PlayerEngine")
    banshee.Open(music)
    banshee.Play()
