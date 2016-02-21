# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:00:31 2016

@author: Victoria Cook

This will track the defensive alignments for both alliances in the FRC 2016 
game Stronghold.
"""
#!/usr/bin/env python 

import tkinter as tk
from tkinter import filedialog

def saveCurrentMatch(matchData, filename):
    '''(list, str)-> None
    Takes the list containing the current matchdata and appends it to filename.
    '''
    
    file=open(filename, mode='a')
    outstr = str(matchData)+'\n'
    file.write(outstr)
    file.close()

#from tkinter import *

root = tk.Tk()
app = tk.Frame(root)

app.master.title('Defense Location Tracker v0.1')

top = app.winfo_toplevel()
top.rowconfigure(1,weight=1)
top.columnconfigure(1,weight=1)

filename = tk.StringVar()

# command using lambda to prevent instant execution if function has parms
# http://stackoverflow.com/questions/8269096/why-is-button-parameter-command-executed-when-declared

fileButton = tk.Button(root, text = 'Set savefile', 
                       command=lambda: filename.set(filedialog.asksaveasfilename(title='Save filename',
                                                                                 filetypes=[('Text CSV', '.csv'),('All Files', '.*')])+'.csv'))
fileButton.grid(column=1, row=1, sticky=tk.N+tk.S, padx=7)

saveButton = tk.Button(root, text = 'Save data',
                       command=lambda: saveCurrentMatch(['1','B1','A2','C1','D1','A1','C2','D2'],filename.get()))
saveButton.grid(column=2, row=1, padx=7)













app.mainloop()
                                

