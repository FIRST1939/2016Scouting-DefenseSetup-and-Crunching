# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:43:37 2016


Output from match scouting system

SCOUTHEADER = ['Team','AutoD1Cross','AutoD1Reach','AutoD2Cross','AutoD2Reach',
               'AutoD3Cross','AutoD3Reach','AutoD4Cross','AutoD4Reach',
               'AutoD5Cross','AutoD5Reach','AutoHighShotMade','AutoHighShotAtt',
               'AutoLowShotMade','AutoLowShotAtt','AutoTotalPoints',
               'TeleOpD1Cross','TeleOpD1Att','TeleOpD2Cross','TeleOpD2Att',
               'TeleOpD3Cross','TeleOpD3Att','TeleOpD4Cross','TeleOpD4Att',
               'TeleOpD5Cross','TeleOpD5Att','ChallengeScale',
               'TeleOpHighShotMade','TeleOpHighShotAtt','TeleOpLowShotMade',
               'TeleOpLowShotAtt','TeleOpTotalPoints','TotalPoints','Defense',
               'Match']   

Output from defense tracker

currentObstacles = [tk.IntVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(),
                    # match #,   audience,       blue2,       ,  blue4
                    tk.StringVar(), tk.StringVar(), tk.StringVar(),
                    #blue5,         red2,           red4
                    tk.StringVar()]
                    #red5

Match schedule
#, R1, R2, R3, B1, B2, B3
                    
What I want to know:

resultDict:
{team: [{match: lblmatch.Text,
        defense: {'A_Portcullis': [present?, autoCross, autoReach, teleCross, teleAtt],
                  'A_ChevalDeFrise': [...],
                  'B_Ramparts': [...],
                  'B_Moat': [...],
                  'C_Drawbridge': [...],
                  'C_SallyPort': [...],
                  'D_RoughTerrain': [...],
                  'D_RockWall': [...],
                  'E_LowBar': [...]},
        goals: {auto: [highMade, highAtt, lowMade, lowAtt],
                tele: [highMade, highAtt, lowMade, lowAtt]}
        endgame: [crossed?, scaled?],
        scoring:[auto, tele, total]},
        {match...}],
team2: [{}]}

teamSummary:
{team: {matchesPlayed: value,
        matchScores[m1, m2, m3, ...],
        defense: {'A_Portcullis': [faced, autoCrosses, autoReaches, teleCross, teleAtt],
                  ...}
        goals: {highMade: total,
                highAtt: total,
                highAcc: highMade / highAtt,
                lowMade: total, 
                lowAtt: total, 
                lowAcc: total}
        
"""

DEFENSES = ['A_Portcullis','A_ChevalDeFrise','B_Ramparts','B_Moat',
            'C_Drawbridge','C_SallyPort','D_RoughTerrain', 'D_RockWall',
            'E_LowBar', 'NotSpecified']  

SCOUTHEADER = ['Team','AutoD1Cross','AutoD1Reach','AutoD2Cross','AutoD2Reach',
               'AutoD3Cross','AutoD3Reach','AutoD4Cross','AutoD4Reach',
               'AutoD5Cross','AutoD5Reach','AutoHighShotMade','AutoHighShotAtt',
               'AutoLowShotMade','AutoLowShotAtt','AutoTotalPoints',
               'TeleOpD1Cross','TeleOpD1Att','TeleOpD2Cross','TeleOpD2Att',
               'TeleOpD3Cross','TeleOpD3Att','TeleOpD4Cross','TeleOpD4Att',
               'TeleOpD5Cross','TeleOpD5Att','ChallengeScale',
               'TeleOpHighShotMade','TeleOpHighShotAtt','TeleOpLowShotMade',
               'TeleOpLowShotAtt','TeleOpTotalPoints','TotalPoints','Defense',
               'Match']           
               
from pprint import pprint
import pandas as pd
import numpy as np

            
def getData():
    '''(None) -> (pd.DataFrame, pd.DataFrame)
    Pulls data from match schedule, defense tracker, and match scouting files.
    '''
    from tkinter import filedialog
    
    defensefilename = filedialog.askopenfilename(title='Defense File')

    defenses = pd.read_csv(defensefilename)
    
    scoutfilename = filedialog.askopenfilename(title='Scout File')
    
    scoutdata = pd.read_csv(scoutfilename, header=None, names=SCOUTHEADER)
    
    matchfilename = filedialog.askopenfilename(title='Match File')
    
    matchdata = pd.read_csv(matchfilename)
    
    return(defenses, scoutdata, matchdata)
    
def calcValues(df):
    
    df['AutoCross'] = np.logical_or(              np.logical_or(np.greater(df.AutoD1Cross, 0),
                                                                np.greater(df.AutoD2Cross, 0)),
                                    np.logical_or(np.logical_or(np.greater(df.AutoD3Cross, 0),
                                                                np.greater(df.AutoD4Cross, 0)),
                                                  np.greater(df.AutoD5Cross, 0)))

    return df


def comboResult(defenses, scoutdata, matchlist):
    '''(pd.DataFrame, pd.DataFrame) -> pd.DataFrame
    Combines match schedule, defense tracker, and match scouting data into a 
    match result dictionary
    
    resultDict:
        {team: [{match: lblmatch.Text,
                 defense: {'A_Portcullis': [present?, autoCross, autoReach, teleCross, teleAtt],
                           'A_ChevalDeFrise': [...],
                      'B_Ramparts': [...],
                      'B_Moat': [...],
                      'C_Drawbridge': [...],
                      'C_SallyPort': [...],
                      'D_RoughTerrain': [...],
                      'D_RockWall': [...],
                      'E_LowBar': [...]},
                 goals: {auto: [highMade, highAtt, lowMade, lowAtt],
                    tele: [highMade, highAtt, lowMade, lowAtt]}
                    endgame: [crossed?, scaled?],
                 scoring:[auto, tele, total]},
                {match...}],
        team2: [{}]}
        
    Or does something like that in pandas
    '''
    print('Defenses:', defenses.columns, '\nData:', scoutdata.columns, '\nMatches:', matchlist.columns)
    
    bigdf = pd.merge(scoutdata, matchlist, on=('Match','Team'))
    
    print('\nJoined DataFrames:\n')

    allcalc = calcValues(bigdf)

                                       
    print(allcalc.head())
    
    flatterdf = pd.melt(allcalc, id_vars=['Match', 'Team', 'Alliance'], var_name='measurement')
    
    print('\nMelted DataFrames\n')
    print(flatterdf.head())

def teamSummary():
    '''
    Takes resultDict and creates a team summary
    teamSummary:
        {team: {matchesPlayed: value,
                matchScores[m1, m2, m3, ...],
                defense: {'A_Portcullis': [faced, autoCrosses, autoReaches, teleCross, teleAtt],
                          ...}
                goals: {highMade: total,
                        highAtt: total,
                        highAcc: highMade / highAtt,
                        lowMade: total, 
                        lowAtt: total, 
                        lowAcc: lowMade / lowAtt}
                endgame: [challenges, scales]},
        }
    '''
    pass

def preMatchSummary():
    '''(matchList, resultDict)
    Prompts user for target match or all future matches for target team
    Pulls team summaries from resultDict, and writes to a file.
    '''
    pass

def pickList():
    pass


def quickrun():
    df1, df2, df3 = getData()
    
    #comboResult(defenses, scoutdata, matchlist)
    comboResult(df1, df2, df3)
    