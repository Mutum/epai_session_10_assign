#!/usr/bin/env python
# coding: utf-8

# #### Part 1 ####

# * Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings). - 250**

# In[28]:


from collections import namedtuple, Counter
from operator import attrgetter

from datetime import date, datetime, timezone
from faker import Faker
fake = Faker()


# In[29]:


def calculate_age(dob: datetime):
    '''
    Return age from date of birth
    '''
    return int((date.today() - dob).days / 365.2425)


# In[30]:


def timed_reps(reps):
    '''
    Decorator function to run a function reps times and return average run times.
    '''
    if not isinstance(reps, int):
        raise ValueError(f"{reps} must be of int type")
    def timed(fn):
        from time import perf_counter
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / reps
            print('Avg Run time of {0} is: {1:.8f}s ({2} reps)'.format(fn.__name__, avg_run_time, reps))
            return result
        return inner
    return timed


# In[31]:


random_profile = namedtuple('random_profile', 'name, age, sex, blood_group, location')
profiles_list = []

@timed_reps(30)
def create_random_profiles(n: int):
    '''
    Generate n fake profiles with each profile is stored as a namedtuple in a list.
    Then return  most frequent blood group, average location, oldest person and average age 
    Decorated with timed_reps to run the function 15 times to get the average run time.
    '''
    if not isinstance(n, int):
        raise ValueError(f"{n} must be of int type")

    for i in range(n):
        rp = fake.profile()
        profile = random_profile(rp['name'], calculate_age(rp['birthdate']), rp['sex'], rp['blood_group'], rp['current_location'])
        profiles_list.append(profile)

    largest_bood_group = Counter(i.blood_group for i in profiles_list).most_common(1)[0]
    mean_current_location = float(sum([i.location[0] for i in profiles_list])/len(profiles_list)), float(sum([i.location[1] for i in profiles_list])/len(profiles_list))
    oldest_person_age = sorted(profiles_list, key=lambda x: x.age, reverse=True)[0]
    average_age = sum([i.age for i in profiles_list])/len(profiles_list)

    return f'\nSummary of {n} random profiles:         \nMost frequent blood group in the profile list: {largest_bood_group}         \nMean of current location of all the profiles: {mean_current_location}         \nOldest person in the list: {oldest_person_age.name, oldest_person_age.age}         \nAvegerage age of people from the list: {average_age}'


# In[32]:


print(create_random_profiles(1000))


# #### Part 2 ####

# *Do part 1 as above using a dictionary. Prove that namedtuple is faster. - 250**

# In[33]:


d_profiles_list = []

@timed_reps(30)
def d_create_random_profiles(n: int):
    '''
    Creates n as input and creates n number of fake profiles.
    Each profile is stored as a dictionary in a list.
    It calculates most frequent blood group, average location, oldest person and average age and returns them.
    Decorated with timed_reps to run 15 times to get average run time.
    '''
    if not isinstance(n, int):
        raise ValueError(f"{n} must be of int type")

    for i in range(n):
        rp = fake.profile()
        profile = {'name':rp['name'], 'age':calculate_age(rp['birthdate']), 'sex':rp['sex'], 'blood_group':rp['blood_group'], 'location':rp['current_location']}
        d_profiles_list.append(profile)

    largest_bood_group = Counter(i['blood_group'] for i in d_profiles_list).most_common(1)[0]
    mean_current_location = float(sum([i['location'][0] for i in d_profiles_list])/len(d_profiles_list)), float(sum([i['location'][1] for i in d_profiles_list])/len(d_profiles_list))
    oldest_person_age = sorted(d_profiles_list, key=lambda x: x['age'], reverse=True)[0]
    oldest_person_age = (oldest_person_age['name'], oldest_person_age['age'])
    average_age = sum([i['age'] for i in d_profiles_list])/len(d_profiles_list)

    return f'\nSummary of {n} random profiles:         \nMost frequent blood group in the profile list: {largest_bood_group}         \nMean of current location of all the profiles: {mean_current_location}         \nOldest person in the list: {oldest_person_age}         \nAvegerage age of people from the list: {average_age}'


# In[34]:


print(d_create_random_profiles(1000))


# **Observation:**  
# Avg Run time of create_random_profiles is: 1.59312059s (30 reps)  
# Avg Run time of d_create_random_profiles is: 1.59780397s (30 reps)  
# It seems the function with namedtuple slightly faster than the one with dictionaries. But we can repeat more iteratioin to validate again

# #### Part 3 ####

# * Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500**

# In[35]:


import pandas as pd
import random
pd.set_option('display.max_rows', 150)


# In[36]:


company_symbol = lambda x: x[:4].upper() if len(x.split()) == 1 else str(x.split()[0][:3] + x.split()[1][0]).upper()
company_stock = namedtuple('company_stock', ['name', 'symbol', 'open', 'low', 'high', 'close'])
company_stock_profiles = []


# In[37]:


def stock_exchange(n: int):
    '''
    Takes n as input and creates n number of random company names using Faker.
    Calls company_symbol function to create 5 character symbol for the company.
    Creates random values to assign open, high, low and close stock values however adhering to comparison rules.
    Puts the company stock details in pandas dataframe to print in tabular form.
    '''
    if not isinstance(n, int):
        raise ValueError("Input must be an interger")

    weights = [round(random.uniform(0.4, 0.9),3) for _ in range(n)]
    norm_weights = [w / sum(weights) for w in weights]
    for i in range(n):
        company_name = fake.company()
        company_sym = company_symbol(company_name)
        company_open = round((random.randint(200, 5000) * norm_weights[i]), 3)
        company_high = round(random.uniform(company_open, company_open*1.3), 3)
        company_low = round(random.uniform(company_open*0.7, company_high),3)
        company_close = round(random.uniform(company_low, company_high),3)
        company = company_stock(company_name, company_sym, company_open, company_low, company_high, company_close)
        company_stock_profiles.append(company)

    company_stock_profiles_pd = pd.DataFrame(company_stock_profiles)
    return company_stock_profiles_pd


# In[38]:


df = stock_exchange(100)
df

