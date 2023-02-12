#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

def get_date(date_num):
    date_num_str = "first" if date_num == 0 else "second"
    while(1):
        date = input(f"Input {date_num_str} date (MM/DD): ")
        try:
            date_clean = datetime.strptime(date, '%m/%d')
        except:
            print("'" + date + "': " + "Invalid entry. Try again")
            continue
        break
    return date_clean

def request_input():
    dates = []
    print("Find the number of days and weeks between 2 dates")
    dates.append(get_date(0))
    dates.append(get_date(1))
    return dates

def calculate():
    dates = request_input()

    delta_days = dates[1] - dates[0]
    total_days = abs(delta_days.days)
    weeks = abs(total_days / 7)
    print(f'{total_days} days')
    print(f'{weeks} weeks')

def main():
    calculate()


if __name__ == "__main__":
    main()
