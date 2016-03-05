# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:12:28 2016

"""

import urllib.request
import json
import pprint

URL = 'http://www.thebluealliance.com/api/v2/'

'''
X-TBA-App-Id is required by the blue alliance api for tracking
Default User-Agent value causes 403 Forbidden so I pretend to be a browser.
'''
REQHEADERS = {'X-TBA-App-Id': 'vhcook-frc1939:scouting:1',
              'User-Agent': 'Mozilla/5.0'}
              
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
    
def get_event_list(year):
    fullurl = URL + 'events/' + str(year)
    print(fullurl)
    result = get_request(fullurl)
    return result


'mokc'

def get_event_teams(event, year):
    event_key = str(year) + event
    fullurl = URL + 'event/' + event_key + '/teams'
    print(fullurl)
    result = get_request(fullurl)
    return result
