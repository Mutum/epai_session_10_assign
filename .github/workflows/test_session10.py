import pytest
import os
import inspect
import re
import pandas as pd

import session10

# os.chdir("D:\Courses\EPAI\session_10")

README_CONTENT_CHECK_FOR = [
    'test_create_random_profiles_type',
    'test_stock_exchange_type_check',
    'test_stock_exchange',
    'test_stock_exchange',
    'calculate_age',
    'timed_reps',
    'd_create_random_profiles',
    'stock_exchange',
]

CHECK_FOR_THINGS_NOT_ALLOWED = []

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add atleast 200 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 8

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session10)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_create_random_profiles_type():    
    with pytest.raises(ValueError) as e_info:
        _ = session10.create_random_profiles('text')


def test_stock_exchange_type_check():    
    with pytest.raises(ValueError) as e_info:
        _ = session10.stock_exchange('text')

def test_stock_exchange():
    df = session10.stock_exchange(100)
    assert df.high.gt(df.low).nunique() == 1
    assert df.high.gt(df.low).unique()[0] == True
    assert df.high.gt(df.open).nunique() == 1
    assert df.high.gt(df.open).unique()[0] == True
    assert df.high.gt(df.close).nunique() == 1
    assert df.high.gt(df.close).unique()[0] == True
