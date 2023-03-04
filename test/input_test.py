from unittest import TestCase
import input


class ImportExcelCheckCorrectScoreTest(TestCase):

    def test_first_win_common(self):
        self.assertEqual(input.Import_Excel.check_correct_score(21, 0), True)

    def test_first_win_common2(self):
        self.assertEqual(input.Import_Excel.check_correct_score(21, 1), True)

    def test_first_win_common3(self):
        self.assertEqual(input.Import_Excel.check_correct_score(21, 19), True)

    def test_second_win_common(self):
        self.assertEqual(input.Import_Excel.check_correct_score(0, 21), True)

    def test_second_win_common2(self):
        self.assertEqual(input.Import_Excel.check_correct_score(1, 21), True)

    def test_second_win_common3(self):
        self.assertEqual(input.Import_Excel.check_correct_score(19, 21), True)

    def test_first_win_balance1(self):
        self.assertEqual(input.Import_Excel.check_correct_score(22, 20), True)

    def test_first_win_balance2(self):
        self.assertEqual(input.Import_Excel.check_correct_score(30, 28), True)

    def test_second_win_balance1(self):
        self.assertEqual(input.Import_Excel.check_correct_score(20, 22), True)

    def test_second_win_balance2(self):
        self.assertEqual(input.Import_Excel.check_correct_score(28, 30), True)

    def test_negative1(self):
        self.assertEqual(input.Import_Excel.check_correct_score(21, 21), False)

    def test_negative2(self):
        self.assertEqual(input.Import_Excel.check_correct_score(0, 0), False)

    def test_negative3(self):
        self.assertEqual(input.Import_Excel.check_correct_score('null', 21), False)

    def test_negative4(self):
        self.assertEqual(input.Import_Excel.check_correct_score('null', 'null'), False)

    def test_negative5(self):
        self.assertEqual(input.Import_Excel.check_correct_score(30, 1), False)

    def test_negative6(self):
        self.assertEqual(input.Import_Excel.check_correct_score(21, 20), False)

    def test_negative7(self):
        self.assertEqual(input.Import_Excel.check_correct_score(23, 22), False)

    def test_negative8(self):
        self.assertEqual(input.Import_Excel.check_correct_score(1, 22), False)