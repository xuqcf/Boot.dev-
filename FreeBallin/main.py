def split_players_into_teams(players):
    team_even = players[::2]
    team_odd = players[1::2]
    return team_even, team_odd