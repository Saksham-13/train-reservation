
import json

import webbrowser
from json2html import *

with open("trains.json") as file:
    data = json.load(file)
a = json2html.convert(json= data)
f = open('helloworld.html','w')
f.write(a)
f.close()
with open("userinfo1.json") as file1:
    data1 = json.load(file1)
a1 = json2html.convert(json= data1)
f1 = open('helloworld1.html','w')
f1.write(a1)

filename  = "Users/sakshamalok/Desktop/prj/helloworld.html"

webbrowser.open_new_tab(filename)