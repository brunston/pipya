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
from urllib.request import urlopen
import json
import os, sys
import feedparser
import webbrowser

if os.name == "nt":
    try:
        from colorama import init
        init()
    except ImportError:
        print("colorama is a windows dependency for ANSI colors support")
        sys.exit()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def kernfig():
  with open("settings.cfg") as file:
    config = [line.rstrip('\n') for line in file]
    with open("api.key") as file:
      wlist = [line.rstrip('\n') for line in file]
  wapi = wlist[0]
  user = config[0]
  citystr = config[1]
  newslink = config[2]
  return (wapi,user,citystr,newslink)

def todaysdate():
  return datetime.now()

def grab(link):
  return feedparser.parse(link)

def template():
  print("""

""")
  return None

def cfgwriter(inputs,lineno,text):
  """Writes text to given config file in inputs on line lineno"""
  tmp = str(inputs+".tmp")
  with open(inputs) as fin, open(tmp,'w') as fout:
    count = 0
    for line in fin:
      if count == lineno:
        fout.write(text+"\n")
      else:
        fout.write(line)
      count += 1
  with open(tmp) as fin, open(inputs,'w') as fout:
    for line in fin:
      fout.write(line)
  return None

def wloader(typeofdata):
  f = urlopen(typeofdata)
  json_string = f.read()
  json_middleman = json_string.decode("utf-8")
  parsed_json = json.loads(json_middleman)
  return parsed_json

def giveComputerIndex(uin):
  return [int(s) for s in uin.split() if s.isdigit()]

#TEXT TEXT TEXT TEXT TEXT

def pipya():
  return bcolors.HEADER + "Pipya: " + bcolors.ENDC

def welcome(user):
  print(pipya() + bcolors.OKBLUE + """\
Hi {0}! It's {1}. What can I do for you?
Don't forget, you can always ask me what I can do.
My keywords are 'fetch' and 'set'
""".format(user, todaysdate()) + bcolors.ENDC)
  return None

def ask():
  ask = pipya() + bcolors.OKBLUE + "What's up? " + bcolors.ENDC
  return ask

def rt(thing):
  print(pipya() + bcolors.OKBLUE +\
     "Here's what you asked for: {0}!".format(thing) +\
     bcolors.ENDC)
  return None

def capabilities():
  print(pipya() + bcolors.OKBLUE +"""\
\n-Here's what I can do:
-interpret (to a certain degree) plain-english commands
-fetch news headlines from NPR and the Atlantic
-fetch the weather
"""
+ bcolors.ENDC)
  return None

def wcurre(parsed_json):
  print(pipya() + bcolors.OKBLUE +\
                "Weather in " +\
                parsed_json["location"]["city"] +\
                " now: " +\
                parsed_json["current_observation"]["weather"]+ " at " +\
                parsed_json["current_observation"]["temperature_string"] +\
                bcolors.ENDC)
  return None

def wforec(parsed_json):
  print(pipya() + bcolors.OKBLUE +\
                  "Weather in " +\
                  parsed_json["location"]["city"] +\
                  " soon:\n" +\
                  parsed_json["forecast"]["txt_forecast"]["forecastday"][1]["title"]+\
                  "- " +\
                  parsed_json["forecast"]["txt_forecast"]["forecastday"][1]["fcttext"]+\
                  "\n" +\
                  parsed_json["forecast"]["txt_forecast"]["forecastday"][2]["title"]+\
                  "- " +\
                  parsed_json["forecast"]["txt_forecast"]["forecastday"][2]["fcttext"]+\
                  "\n" +\
                  parsed_json["forecast"]["txt_forecast"]["forecastday"][4]["title"]+\
                  "- " +\
                  parsed_json["forecast"]["txt_forecast"]["forecastday"][4]["fcttext"]+\
                  bcolors.ENDC)
  return None

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