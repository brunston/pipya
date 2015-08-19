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
import sys
#import configparser
import time
import feedparser

import helper as h

toggle = True
version = sys.version_info[0]
if version != 3:
    print("""
Please upgrade to Python3, preferably 3.4.* or greater, before continuing""")
    toggle = False
    sys.exit()

def main():
    with open("settings.cfg") as file:
        config = [line.rstrip('\n') for line in file]
    user = config[0]
    h.welcome(user)

    while True:
        with open("settings.cfg") as file:
            config = [line.rstrip('\n') for line in file]
        user = config[0]
        uin = str.lower(input(h.ask()))
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

        elif "name" and "pronounce" in uin:
            print(h.pipya()+"My name is pronounced Pip-pah. The y is silent :).")

        elif "name" and ("how" or "where") and "get" in uin:
            print(h.pipya()+"""\
My name started as pypa, for "python personal assistant". It morphed to pipya
for pronounceability. Thanks for asking!""")

        elif uin in ["q", "quit", "exit", "goodbye"]:
            print("Goodbye, {0}! 'Till next time.".format(user))
            sys.exit()

        elif uin in ["jellyfish"]:
            h.jellyfish()

        else:
            print("Pipya: Sorry, {0}, I didn't quite catch that.".format(user))

if (__name__ == '__main__') and (toggle==True):
    main()