from Badminton_class import Player, Pair, Game, Day

Dima = Player('Dima', 500)
Gosha = Player('Gosha', 500)
Toly = Player('Toly', 500)
Denis = Player('Denis', 500)

Players = (Dima, Gosha, Toly, Denis)

Pair1 = Pair('Pair1', Dima, Gosha)
Pair2 = Pair('Pair2', Toly, Denis)
Pair3 = Pair('Pair3', Dima, Denis)
Pair4 = Pair('Pair4', Toly, Gosha)
Pair5 = Pair('Pair5', Dima, Toly)
Pair6 = Pair('Pair6', Gosha, Denis)


Game1 = Game(Pair1, Pair2, 21, 19)
Game2 = Game(Pair3, Pair4, 19, 21)
Game3 = Game(Pair5, Pair6, 30, 28)

Today = (Game1, Game2, Game3)

Day1 = Day('10.01.2023', Today)

def players_score(player):
    for i in range(len(player)):
        print('Score ', player[i].name, ' = ', player[i].score, 'Daily score = ', player[i].daily_score)

def update_all_score(player):
    for i in range(len(player)):
        player[i].update_score()


print('Before', Day1.get_day())
players_score(Players)

Day1.update_day_score()
print('After', Day1.get_day())
update_all_score(Players)
players_score(Players)









