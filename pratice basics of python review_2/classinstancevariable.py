
class player:

    team_name = "killerKnights"

    def __init__(self, name ):
        self.name = name 


p1 = player("Yushi")
p2 = player("yushiiii")
p3 = player("Piyush")


print(f"player 1 is {p1.name}")
print(f"player 2 is {p2.name}")
print(f"player 3 is {p3.name}")

##       the team name is --------
print(p1.team_name)
print(p2.team_name)
print(p3.team_name)

p1.name = "Ayush"
print(p1.name)
print(p2.name)

player.team_name = "Ghostrider"
print(p3.team_name)
p1.team_name = "knight"
print(p1.team_name)
print(p2.team_name)
print(p1.team_name)