# import json file 
import json


# load competition data
with open('D:/football-data-exploration/datasets/statsBomb/data/competitions.json', encoding='utf-8') as f:
    competitions: list = json.load(f)

# Afcon 2023
competitions_id= 1267

#Load the list of matches for this competitions
with open('D:/football-data-exploration/datasets/statsBomb/data/matches/'+str(competitions_id)+'/107.json', encoding='utf-8') as f:
    matches: list = json.load(f) 
    
#Look inside matches
matches[0]
matches[0]['home_team']
matches[0]['home_team']['home_team_name']
matches[0]['away_team']['away_team_name']

# Print all match results 
for match in matches:
    home_team_name = match['home_team']['home_team_name']
    away_team_name = match['away_team']['away_team_name']
    home_score = match['home_score']
    away_score = match['away_score']
    describe_text = 'The match between ' + home_team_name + ' and ' + away_team_name + ' '
    result_text = 'finished ' + str(home_score) + ':' + str(away_score)
    print(describe_text + result_text)
    
# Next, we find a match we are interested in
home_team_required = 'Nigeria'
away_team_required = "Côte d'Ivoire"
match_id_required = None
# Find ID for the match
for match in matches :
    home_team_name = match['home_team']['home_team_name']
    away_team_name = match['away_team']['away_team_name']
    if(home_team_name==home_team_required) and (away_team_name==away_team_required):
        match_id_required = match['match_id']
        print(home_team_required + ' vs ' + away_team_required + ' has id:' + str(match_id_required))
        break

# After the loop, check if found
if match_id_required is None:
    print('No match id found')
