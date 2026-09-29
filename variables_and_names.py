#storing values in variables
team = "Toronto Blue Jays" #string value "toronto Blue Jays" is stored in the variable team
current_date = "July 18, 2021" #string value "July 18, 2021" is stored in the variable current_date
player =  "Vladimir Guerrero Jr." #string value "Vladimir Guerrero Jr." is stored in the variable player
home_runs_to_date = 31 #integer value 31 is stored in the variable home_runs_to_date
games_played = 88 #integer value 88 is stored in the variable games_played
total_season_games = 162 #integer value 162 is stored in the variable total_season_games
home_run_record = 73 #integer value 73 is stored in the variable home_run_record

#calculations
games_remaining = total_season_games - games_played #integer value 162 minus 88 (=74) is stored in the variable games_remaining
home_runs_per_game = home_runs_to_date / games_played #integer value 31 divided by 88 (=0.3522727272727273) is stored in the variable home_runs_per_game
projected_home_runs = home_runs_per_game * total_season_games #integer value 0.3522727272727273 multiplied by 162 (=57.09090909090909) is stored in the variable projected_home_runs
can_break_record = projected_home_runs > home_run_record #boolean value True or False (False in this case) depending on the comparison of projected_home_runs and home_run_record is stored in the variable can_break_record

#outputs
print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining, and an average of {int(round(home_runs_per_game, 0))} home runs per game,") #rounded 0.3522727272727273 to 0 decimal places (=0) and converted into an integer value to make sentence
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {int(round(projected_home_runs, 0))} home runs this season.") #rounded 57.09090909090909 to 0 decimal places (=57) and converted into an integer value to make sentence


#the reason why without knowing any of the values stored in the variables, we know the line games_remaining = total_season_games - games_played because we are simply subtracting the number of games played from the total number of games in a season so it will always print the right result.