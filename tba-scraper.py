# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:12:28 2016

@author: stat
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
              


#returns the dictionary for a request for a team
def get_team(team_num):
    fullurl = URL + 'team/frc' + str(team_num)
    request = urllib.request.Request(fullurl, headers = REQHEADERS)
    response = urllib.request.urlopen(request)
    jsonified = json.loads(response.read().decode("utf-8"))
    return jsonified