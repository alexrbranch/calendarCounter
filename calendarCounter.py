#!/usr/bin/env python
# -*- coding: utf-8 -*-

DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def request_input():
    dates = [[], []]
    print("Find the number of days and weeks between 2 dates")
    while(1):
        date = input("Input first date (MM/DD): ")
        dates[0] = date.split('/')
        if is_valid_date(dates[0]):
            break
        print("'" + date + "': " + "Invalid entry. Try again")
    while(1):
        date = input("Input second date (MM/DD): ")
        dates[1] = date.split('/')
        if is_valid_date(dates[1]):
            break
        print("'" + date + "': " + "Invalid entry. Try again")
    return dates

def is_valid_date(date):
    date_int = [int(date[0]), int(date[1])]
    if (date_int[0] < 1) or (date_int[0] > 12) or (DAYS_IN_MONTH[date_int[0] - 1] - date_int[1] < 1) or (len(date) > 2):
        # check if month is 1 <= m <= 12 and days is not more than # days in that month and for correct format
        return False
    return True


def calculate():
    dates = request_input()


def main():
    calculate()


if __name__ == "__main__":
    main()
