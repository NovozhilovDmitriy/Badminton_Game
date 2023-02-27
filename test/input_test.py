from unittest import TestCase
import input


class Import_Excel_check_correct_score_Test(TestCase):

    def first_win_common(self):
        self.assertEqual(input.Import_Excel.check_correct_score(21, 0), True)

    def first_win_common2(self):
        self.assertEqual(input.Import_Excel.check_correct_score(21, 1), True)

    def first_win_common3(self):
        self.assertEqual(input.Import_Excel.check_correct_score(21, 19), True)
