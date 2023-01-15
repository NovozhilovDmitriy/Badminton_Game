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
Game3 = Game(Pair5, Pair6, 18, 21)

Day1 = Day('10.01.2023', Game1, Game2, Game3)

# print('Pair1= ', Pair1.get_pair_players(), ', avr_score =', Pair1.get_pair_avr_score())
# print('Pair2= ', Pair2.get_pair_players(), ', avr_score =', Pair2.get_pair_avr_score())
# print('Game1 Pair1 = ', Game1.score_pair1, ', Game1 Pair2 = ', Game1.score_pair2)
# print('Game1 Pair1/Pair2 = ', Game1.get_pair())
# print('Ea_pair1_Game1= ', Game1.wait_score_1())
# print('Ea_pair2_Game1= ', Game1.wait_score_2())
# print('Real_Score_1 = ', Game1.real_score_1())
# print('Real_Score_2 = ', Game1.real_score_2())
Day1.update_day_score()
for i in range(len(Players)):
    print (Players[i].name, Players[i].score)








