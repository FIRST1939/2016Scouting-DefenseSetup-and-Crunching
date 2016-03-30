This repo contains three major programs.  

DefenseTracker.py will have the code to track defenses throughout a regional for scouting.  

	Requires: Python3

Scoutmaster.py will have the code to combine the results file from DefenseTracker with the main Scouting system output file, and possibly results from pit scouting.
	Requires: Python3, numpy, pandas

TBA-scraper.py pulls data from TBA and does various things with it.
	Requires: Python3

Coding for Groups in all programs will match TBA's format:

['A_Portcullis','A_ChevalDeFrise','B_Ramparts','B_Moat','C_Drawbridge','C_SallyPort','D_RoughTerrain', 'D_RockWall','E_LowBar', 'NotSpecified']


DefenseTracker:

The position 1 defense is always the low bar.  Position 3 is audience selected and the same for both alliances and will change once every N matches, where N is the number required for all teams at the regional to have seen the selection once.  First audience grouping will be randomly selected and will advance alphabetically through defense groups A-D.



Output file will contain a CSV with the following header format:

     Match#,Zone3Shared,Red2,Red4,Red5,Blue2,Blue4,Blue5


Sample output:
'Match#,Zone3Shared,Blue2,Blue4,Blue5,Red2,Red4,Red5
1, 'A_Portcullis', 'C_Drawbridge', 'D_RoughTerrain', 'B_Ramparts', 'B_Ramparts', 'D_RoughTerrain', 'C_SallyPort'
2, 'A_Portcullis', 'C_Drawbridge', 'B_Ramparts', 'D_RockWall', 'B_Moat', 'C_Drawbridge', 'D_RockWall'

