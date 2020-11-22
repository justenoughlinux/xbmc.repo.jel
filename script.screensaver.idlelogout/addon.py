#!/usr/bin/python

import xbmc

class idlelogout(xbmc.Monitor):
        xbmc.executebuiltin("System.Logoff()")

xbmclogoff = idlelogout()
del xbmclogoff
