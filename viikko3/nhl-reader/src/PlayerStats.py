from datetime import datetime
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
        self._players = []

    def top_scorers_by_nationality(self, given_nat):
        response = self._reader.get_players()

        for player_dict in response:
            name = player_dict['name']
            nat = player_dict['nationality']
            assists = player_dict['assists']
            goals = player_dict['goals']
            team = player_dict['team']

            if (nat != given_nat):
                continue

            player = Player(
                name,
                nat,
                assists,
                goals,
                team
            )

            self._players.append(player)

        self._players.sort()

        return self._players