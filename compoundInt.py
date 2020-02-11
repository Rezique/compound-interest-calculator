# Desription: Compound Interest
# Author: Ziqing Zhang
# When a bank account pays compound interest, 
# it pays interest not only on the principal amount that was deposited into the account, 
# but also on the interest that has accumulated over time. 
# Suppose you want to deposit some money into a savings account,
# and let the account earn compound interest for a certain number of years. 
# The formula for calculating the balance of the account 
# after a specified number of years is:

# A = P ( 1 + r n ) n t 
# The terms in the formula are:
# A is the amount of money in the account after the specified number of years.
# P is the principal amount that was originally deposited into the account.
# r is the annual interest rate.
# n is the number of times per year that the interest is compounded.
# t is the specified number of years.

# Write a program that makes the calculation for you. 
# The program should ask the user to input the following:
# The amount of principal originally deposited into the account
# The annual interest rate paid by the account
# The number of times per year that the interest is compounded 
# (For example, if interest is compounded monthly, enter 12. 
#  If interest is compounded quarterly, enter 4.)
# The number of years the account will be left to earn interest
# Once the input data has been entered, the program should calculate 
# and display the amount of money that will be 
# in the account after the specified number of years.
# The user should enter the interest rate as a percentage. 
# For example, 2 percent would be entered as 2, not as .02. 
# The program will then have to divide the input by 100 
# to move the decimal point to the correct position.

#input
def get_user_principal():
  principal = None
  while principal is None:
    try:
      principal = float(input("Please enter the principle amount: "))
      if principal < 0:
        print("ERROR: Number must be greater than 0.")
        principal = None
    except:
      print("ERROR: Input must be a number.")
  return principal

def get_user_rate():
  rate = None
  while rate is None:
    try:
      rate = float(input("Annual Interest Rate of the account: "))
      rate /= 100
      if rate < 0:
        print("ERROR: Number must be greater than 0.")
        rate = None
    except:
      print("ERROR: Must be a number")
  return rate

def get_user_times():
  times_per_year = None
  while times_per_year is None:
    try:
      times_per_year = float(input("Number of times interest is compounded in a year: "))
      if times_per_year < 0:
        print("ERROR: Number should be greater than 0.")
        times_per_year = None
    except:
      print("ERROR: Must be a number")
  return times_per_year

def get_user_years():
  years = None
  while years is None:
    try:
      years = int(input('Duration (years): '))
      if years < 0:
        print("ERROR: Number should be greater than 0")
        years = None
    except:
      print("ERROR: Must be a number")
  return years

def calc_total(principal, rate, times_per_year, years):
  return principal * (( 1 + (rate / times_per_year)) ** (times_per_year * years))

def main():
  
  principal = get_user_principal()
  rate = get_user_rate()
  times_per_year = get_user_times()
  years = get_user_years()
  #process
  total = calc_total(principal, rate, times_per_year, years)
  #output
  print("total: ", '$', format(total, '.2f'), sep = '')
  return True


main()
