import datetime


class Calendar:
    """ Класс, реализующий функционал программы для напоминания о днях рождения друзей. """

    birthdays = dict()

    def get_all_birthdays(self):
        """
        Генерирует список всех дней рождений друзей.

        :return: словарь дней рождений друзей
        :rtype: dict
        """
        return self.birthdays

    def get_birthdays_of_date(self, date):
        """
        Генерирует список дней рождений друзей по дате.

        :param date: дата в которую необходимо вывести все дни рождения
        :type date: date

        :return: словарь дней рождений друзей в выбранную дату
        :rtype: dict
        """
        birthdays_of_date = dict()
        for name, date_of_birthday in self.birthdays.items():
            if date == date_of_birthday:
                birthdays_of_date[name] = date_of_birthday
        return birthdays_of_date

    def add_friend_birthday(self, name, birthday_date):
        """
        Генерирует список дней рождений друзей по дате.

        :param name: имя друга
        :type name: str

        :param birthday_date: дата рождения друга
        :type birthday_date: date
        """
        self.birthdays[name] = birthday_date

    def delete_birthday(self, name):
        """
        Удаляет день рождение друга из списка.

        :param name: имя друга
        :type name: str
        """
        self.birthdays.pop(name)


if __name__ == "__main__":
    cal = Calendar()
    cal.add_friend_birthday("alex", datetime.date(2021, 10, 10))
    cal.add_friend_birthday("max", datetime.date(2021, 10, 16))
    cal.add_friend_birthday("alex", datetime.date(2021, 10, 16))
    cal.add_friend_birthday("slava", datetime.date(2021, 10, 21))
    print(cal.get_birthdays_of_date(datetime.date(2021, 10, 16)))
    print(cal.get_all_birthdays())
