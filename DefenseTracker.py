# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:00:31 2016

@author: Victoria Cook

This will track the defensive alignments for both alliances in the FRC 2016 
game Stronghold.
"""
#!/usr/bin/env python 

import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
app = tk.Frame(root)

app.master.title('Defense Location Tracker v0.1')

top = app.winfo_toplevel()
top.rowconfigure(20,weight=5)
top.columnconfigure(50,weight=1)
blue2 = tk.StringVar()

def saveCurrentMatch(matchData, filename):
    '''(list, str)-> None
    Takes the list containing the current matchdata and appends it to filename.
    '''
    
    file=open(filename, mode='a')
    outstr = str(matchData)+'\n'
    file.write(outstr)
    file.close()

def setDefenseValue(targetvar, targetLabel):
    '''(stringvar) -> None
    Sets the variable to selected defense and updates
    '''
    targetvar.set('B1')

    targetLabel.config(text=blue2.get())
    

#from tkinter import *



filename = tk.StringVar()

# command using lambda to prevent instant execution if function has parms
# http://stackoverflow.com/questions/8269096/why-is-button-parameter-command-executed-when-declared

fileButton = tk.Button(top, text = 'Set savefile', 
                       command=lambda: filename.set(fd.asksaveasfilename(title='Save filename',
                                                                         filetypes=[('Text CSV', '.csv')])
                                                    +'.csv'))
fileButton.grid(column=6, row=1, padx=7)

saveButton = tk.Button(top, text = 'Save data',
                       command=lambda: saveCurrentMatch(['1','B1','A2','C1','D1','A1','C2','D2'],
                                                        filename.get()))
saveButton.grid(column=6, row=4, padx=7, sticky=tk.N+tk.S)

blue1Spot = tk.Label(top, relief='groove',
                     bg='Blue', fg='White',text = 'Low Bar', padx=10,pady=10)
                     #image=tk.PhotoImage(file='.\images\lowbar.gif'))
                     #bitmap=tk.BitmapImage(file='.\images\lowbar.bmp'))
                     
#COOK I want to display a graphic of the low bar.  Instead I get a blank cell
#     the size of the low bar. Subbing in text for the moment
blue1Spot.grid(column=2, row=6, sticky=tk.N+tk.S+tk.E+tk.W)


#COOK This button does nothing and displays no text
#blue2 = tk.StringVar()
blue2Button = tk.Label(top, bg='Blue', fg='White', padx=10, pady=10,
                        #command = lambda: blue2.set('B1'), 
                        textvariable = blue2.get())
                     #image=tk.PhotoImage(file='.\images\lowbar.gif'))
                     #bitmap=tk.BitmapImage(file='.\images\lowbar.bmp'))
blue2Button.grid(column=2, row=5, sticky=tk.N+tk.S+tk.E+tk.W)

changeB2 = tk.Button(top, command = lambda: setDefenseValue(blue2, blue2Button), text = 'Set')
changeB2.grid(column = 1, row = 5, padx = 10)

#COOK Everything after this point is placeholder and will need fixing
blue3Spot = tk.Label(top, relief='groove',
                     bg='Blue', fg='White',text = 'Audience Defense', padx=10,pady=10)
blue3Spot.grid(column=2, row=4, sticky=tk.N+tk.S+tk.E+tk.W)

blue4Button = tk.Button(top, bg='Blue', fg='White', padx=10, pady=10,
                        text = 'Placeholder' )
blue4Button.grid(column=2, row=3, sticky=tk.N+tk.S+tk.E+tk.W)

blue5Button = tk.Button(top, bg='Blue', fg='White', padx=10, pady=10,
                        text = 'Placeholder' )
blue5Button.grid(column=2, row=2, sticky=tk.N+tk.S+tk.E+tk.W)

audienceButton = tk.Button(top, bg='Purple', fg='White', padx=10, pady=10,
                           text = 'Placeholder' )
                           
audienceButton.grid(column=3, row=3, rowspan=2, sticky=tk.E+tk.W, padx=10,pady=10)

red1Spot = tk.Label(top, relief='groove',
                     bg='Red', fg='White',text = 'Low Bar', padx=10,pady=10)
#COOK Fix image with blue1Spot
red1Spot.grid(column=4, row=1, sticky=tk.N+tk.S+tk.E+tk.W)



# Runs the application
app.mainloop()
                                

