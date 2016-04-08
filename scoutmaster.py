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
    '''(pd.DataFrame) -> pd.DataFrame
    
    Takes the dataframe and calculates crossing and reach totals, then
    recalculates auton and teleop scoring.
    '''
    
    # If any of the autonomous crossings have a positive value, score a crossing    
    
    
    df['AutoCross'] = np.logical_or(              np.logical_or(np.greater(df.AutoD1Cross, 0),
                                                                np.greater(df.AutoD2Cross, 0)),
                                    np.logical_or(np.logical_or(np.greater(df.AutoD3Cross, 0),
                                                                np.greater(df.AutoD4Cross, 0)),
                                                  np.greater(df.AutoD5Cross, 0)))

    df['AutoReach'] = np.logical_or(              np.logical_or(np.greater(df.AutoD1Reach, 0),
                                                                np.greater(df.AutoD2Reach, 0)),
                                    np.logical_or(np.logical_or(np.greater(df.AutoD3Reach, 0),
                                                                np.greater(df.AutoD4Reach, 0)),
                                                  np.greater(df.AutoD5Reach, 0)))

    # Multiply each scoring activity by its value and sum

    autodf = pd.DataFrame({'AutoCross': df.AutoCross,
                           'AutoReach': df.AutoReach,
                           'AutoHighShotMade': df.AutoHighShotMade,
                           'AutoLowShotMade': df.AutoLowShotMade})
                           
    # This automatically alphabetizes to                            
    # AutoCross  AutoHighShotMade  AutoLowShotMade AutoReach                           
    autoscore = [10, 10, 5, 2]

    df['AutoTotalPoints'] = np.dot(autodf, autoscore)
     
    autodf['AutoTotalPoints'] = np.dot(autodf, autoscore)
    
    # No more than two crossings per defense for scoring
    
    crosser = pd.DataFrame({'TeleOpD1Cross': np.clip(df.TeleOpD1Cross, 0, 2),
                            'TeleOpD2Cross': np.clip(df.TeleOpD2Cross, 0, 2),
                            'TeleOpD3Cross': np.clip(df.TeleOpD3Cross, 0, 2),
                            'TeleOpD4Cross': np.clip(df.TeleOpD4Cross, 0, 2),
                            'TeleOpD5Cross': np.clip(df.TeleOpD5Cross, 0, 2)})
                            
    df['TeleCross'] = np.dot(crosser,[1,1,1,1,1])
    
    df['TeleCrossRaw'] = df['TeleOpD1Cross'] + df['TeleOpD2Cross'] + df['TeleOpD3Cross'] + df['TeleOpD4Cross'] + df['TeleOpD5Cross']
    
    challenges = np.equal(df.ChallengeScale, 1)
    scales = np.equal(df.ChallengeScale, 2)
    
    teledf = pd.DataFrame({'Crossings': df.TeleCross,
                           'HighShot': df.TeleOpHighShotMade,
                           'LowShot': df.TeleOpLowShotMade,
                           'Challenge': challenges,
                           'Scale': scales})

    #Challenge  Crossings  HighShot  LowShot  Scale
    telescore = [5, 5, 5, 2, 15]    

    df['TeleOpTotalPoints'] = np.dot(teledf, telescore)
    
    teledf['TeleTotal'] = np.dot(teledf, telescore)
    
    
    df['TotalPoints'] = np.add(df.AutoTotalPoints, df.TeleOpTotalPoints)
    
    print('\nMath Check\n')
    
    print(teledf)
    print('\n')
                        

    return df

def patchDefenses(df, defenses):
    '''(pd.DataFrame, pd.DataFrame) -> pd.DataFrame
    '''
    redloc = ['E_LowBar', 'Red2', 'Zone3Shared', 'Red4', 'Red5']
    blueloc = ['E_LowBar', 'Blue2', 'Zone3Shared', 'Blue4', 'Blue5']
    
    #'A_Portcullis','A_ChevalDeFrise','B_Ramparts','B_Moat',
    #        'C_Drawbridge','C_SallyPort','D_RoughTerrain', 'D_RockWall',

    
    tgtmeas = ['AutoD1Cross', 'AutoD1Reach', 'AutoD2Cross', 'AutoD2Reach',
               'AutoD3Cross', 'AutoD3Reach', 'AutoD4Cross', 'AutoD4Reach',
               'AutoD5Cross', 'AutoD5Reach', 'TeleOpD1Cross', 'TeleOpD1Att',
               'TeleOpD2Cross', 'TeleOpD2Att', 'TeleOpD3Cross', 'TeleOpD3Att',
               'TeleOpD4Cross', 'TeleOpD4Att', 'TeleOpD5Cross', 'TeleOpD5Att']
               
    dloc = []
    
    for item in df['measurement']:
        if item[0] == 'A' and item[5].isdigit():
            dloc.append(int(item[5]))
        elif item[0] == 'T' and item[7].isdigit():
            dloc.append(int(item[7]))
        else:
            dloc.append(None)
    
    df['dloc'] = dloc


    
    bluedefs = defenses.loc[:, ('Match', 'Zone3Shared', 'Blue2', 'Blue4', 'Blue5')]
    reddefs = defenses.loc[:, ('Match', 'Zone3Shared', 'Red2', 'Red4', 'Red5')]
    
    bluedefs['Alliance'] = 'blue'
    
    #print(bluedefs.columns, reddefs.columns)
    
    bluedefs.columns = ['Match', 3, 2, 4, 5, 'Alliance']
    reddefs['Alliance'] = 'red'
    
    reddefs.columns = ['Match', 3, 2, 4, 5,'Alliance']
    
    glueme = [bluedefs, reddefs]
    alldefs = pd.concat(glueme)
    
    alldefs[1] = 'E_LowBar'
    
    colordefs = pd.melt(alldefs, id_vars= ['Match', 'Alliance'], var_name = 'dloc')
    
    colordefs.columns = ['Match','Alliance','dloc','DefType']
    
    print('\n Applying Defenses to Matches \n')
    
    print(colordefs.head(), '\n', colordefs.tail(), '\n')

    #Make sure that the measurements that aren't for defenses have no location
    
    #df['DefType'] = None  
    
    #df.ix[df.dloc == 1, 'DefType'] = 'E_LowBar'
    
    outdf = pd.merge(df, colordefs, how='left', on=('Match', 'Alliance', 'dloc'))
    
    print(outdf.head())
        
    return outdf            

def comboResult(defenses, scoutdata, matchlist):
    '''(pd.DataFrame, pd.DataFrame) -> pd.DataFrame
    Combines match schedule, defense tracker, and match scouting data into a 
    match result dataframe that is melted for easier analysis.
    '''
    print('Defenses:', defenses.columns, '\nData:', scoutdata.columns, '\nMatches:', matchlist.columns)
    
    bigdf = pd.merge(scoutdata, matchlist, on=('Match','Team'))
    
    print('\nJoined DataFrames:\n')

    allcalc = calcValues(bigdf)

                                       
    print(allcalc.head())
    
    flatterdf = pd.melt(allcalc, id_vars=['Match', 'Team', 'Alliance'], var_name='measurement')
    
    print('\nMelted DataFrames\n')
    print(flatterdf.head())
    
    print('\nPatching Defenses\n')
    
    allstuff = patchDefenses(flatterdf, defenses)
    
    return allstuff

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
    crunchings = comboResult(df1, df2, df3)
    
    crunchings.to_csv('C://Users//stat//Documents//GitHub//2016Scouting-DefenseSetup-and-Crunching//QC Data//qcfriday.csv')