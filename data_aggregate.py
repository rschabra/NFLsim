from sportsipy.nfl.teams import Teams
from csv import writer
from array import *

teams2020 = Teams(year = '2020')
elems = [0]*48
props = ['name', 'assists_on_tackles', 'attempted_passes', 'completed_passes', 'extra_points_attempted',
        'extra_points_made', 'field_goals_attempted', 'field_goals_made', 'fumbles', 'fumbles_forced', 
        'fumbles_recovered', 'fumbles_recovered_for_touchdown', 'interceptions', 'interceptions_returned_for_touchdown', 'interceptions_thrown', 
        'kickoff_return_touchdown', 'kickoff_return_yards', 'kickoff_returns', 'longest_interception_return', 'longest_kickoff_return', 
        'longest_pass', 'longest_punt', 'longest_punt_return', 'longest_reception', 'longest_rush', 'passes_defended', 'passing_touchdowns', 
        'passing_yards', 'punt_return_touchdown', 'punt_return_yards', 'punt_returns', 'punts', 'quarterback_rating', 'receiving_touchdowns', 'receiving_yards',
        'receptions', 'rush_attempts', 'rush_touchdowns', 'rush_yards', 'sacks', 'times_pass_target', 'times_sacked', 'total_punt_yards', 'yards_per_punt', 
        'yards_per_punt_return', 'yards_recovered_from_fumble', 'yards_returned_from_interception']

with open('/Users/rohanchabra/nflwinnersim/player_data.csv', 'w', newline='') as write_arr:
        csv_writer = writer(write_arr)
        csv_writer.writerow(['team.name'] + props)

def append_arr_as_row(file_name, arr_elem, newline=''):
    with open(file_name, 'a+', newline='') as write_arr:
        csv_writer = writer(write_arr)
        csv_writer.writerow(arr_elem)

for team in teams2020:
    elems[0] = team.name
    for player in team.roster.players:
        g = 1
        for prop in props:
            try:
                elems[g] = getattr(player, prop)
            except:
                elems[g] = 0
            g += 1
        append_arr_as_row('/Users/rohanchabra/nflwinnersim/player_data.csv', elems)
   

