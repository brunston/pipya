# -*- coding: utf-8 -*-
"""
pipya fetch file
Copyright (c) 2015 Brunston Poon
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Full license in LICENCE.txt
"""
import sys, os
import time
import json
import webbrowser
import feedparser
import helper as h

def main(uin):
    wapi, user, citystr = h.kernfig()[0:3]
    if "headlines" in uin:
        if "npr" in uin:
            h.rt(uin)
            link = "http://www.npr.org/rss/rss.php?id=1001"
            newsfeed = h.grab(link)
            for i in range(10):
                print("Item {0}: ".format(i+1) + h.bcolors.BOLD +\
                  newsfeed.entries[i].title +\
                  h.bcolors.ENDC)
                print("Time Published ",newsfeed.entries[i].published)
        elif "atlantic" in uin:
            h.rt(uin)
            link = "http://feeds.feedburner.com/TheAtlantic?format=xml"
            newsfeed = h.grab(link)
            for i in range(10):
                print("Item {0}: ".format(i+1) + h.bcolors.BOLD +\
                  newsfeed.entries[i].title +\
                  h.bcolors.ENDC)
                print("Time Published: ",newsfeed.entries[i].published)
        else:
            print(h.pipya() + "Defaulting to NPR!")
            link = "http://www.npr.org/rss/rss.php?id=1001"
            newsfeed = h.grab(link)
            for i in range(10):
                print("Item {0}: ".format(i+1) + h.bcolors.BOLD +\
                  newsfeed.entries[i].title +\
                  h.bcolors.ENDC)
                print("Time Published ",newsfeed.entries[i].published)
        h.cfgwriter("settings.cfg",2,link)

    elif "weather" in uin:
        currentcond = str('http://api.wunderground.com/api/'+wapi+\
                    '/geolookup/conditions/q/'+citystr+'.json')
        parsed_json = h.wloader(currentcond)
        h.wcurre(parsed_json)

        currentforec = str('http://api.wunderground.com/api/'+wapi+\
                    '/geolookup/forecast/q/'+citystr+'.json')
        parsed_json = h.wloader(currentforec)
        h.wforec(parsed_json)
    return None