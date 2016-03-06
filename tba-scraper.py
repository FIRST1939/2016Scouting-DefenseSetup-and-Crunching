# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:12:28 2016

"""

import urllib.request
import json
from pprint import pprint
from tkinter import filedialog as fd

URL = 'http://www.thebluealliance.com/api/v2/'

'''
X-TBA-App-Id is required by the blue alliance api for tracking
Default User-Agent value causes 403 Forbidden so I pretend to be a browser.
'''
REQHEADERS = {'X-TBA-App-Id': 'vhcook-frc1939:scouting:1',
              'User-Agent': 'Mozilla/5.0'}
              
DEFENSES = ['A_Portcullis','A_ChevalDeFrise','B_Ramparts','B_Moat',
            'C_Drawbridge','C_SallyPort','D_RoughTerrain', 'D_RockWall',
            'E_LowBar', 'NotSpecified']    
            
DONE = ['scmb','casd','mndu','mndu2','onto2','mike2','misou','mista','miwat',
        'waamv','waspo','ctwat','ncmcl','nhgrs','njfla','pahat','vahay'
        ]
              
def get_request(fullurl):
    request = urllib.request.Request(fullurl, headers = REQHEADERS)
    response = urllib.request.urlopen(request)
    jsonified = json.loads(response.read().decode("utf-8"))
    return jsonified


def get_team(team_num):
    fullurl = URL + 'team/frc' + str(team_num)
    result = get_request(fullurl)
    return result
   
    
def get_team_bots(team_num):
    fullurl = URL + 'team/frc' + str(team_num) + '/history/robots'
    print(fullurl)
    result = get_request(fullurl)
    return result
    
def get_team_history(team_num):
    fullurl = URL + 'team/frc' + str(team_num) + '/history/events'
    print(fullurl)
    result = get_request(fullurl)
    return result


def get_award_history(team_num):    
    fullurl = URL + 'team/frc' + str(team_num) + '/history/awards'
    print(fullurl)
    result = get_request(fullurl)
    return result

def get_team_year(team_num, year):
    fullurl = URL + 'team/frc' + str(team_num) + '/' + str(year) + '/events'
    print(fullurl)
    result = get_request(fullurl)
    return result
    
def get_event_list(year=2016):
    fullurl = URL + 'events/' + str(year)
    print(fullurl)
    result = get_request(fullurl)
    return result

def get_event_teams(event, year=2016):
    event_key = str(year) + event
    fullurl = URL + 'event/' + event_key + '/teams'
    print(fullurl)
    result = get_request(fullurl)
    return result

def get_event_matches(event, year=2016):
    event_key = str(year) + event
    fullurl = URL + 'event/' + event_key + '/matches'
    print(fullurl)
    result = get_request(fullurl)
    return result
    
def get_event_stats(event, year=2016):
    #OPR, DPR, CCWM
    event_key = str(year) + event
    fullurl = URL + 'event/' + event_key + '/stats'
    print(fullurl)
    result = get_request(fullurl)
    return result    

def analyze_matches(event, year=2016):
    '''
    Take match data for event and find things
    
    Crossings per defense
    Crossings per position
    Crossings per defense in position
    '''
    
    data = get_event_matches(event, year)
    print('Analyzing', event, '\n')    
    
    #pprint(data[0])
    dcrossed={}
    dpositions={}
    
    for match in data:
        if match['alliances']['blue']['score'] == -1:
            #print('Defect in',match['match_number'])
            continue
        for alliance in ['red', 'blue']:
            if 'E_LowBar' not in dcrossed:
                dcrossed['E_LowBar'] = []
            dcrossed['E_LowBar'].append(match['score_breakdown'][alliance]['position1crossings'])
            for pos in range(2, 6):
                spot = str(pos)
                d = match['score_breakdown'][alliance]['position'+spot]
                if d not in dpositions:
                    dpositions[d] = []
                    dcrossed[d] = []
                dpositions[d].append(spot)
                dcrossed[d].append(match['score_breakdown'][alliance]['position'+spot+'crossings'])
                
                if d == 'NotSpecified':
                    print('Missing Defense Info:', match['match_number'], alliance, pos)
       
    return (dpositions, dcrossed)    
 
def defposit(positions, event, year=2016, write=None):
    '''
    Determine times each defense is in each position at an event
    '''
    
    dpos = {}
    cksum = [0,0,0,0]
    
    if write != None:
        filename = open(write, mode='a')

    for defense in DEFENSES:
        if defense not in positions:
            continue
        if defense not in dpos:
            dpos[defense] = [0,0,0,0,0]
            
        if defense != 'E_LowBar':
            for spot in positions[defense]:
                dpos[defense][int(spot) - 1] += 1
            
            total = 0
            for i in dpos[defense]:
                total += i
            print(defense, total)
            if defense[0] == 'A':
                cksum[0] += total
            elif defense[0] == 'B':
                cksum[1] += total
            elif defense[0] == 'C':
                cksum[2] += total
            elif defense[0] == 'D':
                cksum[3] += total
            else:
                print(defense, 'Category not found')
                
        if write != None:
            outtext = event + ',' +defense + ',' + str(dpos[defense]).strip('[]') + '\n'
            filename.write(outtext)
    
    if write != None:
        filename.close()
            
    #pprint(dpos)
    print('Category checksums', cksum)
    
def defcrossings(crossings, positions, event, write=None)            :
    '''
    Take crossing data for an event, and determine defense durability
    '''
    print('\nEvaluating Crossings\n')
    dcross = {}
    dbreach = {}
    
    if write != None:
        filename = open(write, mode='a')    
    
    for defense in DEFENSES:
        if defense not in crossings:
            continue
        
        if defense not in dcross:
            dcross[defense] = [0,0,0,0,0]
            dbreach[defense] = [0,0,0,0,0]
            
        if defense == 'E_LowBar':
            for i in range(len(crossings[defense])):
                dcross[defense][0] += crossings[defense][i]
                if crossings[defense][i] == 2:
                    dbreach[defense][0] += 1
        else:
            assert len(crossings[defense]) == len(positions[defense])
            for i in range(len(crossings[defense])):
                pos = int(positions[defense][i]) - 1
                dcross[defense][pos] += crossings[defense][i]
                if crossings[defense][i] == 2:
                    dbreach[defense][pos] += 1
        print(defense, dcross[defense])

        if write != None:
            outtext = event + ',crossing,' +defense + ',' + str(dcross[defense]).strip('[]') + '\n'
            filename.write(outtext)
            outtext = event + ',breach,' +defense + ',' + str(dbreach[defense]).strip('[]') + '\n'
            filename.write(outtext)
    
    if write != None:
        filename.close()
        
def quickevents():        
    eventlist = get_event_list()
    
    for event in eventlist:
        print(event['short_name'], event['event_code'])
        
        
#writefile = fd.asksaveasfilename(title='Save defense usage')      
crossfile = fd.asksaveasfilename(title='Save crossing success')      
  
for thing in DONE:
    positions, crossings = analyze_matches(thing)
    #defposit(positions, thing, write=writefile)
    defposit(positions, thing)
    #defcrossings(crossings, positions, thing)
    defcrossings(crossings, positions, thing, write=crossfile)
        
        
        
        
        
        
        
        
        