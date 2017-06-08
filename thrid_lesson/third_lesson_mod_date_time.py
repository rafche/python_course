# datetime is very important module
# a very good guide for strftime
# http://strftime.org/

import datetime


# print the date of today
print('----- print date -----\n')

print(datetime.date.today())

# print another date
print(datetime.date(day=9, month=11, year=1989))

# print the date in other format
# using strftime
print(datetime.date.today().strftime('%d.%m.%Y'))

# adding the weekday
print(datetime.date.today().strftime('%d.%m.%Y %a'))

# adding the full weekday
print(datetime.date.today().strftime('%d.%m.%Y %A'))

print('\n-----------\n\n')


print('----- print time -----\n')

print(datetime.datetime.now().time())


# get the calendarweek
# calling the function isocalendar with the date today
# return a 3-tuple containing ISO year, week number, and weekday.
print('----- calendarweek -----\n')

print(datetime.date.isocalendar(datetime.date.today()))

#lets unpack the isocalendar to a tuple
isoyear, isoweek, isoday = datetime.date.isocalendar(datetime.date.today())

# isoweek = calendarweek
# isoyear = year
# isoday = 1:monday, 2:tuesday, 3:wednesday,....
print(f'isoyear = {isoyear} isoweek = {isoweek} isoday = {isoday}')

# works also with
print(datetime.date.isocalendar(datetime.date(day=13, month=5, year=1998)))


# calculate datedifferenz


# ex_3_1 write a function that returns your age, input should be your birthday
# ex_3_2 write a function that returns remaining days a date

print('\n-----------\n\n')


