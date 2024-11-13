from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered_players = [player for player in players if player.nationality == nationality]
        sorted_players = sorted(filtered_players, key=lambda p: p.summa, reverse=True)
        return sorted_players
    
    def get_players_by_season_and_nationality(self, season, nationality):
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        players = reader.get_players()

        filtered_players = [player for player in players if player.nationality == nationality]
        sorted_players = sorted(filtered_players, key=lambda p: p.summa, reverse=True)
        return sorted_players