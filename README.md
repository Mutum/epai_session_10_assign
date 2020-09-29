# EPAI Session 10

# test_create_random_profiles_type
raise ValuError if rep n is pass as text format


# test_stock_exchange_type_check
raise ValuError if rep n is pass as text format

# test_stock_exchange
This test function calls stock_exchange function that returns a pandas dataframe. This test case validates all the high values are actually greater than open, close and low values for all the instances. If any of them fail, in that case the test fails.

# calculate_age
function to calculate age from a given date of birth

# timed_reps
Decorator function to run a function reps times and return average run times..

# create_random_profiles
  Generate n fake profiles with each profile is stored as a namedtuple in a list.
   Then return  most frequent blood group, average location, oldest person and average age
   Decorated with timed_reps to run the function 15 times to get the average run time.

# d_create_random_profiles
Creates n as input and creates n number of fake profiles.
    Each profile is stored as a dictionary in a list.
    It calculates most frequent blood group, average location, oldest person and average age and returns them.
    Decorated with timed_reps to run 15 times to get average run time.


# stock_exchange
  Takes n as input and creates n number of random company names using Faker. Calls company_symbol function to create 5 character symbol for the company.
  Creates random values to assign open, high, low and close stock values however adhering to comparison rules. Puts the company stock details in pandas dataframe to print in tabular form.
