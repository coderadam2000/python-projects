from tkinter import *
import requests
import json
from urllib.request import urlopen
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

root = Tk()
root.title('Dictionary')

Definition = Label(root,
            text = '')

def define(word2def):
    global Definition
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + str(word2def)
    res = urlopen(url)
    j = json.loads(res.read())

    data = json.dumps(j)

    i=data.find("definition\"")
    j=data.find("example")
    k=data.find("synonyms")

    prefix_num = 1

    if j == -1:
        j=k

    output = str(prefix_num)+ ". "
    output += data[i+14:j-4].capitalize()

    definitions = True

    while(definitions == True):
        newi=data.find("definition\"",i+14)
        i=newi
        if newi != -1:
            definitions = True
            j=data.find("example", j+4)
            k=data.find("synonyms")
            if j == -1:
                j=k
            output += "\n"
            prefix_num += 1
            output += str(prefix_num)+ ". "
            output += data[newi+14:j-4].capitalize()
        else:
            definitions = False

    Definition.destroy()

    Definition = Label(root,
            text = output, justify = LEFT)

    Definition.grid(row = 1, column = 0)
    

word = Entry(root, width = 50)
check = Button(root, text = 'define', command = lambda: define(word.get()))
word.grid(row = 0, column = 0)
check.grid(row = 0, column = 1)


root.mainloop()
