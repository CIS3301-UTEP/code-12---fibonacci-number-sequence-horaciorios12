import os,sys
import random
from code_12 import get_fibonacci_number
from code_12 import get_fibonacci_number_sequence

import random

def check_if_file_exists():
    try:
        exists = os.path.exists("code_12.py")
        assert exists == True
    except:
        sys.exit()

def test_get_fibonacci_number():
    check_if_file_exists()
    values = [4,23,26,12,3,20,16]
    fibonacci_number = [3, 28657, 121393, 144, 2, 6765, 987]
    random_number = random.randint(1,6)-1
    assert get_fibonacci_number(values[random_number]) == fibonacci_number[random_number]

def test_get_fibonacci_number_sequence():
    check_if_file_exists()
    values = [6,7,8,9,10]
    fibonacci_number_sequence =[[1, 1, 2, 3, 5, 8],[1, 1, 2, 3, 5, 8, 13],[1, 1, 2, 3, 5, 8, 13, 21],[1, 1, 2, 3, 5, 8, 13, 21, 34],[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]]
    random_number = random.randint(1,5)-1
    assert get_fibonacci_number_sequence(values[random_number]) == fibonacci_number_sequence[random_number]