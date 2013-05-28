"""
file: glossary.py
author: Niam Patel
Description: A(n overly) complex solution to glossaries! 
"""
from tkinter import *
import csv

glossary = None

def pull_data(filename):
  "Pulls the data from the specified .csv file and parses it into a dict"
  raw = open(filename, "r")
  data = csv.reader(raw)
  data = [row for row in data]
  global glossary
  glossary = dict(data)
  raw.close()

def write_data(filename, data):
  "Takes an object[list/dict] to write to the specified .csv file, then calls pull_data()"
  raw = open(filename, "w")
  write = csv.writer(raw)
  raw.close()

def retreive_entry(event):
  "Takes the widgets value and retreives the corresponding value from glossary"
  raw = event.widget.get()
  if raw == "?":
    event.widget.delete(0, len(event.widget.get()))
    event.widget.insert(0, "Type the entry, then Control-n to add it to the file. <Tab> clears the field.")
  elif raw == "?1":
    event.widget.delete(0, len(event.widget.get()))
    event.widget.insert(0, "Type added definitions as 'name:definition'")
  else:
    try:
      data = glossary[raw]
    except:
      event.widget.delete(0, len(event.widget.get()))
      event.widget.insert(0, "Oops, looks like that definition couldn't be found!")
    else:
      event.widget.delete(0, len(event.widget.get()))
      event.widget.insert(0, data)

def add_entry(event):
  "Parses entry into a list, then calls write_data()"
  raw = event.widget.get()
  data = raw.split(":")
  data[:] = [x.strip() for x in data]
  #key = re.search('^\w*', raw)
  #key = key.group()
  #value = re.search('', raw)
  event.widget.delete(0, len(raw))
  event.widget.insert(0, [d for d in data])

def clear_entry(event):
  "Clear the target entry box"
  event.widget.delete(0, len(event.widget.get()))

def destroy(event):
  "A function to facilitate the closing of the window with a command"
  event.widget.destroy()

def build_widgets(window):
  "Renders and packs the widget elements onto the screen"
  l1 = Label(window, text = "Enter a term to search, then press Return to execute the query. ? = help:pg1, ?1 = help:pg2")
  l1.pack(side = TOP)
  e1 = Entry(window, exportselection = 0, justify=CENTER)
  e1.pack(side = BOTTOM, expand = 1, fill = "x")
  e1.bind("<Return>", retreive_entry)
  e1.bind("<Control-n>", add_entry)
  e1.bind("<Tab>", clear_entry)

app = Tk()
win = Frame(app)
win.pack()
app.bind("<Control-q>", destroy)
app.title("Glossary")
app.maxsize(600,50)
pull_data("glossary.csv")

build_widgets(win)

win.mainloop()
