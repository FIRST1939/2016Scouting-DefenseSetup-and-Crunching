# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:00:31 2016

@author: Victoria Cook

This will track the defensive alignments for both alliances in the FRC 2016 
game Stronghold.
"""
#!/usr/bin/env python 

import tkinter as tk

root = tk.Tk()
app = tk.Frame(root)

app.master.title('Please don\'t crash on me')

top = app.winfo_toplevel()
top.rowconfigure(1,weight=1)
top.columnconfigure(1,weight=1)

quitButton = tk.Button(text = 'Quit', command=tk._exit)
quitButton.grid(column=1, row=1, sticky=tk.N+tk.S+tk.E+tk.W,padx=3)




















app.mainloop()
                                

