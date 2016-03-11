# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:43:37 2016


Output from match scouting system

result = [lblAutoTeamNo1.Text, lblAutoD1Cross.Text, lblAutoD1Reach.Text, 
          lblAutoD2Cross.Text, lblAutoD2Reach.Text, lblAutoD3Cross.Text, 
          lblAutoD3Reach.Text, lblAutoD4Cross.Text, lblAutoD4Reach.Text, 
          lblAutoD5Cross.Text, lblAutoD5Reach.Text, lblAutoHighShotMade, 
          lblAutoHighShotAtt, lblAutoLowShotMade, lblAutoLowShotAtt, 
          lblAutoTotalPoints.Text, lblTeleOpD1Cross.Text, lblTeleOpD1Att.Text, 
          lblTeleOpD2Cross.Text, lblTeleOpD2Att.Text, lblTeleOpD3Cross.Text, 
          lblTeleOpD3Att.Text, lblTeleOpD4Cross.Text, lblTeleOpD4Att.Text, 
          lblTeleOpD5Cross.Text, lblTeleOpD5Att.Text, lblChallengeScale.Text, 
          lblTeleOpD4Att.Text, lblChallengeScale.Text, lblTeleOpHighShotMade, 
          lblTeleOpHighShotAtt, lblTeleOpLowShotMade, lblTeleOpLowShotAtt, 
          lblTeleOpTotalPoints.Text, lblTotalPoints.Text, lblDefense.Text, 
          lblmatch.Text]

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
            
from pprint import pprint
            
def getData():
    '''
    Pulls data from match schedule, defense tracker, and match scouting files.
    '''
    from tkinter import filedialog
    
    defensefilename = filedialog.askopenfilename(title='Defense File')
    defensefile = open(defensefilename, newline = '')
    #defensereader = csv.reader(defensefile, delimiter = ',')
    
    #defenses = []
    #for row in defensereader:
    #    defenses.append(row)
     
    defensestr = defensefile.readlines()
    defensefile.close()
    defenses = []
    
    for line in defensestr:        
        defenses.append(line.replace(' ','').replace('\'','').rstrip('\r\n').split(sep=','))
        
    
    scoutfilename = filedialog.askopenfilename(title='Scout File')
    
    
    
    
    
    
    pass

def comboResult():
    '''
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
    '''
    pass

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