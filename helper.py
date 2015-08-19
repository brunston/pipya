# -*- coding: utf-8 -*-
"""
pipya helper file
Copyright (c) 2015 Brunston Poon
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Full license in LICENCE.txt
"""

from datetime import datetime
import feedparser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def todaysdate():
	return datetime.now()

def grab(link):
	return feedparser.parse(link)

def template():
	print("""

""")
	return None

#TEXT TEXT TEXT TEXT TEXT

def pipya():
  return bcolors.HEADER + "Pipya: " + bcolors.ENDC

def welcome(user):
	print(pipya() + bcolors.OKBLUE + """\
Hi {0}! It's {1}. What can I do for you?
""".format(user, todaysdate()) + bcolors.ENDC)
	return None

def ask():
	ask = pipya() + bcolors.OKBLUE + "What's up? " + bcolors.ENDC
	return ask

def rt(thing):
	print(pipya() + bcolors.OKBLUE +\
		 "Here's what you asked for: {0}!".format(thing) +\
		 bcolors.ENDC)

def jellyfish():
	print("""
                
                                        (hello!)
                                      .'
                                     '
                      _ -- ~~~ -- _      _______
                  .-~               ~-.{__-----. :
                /                       \      | |
               :         O     O         :     | |
               /\                       /------' j
              { {/~-.      \__/      .-~\~~~~~~~~~
               \/ /  |~:- .___. -.~\  \  \.
              / /\ \ | | { { \ \  } }  \  \.
             { {   \ \ |  \ \  \ \ /    } }
              \ \   /\ \   \ \  /\ \   { {
               } } { { \ \  \ \/ / \ \  \ \.
              / /   } }  \ \ }{ {    \ \ } }
             / /   { {     \ \{\ \    } { {
            / /     } }     } } \  / / \ \ \.
           `-'     { {     `-'\ \`-'/ /   `-'
                    `-'        `-' `-'

                    unknown artist
                """)
	return "jellyfish"