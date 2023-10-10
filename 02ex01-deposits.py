#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""


# TODO: add lines to calculate yields for some common periods
#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield
#       as well
# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run
USAGE = """USAGE: {script} initial_sum percent fixed_period set_period 
 
\tCalculate deposit yield. See script source for more details. 
""" 
USAGE = USAGE.strip() 
 
def deposit(initial_sum, percent, fixed_period, set_period): 
    """Calculate deposit yield.""" 
    per = percent / 100 
    growth = (1 + per) ** (set_period / fixed_period) 
    return initial_sum * growth 
 
def main(): 
    """Gets called when run as a script.""" 
    initial_sum = float(input("initial_sum: ")) 
    percent = float(input("percent: ")) 
    fixed_period = float(input("fixed_period: ")) 
    set_period = float(input("set_period: ")) 
 
    res = deposit(initial_sum, percent, fixed_period, set_period) 
    print(f"Total after {set_period} years: {res:.2f}")  # Print the total for the specified set period

    # Calculate yields for some common periods
    yield_1_month = deposit(initial_sum, percent, 1 / 12, 1)
    yield_1_year = deposit(initial_sum, percent, 1, 1)
    yield_5_years = deposit(initial_sum, percent, 1, 5)
    yield_10_years = deposit(initial_sum, percent, 1, 10)

    # Print the yields for common periods
    print(f"Yield for 1 month: {yield_1_month:.2f}")
    print(f"Yield for 1 year: {yield_1_year:.2f}")
    print(f"Yield for 5 years: {yield_5_years:.2f}")
    print(f"Yield for 10 years: {yield_10_years:.2f}")
 
if __name__ == '__main__': 
    main()