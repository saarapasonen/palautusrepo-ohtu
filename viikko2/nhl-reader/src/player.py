class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.team = player_dict["team"]
        self.position = player_dict.get("position", "0")
        self.nationality = player_dict["nationality"]
        self.goals = int(player_dict.get("goals", 0))
        self.assists = int(player_dict.get("assists", 0))
        self.points = int(player_dict.get("points", 0))
        self.penalty_minutes = int(player_dict.get("penalty_minutes", 0))

        self.summa = self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.summa}"
    
