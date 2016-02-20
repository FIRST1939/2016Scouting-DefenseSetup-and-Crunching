This repo contains two major programs.  DefenseTracker.py will have the code to track defenses throughout a regional for scouting.  Scoutmaster.py will have the code to combine the results file from DefenseTracker with the main Scouting system output file, and possibly results from pit scouting.

Coding for Groups in all programs is as follows:

A1 Portcullis
A2 Cheval de Frise
B1 Moat
B2 Ramparts
C1 Drawbridge
C2 Sally Port
D1 Rock Wall
D2 Rough Terrain
E1 Low Bar

unless I decide to go with

{'A': ('Portcullis', 'Cheval de Frise'), 'B': ('Moat','Ramparts'), 'C': ('Drawbridge','Sally Port'), 'D': ('Rock Wall','Rough Terrain'), 'E': ('Low Bar')}

DefenseTracker:

The position 1 defense is always the low bar.  Position 3 is audience selected and the same for both alliances and will change once every N matches, where N is the number required for all teams at the regional to have seen the selection once.  First audience grouping will be randomly selected and will advance alphabetically through defense groups A-D.



Output file will contain a CSV with the following header format:

     Match#,Zone3Shared,Red2,Red4,Red5,Blue2,Blue4,Blue5


Sample output:
Match#,Zone3Shared,Red2,Red4,Red5,Blue2,Blue4,Blue5
1,B1,A1,C2,D2,C1,A2,D2
2,B1,C1,A1,D1,A2,D2,C1



