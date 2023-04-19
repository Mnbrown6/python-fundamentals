""" Exception Handling Lab """

def is_leap_year():
    # ask user for a 4 digit year
    # convert user value to int() <-- this is why we need a try
    # value entered properly can be determined based on the code

    try:
        year = int(input('Please provide a 4 digit year'))

    except ValueError:
        print('You have entered letters instead of numbers.')
    else:
        if year >= 1000:
            if (year % 400 == 0) and (year % 100 == 0):
                print(f'{year} is a leap year.')
            elif year % 4 == 0 and year % 100 != 0:
                print(f'{year} is a leap year.')
            else:
                print(f'{year} is not leap year.')
        else:
            print('Please enter a 4 digit number.')


if __name__ == '__main__':
    is_leap_year()