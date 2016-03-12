# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:06:22 2016


fields = [Your Name,Team Number,Match Number,Alliance,Spy Bot,Reached Defense,
          Crossed Defense,High Goals,Low Goals,
          Low Bar,Cheval de Frise,Portcullis,Moat,Ramparts,
          Drawbridge,Sally Port,Rock Wall,Rough Terrain,
          High Goals,High Goal Misses,
          Low Goals,Low Goal Misses,
          Played Defense,Defensive Rating 1-10,
          Fouls Commited,Challenged,Scaled,
          Got Stuck,Yellow Card,Red Card,Notes]
          
          ['Alexey Ayzin', '1769', '6', 'Red', 'False', 'Moat', 'Moat', '0', '0', 
          '2', '0', '0', '0', '0', '1', '0', '0', '0', 
          '0', '0', '2', '1', 
          'False', '0', 
          '0', 
          'False', 'False', 
          'False', 'False', 'False', '\n'] 
"""

def featurecheck(team, teamfeatures):
    if team not in teamfeatures:
        teamfeatures[team] = {}
        
def addfeature(team, teamfeatures, feature):
    if feature not in teamfeatures[team]:
        teamfeatures[team][feature] = []
        
def adddefense(team, teamfeatures, defense, count):
    #print(defense, count)
    if 'defenses' not in teamfeatures[team]:
        teamfeatures[team]['defenses'] = {}
        
    #print(teamfeatures[team]['defenses'])
    if defense not in teamfeatures[team]['defenses']:
        teamfeatures[team]['defenses'][defense] = 0
    teamfeatures[team]['defenses'][defense] += count
    

from pprint import pprint

# For my computer - change to your file location if otherwise located
datafilename = 'C:\\Users\\stat\\Documents\\GitHub\\2016Scouting-DefenseSetup-and-Crunching\\KC Data\\v8 match data - kc friday.csv'

datafile = open(datafilename, mode='r')

data = datafile.readlines()

#print(data[1])

commasep = []

for line in data[1:]:
    splitline = line.split(',', maxsplit = 31)
    commasep.append(splitline)
    
print('Full file length',len(commasep),'\n')

match = []

matchteam = {}
errata = {}

for i in range(len(commasep)):
    if i <= len(commasep): 
        #We're changing the length list as we go - need to stop early
        if len(commasep[i]) < 15:
            problem = commasep.pop(i)
            commasep[i-1].extend(problem)

print('Length after rejoining broken lines', len(commasep))        

omit = []
cleaner = []

for item in commasep:
    if len(item) < 15:
        print('Error', item)
    else:
        mnum = int(item[2])
        team = item[1]

        
        scout = item[0].rstrip(' ')
        
        if mnum == 0 and team == '0':
            
            if scout not in errata:
                errata[scout] = {}
            if 'No match or team number' not in errata[scout]:
                errata[scout]['No match or team number'] = []
            errata[scout]['No match or team number'].append([mnum, team, item[3]])       
            
            omit.append(item)
        
        elif mnum == 0:

            if scout not in errata:
                errata[scout] = {}
            if 'No match number' not in errata[scout]:
                errata[scout]['No match number'] = []
            errata[scout]['No match number'].append([mnum, team, item[3]])
            
            omit.append(item)
        
        elif team == '0':
            
            if scout not in errata:
                errata[scout] = {}
            if 'No team' not in errata[scout]:
                errata[scout]['No team'] = []
            errata[scout]['No team'].append([mnum, team, item[3]])
            
            omit.append(item)
            
        else:
            cleaner.append(item)
        
print('Length after removing items missing either team or match number', len(cleaner))

teamfeatures = {}

for item in cleaner:
    mnum = int(item[2])
    team = item[1]
    
    if team == '60':
        mnum = 60
        team = '5013'
        
    if team == '19884':
        team = '1984'
    
    
    if mnum not in match:
        match.append(mnum)
        matchteam[mnum] = []
    matchteam[mnum].append(team)
    
    featurecheck(team, teamfeatures)
    
    if 'mp' not in teamfeatures[team]:
        teamfeatures[team]['mp'] = 1
    else:      
        teamfeatures[team]['mp'] += 1
    
    if item[4] == 'True':
        addfeature(team, teamfeatures, 'spybot')
        teamfeatures[team]['spybot'].append(mnum)
        
    if item[30] != '\n':
        addfeature(team, teamfeatures, 'notes')
        teamfeatures[team]['notes'].append([mnum, item[30]])
        
    if item[6] != '':
        addfeature(team, teamfeatures, 'autocross')
        teamfeatures[team]['autocross'].append([mnum, item[6]])
        adddefense(team, teamfeatures, item[6], 1)
        
    
    if item[5] != item[6] and item[5] != '':
        addfeature(team, teamfeatures, 'autoreach')        
        teamfeatures[team]['autoreach'].append([mnum, item[5]])        
        
    if (int(item[18]) + int(item[19])) > 0:
        addfeature(team, teamfeatures, 'telehigh')        
        hit = int(item[18])
        miss = int(item[19])
        teamfeatures[team]['telehigh'].append([mnum, str(hit) + '/' + str(hit+miss), str(hit/(hit+miss)*100) + '%' ]) 
    
    if (int(item[20]) + int(item[21])) > 0:
        addfeature(team, teamfeatures, 'telelow')        
        hit = int(item[20])
        miss = int(item[21])
        teamfeatures[team]['telelow'].append([mnum, str(hit) + '/' + str(hit+miss), str(hit/(hit+miss)*100) + '%' ]) 
        
    if item[9] != '0':
        count = int(item[9])
        adddefense(team, teamfeatures,'Low Bar', count)
    if item[10] != '0':
        count = int(item[10])
        adddefense(team, teamfeatures,'Cheval de Frise', count)
    if item[11] != '0':
        count = int(item[11])
        adddefense(team, teamfeatures,'Portcullis', count)
    if item[12] != '0':
        count = int(item[12])
        adddefense(team, teamfeatures,'Moat', count)
    if item[13] != '0':
        count = int(item[13])
        adddefense(team, teamfeatures,'Ramparts', count)
    if item[14] != '0':
        count = int(item[14])
        adddefense(team, teamfeatures,'Drawbridge', count)
    if item[15] != '0':
        count = int(item[15])
        adddefense(team, teamfeatures,'Sally Port', count)
    if item[16] != '0':
        count = int(item[16])
        adddefense(team, teamfeatures,'Rock Wall', count)        
    if item[17] != '0':
        count = int(item[17])
        adddefense(team, teamfeatures,'Rough Terrain', count)     
        
    high = int(item[7])
    low = int(item[8])
    if (high + low) > 0:
        addfeature(team, teamfeatures, 'autoBoulder')     
        if high > 0:
            teamfeatures[team]['autoBoulder'].append([mnum, 'High', high])
        else:
            teamfeatures[team]['autoBoulder'].append([mnum, 'Low', low])
        
        
print('Matches found', len(match))

shortcount = 0
longcount = 0
goodcount = 0

for match in matchteam:
    teams = len(matchteam[match])
    if teams == 6:
        goodcount += 1
    elif teams < 6:
        shortcount += 1
    else:
        longcount += 1

print('Missing teams', shortcount)
print('Too many teams', longcount)
print('Right number of teams', goodcount)

#pprint(errata)    

print('\nErrata summary')    
for person in errata:
    for issue in errata[person]:
        print([person, issue, len(errata[person][issue])])
    

print('\nTeam Features:\n')
pprint(teamfeatures)