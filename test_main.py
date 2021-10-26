import unittest
import datetime

from main import Calendar


class TestPyramid(unittest.TestCase):

    def setUp(self):
        self.cal = Calendar()

    def test_add_friend_birthday(self):
        dict_1 = {'alex': datetime.date(2021, 10, 16), 'max': datetime.date(2021, 10, 16)}
        dict_2 = {'alex': datetime.date(2021, 10, 16), 'max': datetime.date(2021, 10, 16),
                  'slava': datetime.date(2021, 10, 21)}
        self.cal.add_friend_birthday("alex", datetime.date(2021, 10, 10))
        self.cal.add_friend_birthday("max", datetime.date(2021, 10, 16))
        self.cal.add_friend_birthday("alex", datetime.date(2021, 10, 16))
        self.cal.add_friend_birthday("slava", datetime.date(2021, 10, 21))
        self.assertEqual(self.cal.get_birthdays_of_date(datetime.date(2021, 10, 16)), dict_1)
        self.assertEqual(self.cal.get_all_birthdays(), dict_2)

    def test_delete_birthday(self):
        dict_1 = {'alex': datetime.date(2021, 10, 16), 'max': datetime.date(2021, 10, 16)}
        self.cal.add_friend_birthday("alex", datetime.date(2021, 10, 10))
        self.cal.add_friend_birthday("max", datetime.date(2021, 10, 16))
        self.cal.add_friend_birthday("alex", datetime.date(2021, 10, 16))
        self.cal.add_friend_birthday("slava", datetime.date(2021, 10, 21))
        self.cal.delete_birthday("slava")
        self.assertEqual(self.cal.get_all_birthdays(), dict_1)

    def test_get_birthdays_of_date(self):
        dict_1 = {'alex': datetime.date(2021, 10, 16), 'max': datetime.date(2021, 10, 16)}

        self.cal.add_friend_birthday("alex", datetime.date(2021, 10, 10))
        self.cal.add_friend_birthday("max", datetime.date(2021, 10, 16))
        self.cal.add_friend_birthday("alex", datetime.date(2021, 10, 16))
        self.cal.add_friend_birthday("slava", datetime.date(2021, 10, 21))
        self.assertEqual(self.cal.get_birthdays_of_date(datetime.date(2021, 10, 16)), dict_1)

    def test_get_all_birthdays(self):
        dict_1 = {'alex': datetime.date(2021, 10, 16), 'max': datetime.date(2021, 10, 16),
                  'slava': datetime.date(2021, 10, 21)}
        self.cal.add_friend_birthday("alex", datetime.date(2021, 10, 10))
        self.cal.add_friend_birthday("max", datetime.date(2021, 10, 16))
        self.cal.add_friend_birthday("alex", datetime.date(2021, 10, 16))
        self.cal.add_friend_birthday("slava", datetime.date(2021, 10, 21))
        self.assertEqual(self.cal.get_all_birthdays(), dict_1)


if __name__ == "__main__":
    unittest.main()
