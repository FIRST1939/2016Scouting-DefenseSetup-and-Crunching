# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:00:31 2016

@author: Victoria Cook

This will track the defensive alignments for both alliances in the FRC 2016 
game Stronghold.


Still needs doing: 
- add match number tracking to display and increment on save, 
- actually pick a defense not a placeholder, 
- get the save button to save current defense settings not placeholder line, 
- allow selection of match number.

Future enhancements:
- End swap button
- Defense images and general prettiness

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
#blue2 = tk.StringVar()
currentObstacles = [tk.IntVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(),
                    # match #,   audience,       blue2,       ,  blue4
                    tk.StringVar(), tk.StringVar(), tk.StringVar(),
                    #blue5,         red2,           red4
                    tk.StringVar()]
                    #red5
filename = tk.StringVar()    


def saveCurrentMatch(matchData, filename):
    '''(list, str)-> None
    Takes the list containing the current matchdata and appends it to filename.
    '''

    #outstr = str(matchData)+'\n'

    outlist = []
    
    for item in matchData:
        outlist.append(item.get())
        
    outstr = str(outlist).strip('[]')+'\n'
    
    matchData[0].set(matchData[0].get() + 1)
    matchLabel.config(text=matchData[0].get())
        
    file=open(filename, mode='a')
    file.write(outstr)
    file.close()

def setDefenseValue(targetvar, targetLabel, secondLabel=None):
    '''(stringvar) -> None
    Sets the variable to selected defense and updates
    '''
    targetvar.set('B1') #COOK need to actually pick a real defense here

#    targetLabel.config(text=blue2.get())
    targetLabel.config(text=targetvar.get())

    if secondLabel != None:
        secondLabel.config(text=targetvar.get())

def setSaveFile(filename, matchnum, matchLabel):
    '''(tk.StringVar, tk.IntVar)-> Nonetype
    
    Does a dialog to set the savefile, and initializes match number to 1.
    '''
    
    savefile = fd.asksaveasfilename(title='Save filename',
                                    filetypes=[('Text CSV', '.csv')])+'.csv'    
    filename.set(savefile)
    matchnum.set(1)                          
    matchLabel.config(text=matchnum.get())


# command using lambda to prevent instant execution if function has parms
# http://stackoverflow.com/questions/8269096/why-is-button-parameter-command-executed-when-declared

matchWord = tk.Label(text='Match', font=('Helvetica','16'))
matchWord.grid(column=3, row=1)
matchLabel = tk.Label(text = 'Set Savefile', 
                      font=('Helvetica','16'))
matchLabel.grid(column=3, row=2, padx=7)


fileButton = tk.Button(top, text = 'Set savefile', 
                       command=lambda: setSaveFile(filename, 
                                                   currentObstacles[0],
                                                   matchLabel))
fileButton.grid(column=6, row=1, padx=7)

saveButton = tk.Button(top, text = 'Save data',
                       command=lambda: saveCurrentMatch(currentObstacles,
                                                        filename.get()))
saveButton.grid(column=6, row=4, padx=7, sticky=tk.N+tk.S)

blue1Spot = tk.Label(top, relief='groove',
                     bg='Blue', fg='White',text = 'Low Bar', padx=10,pady=10)
                     #image=tk.PhotoImage(file='.\images\lowbar.gif'))
                     #bitmap=tk.BitmapImage(file='.\images\lowbar.bmp'))
                     
#COOK I want to display a graphic of the low bar.  Instead I get a blank cell
#     the size of the low bar. Subbing in text for the moment
blue1Spot.grid(column=2, row=6, sticky=tk.N+tk.S+tk.E+tk.W)


#blue2 = tk.StringVar()
blue2Button = tk.Label(top, bg='Blue', fg='White', padx=10, pady=10,
#                        textvariable = blue2.get())
                       text = 'Placeholder')
blue2Button.grid(column=2, row=5, sticky=tk.N+tk.S+tk.E+tk.W)

#changeB2 = tk.Button(top, command = lambda: setDefenseValue(blue2, blue2Button), text = 'Set')
changeB2 = tk.Button(top, command = lambda: setDefenseValue(currentObstacles[2], 
                                                            blue2Button), 
                                                            text = 'Set')
changeB2.grid(column = 1, row = 5, padx = 10)


blue3Spot = tk.Label(top, relief='groove',
                     bg='Blue', fg='White',text = 'Audience Defense', padx=10,pady=10)
blue3Spot.grid(column=2, row=4, sticky=tk.N+tk.S+tk.E+tk.W)

blue4Button = tk.Label(top, bg='Blue', fg='White', padx=10, pady=10,
                        text = 'Placeholder' )
blue4Button.grid(column=2, row=3, sticky=tk.N+tk.S+tk.E+tk.W)
changeB4 = tk.Button(top, command = lambda: setDefenseValue(currentObstacles[3], 
                                                            blue4Button), 
                                                            text = 'Set')
changeB4.grid(column = 1, row = 3, padx = 10)

blue5Button = tk.Label(top, bg='Blue', fg='White', padx=10, pady=10,
                        text = 'Placeholder' )
blue5Button.grid(column=2, row=2, sticky=tk.N+tk.S+tk.E+tk.W)
changeB5 = tk.Button(top, command = lambda: setDefenseValue(currentObstacles[4], 
                                                            blue5Button), 
                                                            text = 'Set')
changeB5.grid(column = 1, row = 2, padx = 10)

audienceButton = tk.Button(top, bg='Purple', fg='White', padx=10, pady=10,
                           text = 'Set Audience Pick',
                           command = lambda: setDefenseValue(currentObstacles[1], 
                                                            blue3Spot, red3Spot))

                           
audienceButton.grid(column=3, row=3, rowspan=2, sticky=tk.E+tk.W, padx=10,pady=10)

red1Spot = tk.Label(top, relief='groove',
                     bg='Red', fg='White',text = 'Low Bar', padx=10,pady=10)
#COOK Fix image with blue1Spot
red1Spot.grid(column=4, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

red2Button = tk.Label(top, bg='red', fg='White', padx=10, pady=10,
                      text = 'Placeholder')
red2Button.grid(column=4, row=2, sticky=tk.N+tk.S+tk.E+tk.W)

changeR2 = tk.Button(top, command = lambda: setDefenseValue(currentObstacles[5], 
                                                            red2Button), 
                                                            text = 'Set')
changeR2.grid(column = 5, row = 2, padx = 10)


red3Spot = tk.Label(top, relief='groove',
                     bg='red', fg='White',text = 'Audience Defense', padx=10,pady=10)
red3Spot.grid(column=4, row=3, sticky=tk.N+tk.S+tk.E+tk.W)

red4Button = tk.Label(top, bg='red', fg='White', padx=10, pady=10,
                        text = 'Placeholder' )
red4Button.grid(column=4, row=4, sticky=tk.N+tk.S+tk.E+tk.W)
changeR4 = tk.Button(top, command = lambda: setDefenseValue(currentObstacles[6], 
                                                            red4Button), 
                                                            text = 'Set')
changeR4.grid(column = 5, row = 4, padx = 10)

red5Button = tk.Label(top, bg='red', fg='White', padx=10, pady=10,
                        text = 'Placeholder' )
red5Button.grid(column=4, row=5, sticky=tk.N+tk.S+tk.E+tk.W)
changeR5 = tk.Button(top, command = lambda: setDefenseValue(currentObstacles[7], 
                                                            red5Button), 
                                                            text = 'Set')
changeR5.grid(column = 5, row = 5, padx = 10)


# Runs the application
app.mainloop()
                                

