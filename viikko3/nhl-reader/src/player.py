class Player:
    def __init__(self, name, nat, assists, goals, team):
        self.name = name
        self.nat = nat
        self.assists = assists
        self.goals = goals
        self.team = team

        self.total = self.assists + self.goals
    
    def __gt__(self, other):
        return self.total < other.total

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.total}"
