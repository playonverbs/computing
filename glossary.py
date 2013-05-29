"""
file: glossary.py
author: Niam Patel
Description: A(n overly) complex solution to glossaries! More list comprehensions than you can shake a stick at!
Dependencies: Python 3.x with Tcl/Tk support
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
  glossary = dict([(k.strip(), v.strip()) for k, v in glossary.items()])
  raw.close()

def write_data(filename, data):
  "Takes an object[list/dict] to write to the specified .csv file, then calls pull_data()"
  raw = open(filename, "a")
  write = csv.writer(raw)
  write.writerow(data)
  raw.close()
  pull_data(filename)

def retreive_entry(event):
  "Takes the widgets value and retreives the corresponding value from glossary"
  raw = event.widget.get()
  if raw == "?":
    event.widget.delete(0, len(event.widget.get()))
    event.widget.insert(0, "Type the entry, see help page 2 to add definitions. <Tab> clears the field.")
  elif raw == "?1":
    event.widget.delete(0, len(event.widget.get()))
    event.widget.insert(0, "Type added definitions as 'name:definition'")
  elif ':' in raw:
    add_entry(raw)
    event.widget.delete(0, len(event.widget.get()))
  else:
    try:
      data = glossary[raw]
    except:
      event.widget.delete(0, len(event.widget.get()))
      event.widget.insert(0, "Oops, looks like that definition couldn't be found!")
    else:
      event.widget.delete(0, len(event.widget.get()))
      event.widget.insert(0, data)

def add_entry(raw):
  "Parses entry into a list, then calls write_data()"
  data = raw.split(":")
  data[:] = [x.strip() for x in data]
  write_data("glossary.csv", data)

def clear_entry(event):
  "Clear the target entry box"
  event.widget.delete(0, len(event.widget.get()))

def destroy(event):
  "A function to facilitate the closing of the window with a command"
  event.widget.destroy()

def build_widgets(window):
  "Renders and packs the widget elements onto the screen"
  l1 = Label(window, text = "Enter a term to search (use the x:y syntax to add), press Return to query. ? = help:pg1, ?1 = help:pg2")
  l1.pack(side = TOP)
  e1 = Entry(window, exportselection = 0, justify=CENTER)
  e1.pack(side = BOTTOM, expand = 1, fill = "x")
  e1.bind("<Return>", retreive_entry)
  e1.bind("<Tab>", clear_entry)

app = Tk()
win = Frame(app)
win.pack()
app.bind("<Control-q>", destroy)
app.title("Glossary")
app.maxsize(700,50)
pull_data("glossary.csv")

build_widgets(win)

win.mainloop()
