"""
Enter your Birthday and the return value is your age
"""
import datetime


def get_age(birthday, today):
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


if __name__ == '__main__':
    birthday = input('please input your birthday DD.MM.YYYY\n')

    if len(birthday.split('.')) > 2:
        birthday_date = datetime.date(year=int(birthday.split('.')[-1]),
                                      month=int(birthday.split('.')[1]),
                                      day=int(birthday.split('.')[0]))
        today = datetime.date.today()
        print(f'you are {get_age(birthday_date,today)} years old')
    else:
        print('wrong format')