from tkinter import *
from tkinter import messagebox
import csv
import re

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
  "Takes an object[list/dict] to write to the specified .csv file"
  raw = open(filename, "w")
  write = csv.writer(raw)
  raw.close()

def retreive_entry(event):
  "Takes the widgets value and retreives the corresponding value from glossary"
  raw = event.widget.get()
  if raw == "?":
    event.widget.delete(0, len(event.widget.get()))
    event.widget.insert(0, "Place a `+` symbol before the entry to add it to the file. Press <Tab> to clear the field.")
  else:
    try:
      data = glossary[raw]
    except:
      #messagebox.showerror("Err 404","Definition not found :(")
      event.widget.delete(0, len(event.widget.get()))
      event.widget.insert(0, "Oops, looks like that definition couldn't be found!")
    else:
      #messagebox.showinfo("Meaning:", data)
      event.widget.delete(0, len(event.widget.get()))
      event.widget.insert(0, data)

def add_entry(event):
  "Adds a new entry into the .csv file"
  raw = event.widget.get()

def parse_entry(event):
  raw = event.widget.get()

def clear_entry(event):
  event.widget.delete(0, len(event.widget.get()))

def build_widgets(window):
  "Renders and packs the widget elements onto the screen"
  l1 = Label(window, text = "Enter a term to search, then press Return to execute the query.")
  l1.pack(side = TOP)
  e1 = Entry(window, exportselection = 0, justify=CENTER)
  e1.pack(side = BOTTOM, expand = 1, fill = "x")
  e1.bind("<Return>", retreive_entry)
  e1.bind("<Tab>", clear_entry)

app = Tk()
win = Frame(app)
win.pack()
app.title("Glossary")
app.maxsize(500,50)
pull_data("glossary.csv")

build_widgets(win)

win.mainloop()
