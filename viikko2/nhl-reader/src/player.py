class Player:
    def __init__(self, player_dict):
        self.name = player_dict.get("name", "")
        self.team = player_dict.get("team", "")
        self.goals = int(player_dict.get("goals", 0))
        self.assists = int(player_dict.get("assists", 0))
        self.nationality = player_dict.get("nationality", "")

    def __str__(self):
        total_points = self.goals + self.assists
        return f"{self.name:20} {self.team:3} {self.goals:2} + {self.assists:2} = {total_points:3}"

