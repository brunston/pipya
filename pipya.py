# -*- coding: utf-8 -*-
"""
pipya main cli file
Copyright (c) 2015 Brunston Poon
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Full license in LICENCE.txt
"""

#IMPORT IMPORT IMPORT IMPORT IMPORT IMPORT IMPORT IMPORT IMPORT IMPORT IMPORT
#Let's make sure that the user has all the dependencies installed and that
#they are running the correct version of Python
try:
    import feedparser
except ImportError:
    print("feedparser is a system-agnostic dependency for RSS support")
    sys.exit()

import sys, os
import time
import json
import helper as h

toggle = True
version = sys.version_info[0]
if version != 3:
    print("""
Please upgrade to Python3, preferably 3.4.* or greater, before continuing""")
    toggle = False
    sys.exit()

if os.name == "nt":
    try:
        from colorama import init
        init()
    except ImportError:
        print("colorama is a windows dependency for ANSI colors support")
        sys.exit()

def main():
    with open("settings.cfg") as file:
        config = [line.rstrip('\n') for line in file]
    with open("api.key") as file:
        wlist = [line.rstrip('\n') for line in file]
    wapi = wlist[0]
    user = config[0]
    citystr = config[1]
    h.welcome(user)

    while True:
        with open("settings.cfg") as file:
            config = [line.rstrip('\n') for line in file]
        user = config[0]
        citystr = config[1]
        print(h.ask())
        uin = str.lower(input(">"))
        if "fetch" in uin:
            if "headlines" in uin:
                if "npr" in uin:
                    h.rt(uin)
                    newsfeed = h.grab("http://www.npr.org/rss/rss.php?id=1001")
                    for i in range(10):
                        print(h.bcolors.BOLD + newsfeed.entries[i].title +\
                              h.bcolors.ENDC)
                        print("Time Published ",newsfeed.entries[i].published)
                elif "atlantic" in uin:
                    h.rt(uin)
                    newsfeed = h.grab(\
                    "http://feeds.feedburner.com/TheAtlantic?format=xml")
                    for i in range(10):
                        print(h.bcolors.BOLD + newsfeed.entries[i].title +\
                              h.bcolors.ENDC)
                        print("Time Published: ",newsfeed.entries[i].published)
                else:
                    print(h.pipya() + "Defaulting to NPR!")
                    newsfeed = h.grab("http://www.npr.org/rss/rss.php?id=1001")
                    for i in range(10):
                        print(h.bcolors.BOLD + newsfeed.entries[i].title +\
                              h.bcolors.ENDC)
                        print("Time Published ",newsfeed.entries[i].published)

            elif "weather" in uin:
                currentcond = str('http://api.wunderground.com/api/'+wapi+\
                            '/geolookup/conditions/q/'+citystr+'.json')
                parsed_json = h.wloader(currentcond)
                h.wcurre(parsed_json)

                currentforec = str('http://api.wunderground.com/api/'+wapi+\
                            '/geolookup/forecast/q/'+citystr+'.json')
                parsed_json = h.wloader(currentforec)
                h.wforec(parsed_json)

        elif "set" in uin:
            if "name" in uin:
                name = input("What would you like me to call you? ")
                h.cfgwriter("settings.cfg",0,name)

            if "city" in uin:
                city = input("""
Changing weather location? Where to?
Must be in Wunderground form. """)
                h.cfgwriter("settings.cfg",1,city)

        elif "name" and "pronounce" in uin:
            print(h.pipya()+"My name is pronounced Pip-pah. The y is silent :).")

        elif "name" and ("how" or "where") and "get" in uin:
            print(h.pipya()+"""\
My name started as pypa, for "python personal assistant". It morphed to pipya
for pronounceability. Thanks for asking!""")

        elif "what" and "can" and "do" in uin:
            h.capabilities()

        elif "who" and "are" and ("you" or "pipya") in uin:
            print(h.pipya()+"""
I am Pipya, a personal assistant written in python3. My creator is brupoon.
He intended for me to be a jack-of-all-trades personal assistant operated by
a cli. I am a sexless, genderless entity, though my name is similar to the
human feminine "Pippa".
                """)

        elif ["quit", "exit", "goodbye"] in uin:
            print("Goodbye, {0}! 'Till next time.".format(user))
            sys.exit()

        elif uin in ["jellyfish"]:
            h.jellyfish()

        else:
            print("Pipya: Sorry, {0}, I didn't quite catch that.".format(user))

if (__name__ == '__main__') and (toggle==True):
    main()