from unittest import TestCase
import New_Class


class Game_real_score_Test(TestCase):

    def test_common_win(self):
        self.assertEqual(New_Class.Game.real_score_Sa(21, 11), 1)  # common win

    def test_common_win1(self):
        self.assertEqual(New_Class.Game.real_score_Sa(21, 19), 1)  # common win

    def test_common_lose(self):
        self.assertEqual(New_Class.Game.real_score_Sa(11, 21), 0)  # common lose

    def test_common_lose1(self):
        self.assertEqual(New_Class.Game.real_score_Sa(19, 21), 0)  # common lose

    def test_balance_win(self):
        self.assertEqual(New_Class.Game.real_score_Sa(22, 20), 0.8)  # balance win

    def test_balance_win1(self):
        self.assertEqual(New_Class.Game.real_score_Sa(28, 26), 0.8)  # balance win

    def test_balance_lose(self):
        self.assertEqual(New_Class.Game.real_score_Sa(20, 22), 0.2)  # balance lose

    def test_balance_lose1(self):
        self.assertEqual(New_Class.Game.real_score_Sa(21, 23), 0.2)  # balance lose

    def test_more10_win(self):
        self.assertEqual(New_Class.Game.real_score_Sa(21, 10), 1.2)  # more 10 win

    def test_more10_win1(self):
        self.assertEqual(New_Class.Game.real_score_Sa(21, 3), 1.2)  # more 10 win

    def test_more10_lose(self):
        self.assertEqual(New_Class.Game.real_score_Sa(10, 21), -0.2)  # more 10 lose

    def test_more10_lose1(self):
        self.assertEqual(New_Class.Game.real_score_Sa(2, 21), -0.2)  # more 10 lose

    def test_error1(self):
        self.assertEqual(New_Class.Game.real_score_Sa(10, 8), None)  # more 10 lose

    # def test_exception(self):
    #     with self.assertRaises(ValueError) as e:
    #         New_Class.Game.real_score(1, 2)
    #     self.assertEqual('error', e.exception.args[0])

class Game_win_lose_max_min_Test(TestCase):

    def test_common_win(self):
        self.assertEqual(New_Class.Game.win_lose_max_min(21, 11), [1, 0, 0])  # common win

    def test_common_lose(self):
        self.assertEqual(New_Class.Game.win_lose_max_min(11, 21), [0, 0, 0])  # common lose

    def test_balance_win(self):
        self.assertEqual(New_Class.Game.win_lose_max_min(22, 20), [1, 1, 0])  # balance win

    def test_balance_lose(self):
        self.assertEqual(New_Class.Game.win_lose_max_min(26, 28), [0, 1, 0])  # balance lose

    def test_more10_win(self):
        self.assertEqual(New_Class.Game.win_lose_max_min(21, 2), [1, 0, 1])  # more 10 win

    def test_more10_lose(self):
        self.assertEqual(New_Class.Game.win_lose_max_min(10, 21), [0, 0, 1])  # more 10 win


class Game_get_pair_avr_score_Test(TestCase):

    def test_score_newUser(self):
        self.temp = New_Class.Game(New_Class.Player('Win'), New_Class.Player('Lose'), New_Class.Player('Won', 100), New_Class.Player('Lase', 200), 21, 12)
        self.assertEqual(self.temp.get_pair_avr_score(self.temp.players[0], self.temp.players[1]), 500)

    def test_score_NotNewUser(self):
        self.temp = New_Class.Game(New_Class.Player('Win'), New_Class.Player('Lose'), New_Class.Player('Won', 100), New_Class.Player('Lase', 200), 21, 12)
        self.assertEqual(self.temp.get_pair_avr_score(self.temp.players[2], self.temp.players[3]), 150)

class Game_wait_score_1_Test(TestCase):

    def test_wait_score_1_newUsers(self):
        self.temp = New_Class.Game(New_Class.Player('Win'), New_Class.Player('Lose'), New_Class.Player('Won'), New_Class.Player('Lase'), 21, 12)
        self.assertEqual(self.temp.wait_score_1_Ea(), 0.5)

    def test_wait_score_1_NotNewUsers(self):
        self.temp = New_Class.Game(New_Class.Player('Win'), New_Class.Player('Lose'), New_Class.Player('Won', 450), New_Class.Player('Lase', 450), 21, 12)
        self.assertEqual(self.temp.wait_score_1_Ea(), 0.7597469266479578)

class Game_wait_score_2_Test(TestCase):

    def test_wait_score_2_newUsers(self):
        self.temp = New_Class.Game(New_Class.Player('Win', 300), New_Class.Player('Lose', 300), New_Class.Player('Won', 300), New_Class.Player('Lase', 300), 21, 12)
        self.assertEqual(self.temp.wait_score_2_Ea(), 0.5)

    def test_wait_score_2_NotNewUsers(self):
        self.temp = New_Class.Game(New_Class.Player('Win'), New_Class.Player('Lose'), New_Class.Player('Won', 450), New_Class.Player('Lase', 450), 21, 12)
        self.assertEqual(self.temp.wait_score_2_Ea(), 0.2402530733520421)


class Game_real_score_1_Test(TestCase):

    def test_real_score_1_newUsers(self):
        self.temp = New_Class.Game(New_Class.Player('Win', 300), New_Class.Player('Lose', 300), New_Class.Player('Won', 300), New_Class.Player('Lase', 300), 21, 12)
        self.assertEqual(self.temp.real_score_1_Ra(), 10)

    def test_real_score_1_NotNewUsers(self):
        self.temp = New_Class.Game(New_Class.Player('Win'), New_Class.Player('Lose'), New_Class.Player('Won', 300), New_Class.Player('Lase', 300), 21, 12)
        self.assertEqual(self.temp.real_score_1_Ra(), 0.1980198019801982)

class Game_real_score_2_Test(TestCase):

    def test_real_score_2_newUsers(self):
        self.temp = New_Class.Game(New_Class.Player('Win'), New_Class.Player('Lose'), New_Class.Player('Won'), New_Class.Player('Lase'), 21, 12)
        self.assertEqual(self.temp.real_score_2_Ra(), -10)

    def test_real_score_2_NotNewUsers(self):
        self.temp = New_Class.Game(New_Class.Player('Win'), New_Class.Player('Lose'), New_Class.Player('Won', 400), New_Class.Player('Lase', 400), 21, 12)
        self.assertEqual(self.temp.real_score_2_Ra(), -1.8181818181818183)

class Game_print_list_new_player_Test(TestCase):

    def test_print_list_new_player_NotNewUsers(self):
        self.temp = []
        self.assertEqual(New_Class.Game.print_list_new_player('2023-01-01', self.temp), None)

    # def test_print_list_new_player_NewUsers(self):
    #     self.temp = ['Cinema']
    #     self.assertEqual(New_Class.Game.print_list_new_player('2023-01-01', self.temp), 2, msg='{0}'.format(self.temp))
    #     #New_Class.Game.print_list_new_player('2023-01-01', self.temp)
    #     # def test_exception(self):
    #     #     with self.assertRaises(ValueError) as e:
    #     #         New_Class.Game.real_score(1, 2)
    #     #     self.assertEqual('error', e.exception.args[0])
# if __name__ == '__main__':
#     main()
