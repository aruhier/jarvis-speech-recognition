#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import dbus


def play():
    bus = dbus.SessionBus()
    banshee = bus.get_object("org.bansheeproject.Banshee", "/org/bansheeproject/Banshee/PlayerEngine")
    banshee.Play()

def pause():
    bus = dbus.SessionBus()
    banshee = bus.get_object("org.bansheeproject.Banshee", "/org/bansheeproject/Banshee/PlayerEngine")
    banshee.Pause()

def read(music):
    bus = dbus.SessionBus()
    banshee = bus.get_object("org.bansheeproject.Banshee", "/org/bansheeproject/Banshee/PlayerEngine")
    banshee.Open(music)
    banshee.Play()
