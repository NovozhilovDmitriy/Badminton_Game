from unittest import TestCase
import input
import sys
sys.stdout.reconfigure(encoding="utf-8")

class ImportExcelCheckCorrectScoreTest(TestCase):

    def test_first_win_common(self):
        self.assertTrue(input.Import_Excel.check_correct_score(21, 0))

    def test_first_win_common2(self):
        self.assertTrue(input.Import_Excel.check_correct_score(21, 1))

    def test_first_win_common3(self):
        self.assertTrue(input.Import_Excel.check_correct_score(21, 19))

    def test_second_win_common(self):
        self.assertTrue(input.Import_Excel.check_correct_score(0, 21))

    def test_second_win_common2(self):
        self.assertTrue(input.Import_Excel.check_correct_score(1, 21))

    def test_second_win_common3(self):
        self.assertTrue(input.Import_Excel.check_correct_score(19, 21))

    def test_first_win_balance1(self):
        self.assertTrue(input.Import_Excel.check_correct_score(22, 20))

    def test_first_win_balance2(self):
        self.assertTrue(input.Import_Excel.check_correct_score(30, 28))

    def test_second_win_balance1(self):
        self.assertTrue(input.Import_Excel.check_correct_score(20, 22))

    def test_second_win_balance2(self):
        self.assertTrue(input.Import_Excel.check_correct_score(28, 30))

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


class ImportExcelCheckNoneTest(TestCase):

    def test_positive(self):
        self.assertEqual(input.Import_Excel.check_none(1), 1)

    def test_negative(self):
        self.assertEqual(input.Import_Excel.check_none(""), "")