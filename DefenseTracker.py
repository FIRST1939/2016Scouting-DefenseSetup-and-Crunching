# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:00:31 2016

@author: Victoria Cook

This will track the defensive alignments for both alliances in the FRC 2016 
game Stronghold.


Still needs doing: 
+ add match number tracking to display and increment on save, 
+ actually pick a defense not a placeholder, 
+ get the save button to save current defense settings not placeholder line, 
+ allow selection of match number.

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

currentObstacles = [tk.IntVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(),
                    # match #,   audience,       blue2,       ,  blue4
                    tk.StringVar(), tk.StringVar(), tk.StringVar(),
                    #blue5,         red2,           red4
                    tk.StringVar()]
                    #red5

filename = tk.StringVar()   
 
DEFENSES = ['A_Portcullis','A_ChevalDeFrise','B_Ramparts','B_Moat',
            'C_Drawbridge','C_SallyPort','D_RoughTerrain', 'D_RockWall',
            'E_LowBar', 'NotSpecified']  

def saveCurrentMatch(matchData, filename):
    '''(list, str)-> None
    Takes the list containing the current matchdata and appends it to filename.
    '''
    if len(filename) < 4:
        validSave.config(text='Set Savefile', fg='#ff1212')
        return      
    outlist = []
    validation = []
    
    for item in matchData:
        value = item.get()
        outlist.append(value)
        
        if type(value) == str and len(value) > 1:
            validation.append(value[0])
    
    # Check each alliance for presence of A-D once each
    GOOD = ['A', 'B', 'C', 'D']
    if len(validation) < 7:
        validSave.config(text='Incomplete config', fg='#ff1212')
        return
    blue = validation[0:4]
    red= [validation[0]]
    red.extend(validation[4:]) 
    red.sort()
    blue.sort()
    
   
    if red != GOOD:
        if blue != GOOD:
            validSave.config(text='Configs Invalid', fg='#ff1212')
            return
        else:
            validSave.config(text='Red Config Invalid', fg='#ff1212')
            return      
    elif blue != GOOD:
        validSave.config(text='Blue Config Invalid', fg='#ff1212')
        return         
            
        
    outstr = str(outlist).strip('[]').replace('\'','').replace(' ','')+'\n'
    
        
    #Increment match, save, and output message
    
    matchData[0].set(matchData[0].get() + 1)
    matchLabel.config(text=matchData[0].get())
        
    file=open(filename, mode='a')
    file.write(outstr)
    file.close()
    validSave.config(text='Saved match '+str(outlist[0]), fg='green')

def setDefenseValue(value, targetvar, targetLabel, secondLabel=None):
    '''(stringvar) -> None
    Sets the variable to selected defense and updates
    '''
    
    targetvar.set(value) #COOK need to actually pick a real defense here

    targetLabel.config(text=targetvar.get())

    if secondLabel != None:
        secondLabel.config(text=targetvar.get())

    validSave.config(text='Needs Save', fg='#ff1212')


def setSaveFile(filename, matchnum, matchLabel):
    '''(tk.StringVar, tk.IntVar)-> Nonetype
    
    Does a dialog to set the savefile, and initializes match number to 1.
    '''
    
    savefile = fd.asksaveasfilename(title='Save filename',
                                    filetypes=[('Text CSV', '.csv')])
    if savefile[-4:] != '.csv':
        savefile = savefile + '.csv'
        
    filename.set(savefile)
    matchnum.set(1)                          
    matchLabel.config(text=matchnum.get())
    
    file=open(savefile, mode='a')
    file.write('Match,Zone3Shared,Blue2,Blue4,Blue5,Red2,Red4,Red5\n')
    file.close()

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def Enter(event):

    if RepresentsInt(matchEntry.get()):
        currentObstacles[0].set(int(matchEntry.get()))
        newMatchLabel = tk.Label(text=matchEntry.get())
        matchLabel.config(text=matchEntry.get())

    else:
        newMatchLabel = tk.Label(text='Value Error')
        
    newMatchLabel.grid(column=6,row=4, sticky=tk.W+tk.E)
# command using lambda to prevent instant execution if function has parms
# http://stackoverflow.com/questions/8269096/why-is-button-parameter-command-executed-when-declared

matchWord = tk.Label(text='Match', font=('Helvetica','16'))
matchWord.grid(column=3, row=1)
matchLabel = tk.Label(text = 'Set Savefile', 
                      font=('Helvetica','16'))
matchLabel.grid(column=3, row=2, padx=7)

#This is where I'm trying to update match number on the fly. 
changeLabel = tk.Label(text='Update match number')
changeLabel.grid(column=6,row=2)

newMatchStr = tk.StringVar()
matchEntry = tk.Entry(width = 3)
matchEntry.grid(column=6, row=3, padx=10)
matchEntry.insert(0,newMatchStr.get())
matchEntry.bind('<Return>',Enter)





fileButton = tk.Button(top, text = 'Set savefile', 
                       command=lambda: setSaveFile(filename, 
                                                   currentObstacles[0],
                                                   matchLabel))
fileButton.grid(column=6, row=1, padx=7)

saveButton = tk.Button(top, text = 'Save data',
                       command=lambda: saveCurrentMatch(currentObstacles,
                                                        filename.get()))
saveButton.grid(column=6, row=6, padx=7, sticky=tk.N+tk.S)

blue1Spot = tk.Label(top, relief='groove',
                     bg='Blue', fg='White',text = 'Low Bar', padx=10,pady=10)
                     #image=tk.PhotoImage(file='.\images\lowbar.gif'))
                     #bitmap=tk.BitmapImage(file='.\images\lowbar.bmp'))
                     
#COOK I want to display a graphic of the low bar.  Instead I get a blank cell
#     the size of the low bar. Subbing in text for the moment
blue1Spot.grid(column=2, row=6, sticky=tk.N+tk.S+tk.E+tk.W)



blue2Button = tk.Label(top, bg='Blue', fg='White', padx=10, pady=10,
                       text = 'Placeholder', relief='groove')
blue2Button.grid(column=2, row=5, sticky=tk.N+tk.S+tk.E+tk.W)

changeB2 = tk.Menubutton(top, text = 'Set', relief='raised')
changeB2.grid(column = 1, row = 5, padx = 10)
changeB2.menu = tk.Menu(changeB2)
changeB2['menu'] = changeB2.menu
changeB2.menu.add_radiobutton(label=DEFENSES[0],
                              command = lambda: setDefenseValue(DEFENSES[0],
                                                                currentObstacles[2], 
                                                                blue2Button))
changeB2.menu.add_radiobutton(label=DEFENSES[1],
                              command = lambda: setDefenseValue(DEFENSES[1],
                                                                currentObstacles[2], 
                                                                blue2Button))
changeB2.menu.add_radiobutton(label=DEFENSES[2],
                              command = lambda: setDefenseValue(DEFENSES[2],
                                                                currentObstacles[2], 
                                                                blue2Button))
changeB2.menu.add_radiobutton(label=DEFENSES[3],
                              command = lambda: setDefenseValue(DEFENSES[3],
                                                                currentObstacles[2], 
                                                                blue2Button))
changeB2.menu.add_radiobutton(label=DEFENSES[4],
                              command = lambda: setDefenseValue(DEFENSES[4],
                                                                currentObstacles[2], 
                                                                blue2Button))
changeB2.menu.add_radiobutton(label=DEFENSES[5],
                              command = lambda: setDefenseValue(DEFENSES[5],
                                                                currentObstacles[2], 
                                                                blue2Button))
changeB2.menu.add_radiobutton(label=DEFENSES[6],
                              command = lambda: setDefenseValue(DEFENSES[6],
                                                                currentObstacles[2], 
                                                                blue2Button))
changeB2.menu.add_radiobutton(label=DEFENSES[7],
                              command = lambda: setDefenseValue(DEFENSES[7],
                                                                currentObstacles[2], 
                                                                blue2Button))                                                                
                                                               
blue3Spot = tk.Label(top, relief='groove',
                     bg='Blue', fg='White',text = 'Audience Defense', padx=10,pady=10)
blue3Spot.grid(column=2, row=4, sticky=tk.N+tk.S+tk.E+tk.W)

blue4Button = tk.Label(top, bg='Blue', fg='White', padx=10, pady=10,
                        text = 'Placeholder', relief='groove' )
blue4Button.grid(column=2, row=3, sticky=tk.N+tk.S+tk.E+tk.W)
changeB4 = tk.Menubutton(top, text = 'Set', relief='raised')
changeB4.grid(column = 1, row = 3, padx = 10)
changeB4.menu = tk.Menu(changeB4)
changeB4['menu'] = changeB4.menu
changeB4.menu.add_radiobutton(label=DEFENSES[0],
                              command = lambda: setDefenseValue(DEFENSES[0],
                                                                currentObstacles[3], 
                                                                blue4Button))
changeB4.menu.add_radiobutton(label=DEFENSES[1],
                              command = lambda: setDefenseValue(DEFENSES[1],
                                                                currentObstacles[3], 
                                                                blue4Button))
changeB4.menu.add_radiobutton(label=DEFENSES[2],
                              command = lambda: setDefenseValue(DEFENSES[2],
                                                                currentObstacles[3], 
                                                                blue4Button))
changeB4.menu.add_radiobutton(label=DEFENSES[3],
                              command = lambda: setDefenseValue(DEFENSES[3],
                                                                currentObstacles[3], 
                                                                blue4Button))
changeB4.menu.add_radiobutton(label=DEFENSES[4],
                              command = lambda: setDefenseValue(DEFENSES[4],
                                                                currentObstacles[3], 
                                                                blue4Button))
changeB4.menu.add_radiobutton(label=DEFENSES[5],
                              command = lambda: setDefenseValue(DEFENSES[5],
                                                                currentObstacles[3], 
                                                                blue4Button))
changeB4.menu.add_radiobutton(label=DEFENSES[6],
                              command = lambda: setDefenseValue(DEFENSES[6],
                                                                currentObstacles[3], 
                                                                blue4Button))
changeB4.menu.add_radiobutton(label=DEFENSES[7],
                              command = lambda: setDefenseValue(DEFENSES[7],
                                                                currentObstacles[3], 
                                                                blue4Button)) 

blue5Button = tk.Label(top, bg='Blue', fg='White', padx=10, pady=10,
                        text = 'Placeholder', relief='groove' )
blue5Button.grid(column=2, row=2, sticky=tk.N+tk.S+tk.E+tk.W)

changeB5 = tk.Menubutton(top, text = 'Set', relief='raised')
changeB5.grid(column = 1, row = 2, padx = 10)
changeB5.menu = tk.Menu(changeB5)
changeB5['menu'] = changeB5.menu
changeB5.menu.add_radiobutton(label=DEFENSES[0],
                              command = lambda: setDefenseValue(DEFENSES[0],
                                                                currentObstacles[4], 
                                                                blue5Button))
changeB5.menu.add_radiobutton(label=DEFENSES[1],
                              command = lambda: setDefenseValue(DEFENSES[1],
                                                                currentObstacles[4], 
                                                                blue5Button))
changeB5.menu.add_radiobutton(label=DEFENSES[2],
                              command = lambda: setDefenseValue(DEFENSES[2],
                                                                currentObstacles[4], 
                                                                blue5Button))
changeB5.menu.add_radiobutton(label=DEFENSES[3],
                              command = lambda: setDefenseValue(DEFENSES[3],
                                                                currentObstacles[4], 
                                                                blue5Button))
changeB5.menu.add_radiobutton(label=DEFENSES[4],
                              command = lambda: setDefenseValue(DEFENSES[4],
                                                                currentObstacles[4], 
                                                                blue5Button))
changeB5.menu.add_radiobutton(label=DEFENSES[5],
                              command = lambda: setDefenseValue(DEFENSES[5],
                                                                currentObstacles[4], 
                                                                blue5Button))
changeB5.menu.add_radiobutton(label=DEFENSES[6],
                              command = lambda: setDefenseValue(DEFENSES[6],
                                                                currentObstacles[4], 
                                                                blue5Button))
changeB5.menu.add_radiobutton(label=DEFENSES[7],
                              command = lambda: setDefenseValue(DEFENSES[7],
                                                                currentObstacles[4], 
                                                                blue5Button))
                                                                

audienceButton = tk.Menubutton(top, bg='Purple', fg='White', padx=10, pady=10,
                               text = 'Set Audience Pick', relief='raised')
audienceButton.grid(column=3, row=3, rowspan=2, sticky=tk.E+tk.W, padx=10,pady=10)
audienceButton.menu = tk.Menu(audienceButton)
audienceButton['menu'] = audienceButton.menu
audienceButton.menu.add_radiobutton(label=DEFENSES[0],
                                    command = lambda: setDefenseValue(DEFENSES[0],
                                                                currentObstacles[1], 
                                                                blue3Spot, red3Spot))
audienceButton.menu.add_radiobutton(label=DEFENSES[1],
                                    command = lambda: setDefenseValue(DEFENSES[1],
                                                                currentObstacles[1], 
                                                                blue3Spot, red3Spot))
audienceButton.menu.add_radiobutton(label=DEFENSES[2],
                                    command = lambda: setDefenseValue(DEFENSES[2],
                                                                currentObstacles[1], 
                                                                blue3Spot, red3Spot))
audienceButton.menu.add_radiobutton(label=DEFENSES[3],
                                    command = lambda: setDefenseValue(DEFENSES[3],
                                                                currentObstacles[1], 
                                                                blue3Spot, red3Spot))
audienceButton.menu.add_radiobutton(label=DEFENSES[4],
                                    command = lambda: setDefenseValue(DEFENSES[4],
                                                                currentObstacles[1], 
                                                                blue3Spot, red3Spot))
audienceButton.menu.add_radiobutton(label=DEFENSES[5],
                                    command = lambda: setDefenseValue(DEFENSES[5],
                                                                currentObstacles[1], 
                                                                blue3Spot, red3Spot))
audienceButton.menu.add_radiobutton(label=DEFENSES[6],
                                    command = lambda: setDefenseValue(DEFENSES[6],
                                                                currentObstacles[1], 
                                                                blue3Spot, red3Spot))
audienceButton.menu.add_radiobutton(label=DEFENSES[7],
                                    command = lambda: setDefenseValue(DEFENSES[7],
                                                                currentObstacles[1], 
                                                                blue3Spot, red3Spot))

red1Spot = tk.Label(top, relief='groove',
                     bg='Red', fg='White',text = 'Low Bar', padx=10,pady=10)
red1Spot.grid(column=4, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

red2Button = tk.Label(top, bg='red', fg='White', padx=10, pady=10,
                      text = 'Placeholder', relief='groove')
red2Button.grid(column=4, row=2, sticky=tk.N+tk.S+tk.E+tk.W)

changeR2 = tk.Menubutton(top, text = 'Set', relief='raised')
changeR2.grid(column = 5, row = 2, padx = 10)
changeR2.menu = tk.Menu(changeR2)
changeR2['menu'] = changeR2.menu
changeR2.menu.add_radiobutton(label=DEFENSES[0],
                              command = lambda: setDefenseValue(DEFENSES[0],
                                                                currentObstacles[5], 
                                                                red2Button))
changeR2.menu.add_radiobutton(label=DEFENSES[1],
                              command = lambda: setDefenseValue(DEFENSES[1],
                                                                currentObstacles[5], 
                                                                red2Button))
changeR2.menu.add_radiobutton(label=DEFENSES[2],
                              command = lambda: setDefenseValue(DEFENSES[2],
                                                                currentObstacles[5], 
                                                                red2Button))
changeR2.menu.add_radiobutton(label=DEFENSES[3],
                              command = lambda: setDefenseValue(DEFENSES[3],
                                                                currentObstacles[5], 
                                                                red2Button))
changeR2.menu.add_radiobutton(label=DEFENSES[4],
                              command = lambda: setDefenseValue(DEFENSES[4],
                                                                currentObstacles[5], 
                                                                red2Button))
changeR2.menu.add_radiobutton(label=DEFENSES[5],
                              command = lambda: setDefenseValue(DEFENSES[5],
                                                                currentObstacles[5], 
                                                                red2Button))
changeR2.menu.add_radiobutton(label=DEFENSES[6],
                              command = lambda: setDefenseValue(DEFENSES[6],
                                                                currentObstacles[5], 
                                                                red2Button))
changeR2.menu.add_radiobutton(label=DEFENSES[7],
                              command = lambda: setDefenseValue(DEFENSES[7],
                                                                currentObstacles[5], 
                                                                red2Button))

red3Spot = tk.Label(top, relief='groove',
                     bg='red', fg='White',text = 'Audience Defense', padx=10,pady=10)
red3Spot.grid(column=4, row=3, sticky=tk.N+tk.S+tk.E+tk.W)

red4Button = tk.Label(top, bg='red', fg='White', padx=10, pady=10,
                        text = 'Placeholder', relief='groove' )
red4Button.grid(column=4, row=4, sticky=tk.N+tk.S+tk.E+tk.W)

changeR4 = tk.Menubutton(top, text = 'Set', relief='raised')
changeR4.grid(column = 5, row = 4, padx = 10)
changeR4.menu = tk.Menu(changeR4)
changeR4['menu'] = changeR4.menu
changeR4.menu.add_radiobutton(label=DEFENSES[0],
                              command = lambda: setDefenseValue(DEFENSES[0],
                                                                currentObstacles[6], 
                                                                red4Button))
changeR4.menu.add_radiobutton(label=DEFENSES[1],
                              command = lambda: setDefenseValue(DEFENSES[1],
                                                                currentObstacles[6], 
                                                                red4Button))
changeR4.menu.add_radiobutton(label=DEFENSES[2],
                              command = lambda: setDefenseValue(DEFENSES[2],
                                                                currentObstacles[6], 
                                                                red4Button))
changeR4.menu.add_radiobutton(label=DEFENSES[3],
                              command = lambda: setDefenseValue(DEFENSES[3],
                                                                currentObstacles[6], 
                                                                red4Button))
changeR4.menu.add_radiobutton(label=DEFENSES[4],
                              command = lambda: setDefenseValue(DEFENSES[4],
                                                                currentObstacles[6], 
                                                                red4Button))
changeR4.menu.add_radiobutton(label=DEFENSES[5],
                              command = lambda: setDefenseValue(DEFENSES[5],
                                                                currentObstacles[6], 
                                                                red4Button))
changeR4.menu.add_radiobutton(label=DEFENSES[6],
                              command = lambda: setDefenseValue(DEFENSES[6],
                                                                currentObstacles[6], 
                                                                red4Button))
changeR4.menu.add_radiobutton(label=DEFENSES[7],
                              command = lambda: setDefenseValue(DEFENSES[7],
                                                                currentObstacles[6], 
                                                                red4Button))

red5Button = tk.Label(top, bg='red', fg='White', padx=10, pady=10,
                        text = 'Placeholder', relief='groove' )
red5Button.grid(column=4, row=5, sticky=tk.N+tk.S+tk.E+tk.W)

changeR5 = tk.Menubutton(top, text = 'Set', relief='raised')
changeR5.grid(column = 5, row = 5, padx = 10)
changeR5.menu = tk.Menu(changeR5)
changeR5['menu'] = changeR5.menu
changeR5.menu.add_radiobutton(label=DEFENSES[0],
                              command = lambda: setDefenseValue(DEFENSES[0],
                                                                currentObstacles[7], 
                                                                red5Button))
changeR5.menu.add_radiobutton(label=DEFENSES[1],
                              command = lambda: setDefenseValue(DEFENSES[1],
                                                                currentObstacles[7], 
                                                                red5Button))
changeR5.menu.add_radiobutton(label=DEFENSES[2],
                              command = lambda: setDefenseValue(DEFENSES[2],
                                                                currentObstacles[7], 
                                                                red5Button))
changeR5.menu.add_radiobutton(label=DEFENSES[3],
                              command = lambda: setDefenseValue(DEFENSES[3],
                                                                currentObstacles[7], 
                                                                red5Button))
changeR5.menu.add_radiobutton(label=DEFENSES[4],
                              command = lambda: setDefenseValue(DEFENSES[4],
                                                                currentObstacles[7], 
                                                                red5Button))
changeR5.menu.add_radiobutton(label=DEFENSES[5],
                              command = lambda: setDefenseValue(DEFENSES[5],
                                                                currentObstacles[7], 
                                                                red5Button))
changeR5.menu.add_radiobutton(label=DEFENSES[6],
                              command = lambda: setDefenseValue(DEFENSES[6],
                                                                currentObstacles[7], 
                                                                red5Button))
changeR5.menu.add_radiobutton(label=DEFENSES[7],
                              command = lambda: setDefenseValue(DEFENSES[7],
                                                                currentObstacles[7], 
                                                                red5Button))

validSave = tk.Label(top, text = 'Unsaved', fg='#ff1212', padx=7, pady=5,
                     font=('Helvetica','10'))
validSave.grid(column=6, row=5)

# Runs the application
app.mainloop()
                                

