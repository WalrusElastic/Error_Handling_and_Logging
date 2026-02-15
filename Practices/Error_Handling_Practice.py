# This file demonstrates error handling and logging fundamentals for Python.
# Complete each exercise by implementing the functions according to the requirements.
# Refer to Error_Handling_and_Logging.md for concepts and best practices.

from typing import Any, List, Union

# Exercise 1: Basic try/except
# Problem: The following code crashes if division by zero occurs. 
# Implement proper error handling, such that it returns None instead of crashing when division by zero is attempted, and whether it passes or fails, prints a message indicating it is complete. 

def safe_divide(a: float, b: float) -> Union[float, None]:
    return a/b

test_cases = [(10, 2, 5), (10, 0, None )]
for i in range(len(test_cases)):
    a, b, expected = test_cases[i]
    result = safe_divide(a, b)
    print(f"safe_divide({a}, {b}) = {result}, expected = {expected}")

# Exercise 2: Catching specific exceptions
# Problem: The function below takes in a list containing 2 strings of integers, and returns their sums. However, it fails when the list contains less than 2 elements, or when the strings contain floats/ non-numerical characters. 
# Implement error handling to catch these specific exceptions and return None in those cases.

def add_two_numbers_from_list(input: list) -> Union[int, None]:
    num_1 = int(input[0])
    num_2 = int(input[1])
    result = num_1 + num_2
    return result

test_cases = [["1", "2", 3], ["1.5", "2.5", None],["1", "two", None], ["1", 2, 3]]
for i in range(len(test_cases)):
    input, expected = test_cases[i][0:2], test_cases[i][2]
    result = add_two_numbers_from_list(input)
    print(f"add_two_numbers_from_list({input}) = {result}, expected = {expected}")

# Exercise 3: Raising exceptions
# Problem: The function below accesses the user data from dictionary, with the keys representing the user ids, and the data representing the user data. However, there are cases where the user is not registered yet, meaning it is not in the dictionary, or that the user data is not stored yet, meaning the value is None.
# Raise a KeyError when the user id is not found, and a ValueError when the user data is None, ensurring that the error messages are descriptive.

users_dict = {
    1111: {"name": "Alice", "age": 30},
    6767: None,  # User data not stored yet
}


def get_user_name(users_dict: dict, user_id: int) -> Any:
    username = users_dict[user_id]["name"]
    return username

test_cases = [(1111, "Alice"), (6767, None), (9999, None)]
for user_id in test_cases:
    result = get_user_name(users_dict, user_id[0])
    print(f"get_user_name(users_dict, {user_id[0]}) = {result}, expected = {user_id[1]}")


# Exercise 4: Exception propagation
# Problem: The following code takes in a string containing the raw score data, and an integer n representing the numer of scores to consider, and computes the average of the highest n scores. However, there are multiple points of failure in this code, such as when the user provides an invalid input for N, or when N is larger than the number of scores available. 
# Implement error handling to catch these exceptions, in each sub function as well as in the process_student function, Printing appropriate error messages and returning None when an error occurs.

def parse_scores(input_str: str):
    """
    Reads comma-separated scores and converts them to integers.
    Example input: 80,75,90
    """
    scores = [int(x.strip()) for x in input_str.split(",")]  
    return scores


def compute_average(scores, n):
    scores.sort(reverse = True)
    selected = [scores[i] for i in range[n]]
    avg = sum(scores) / len(scores) 


def process_student(input_str: str, num_to_consider: int):
    scores = parse_scores(input_str)
    avg = compute_average(scores, num_to_consider)
    print("Average score:", avg)

test_cases = [("80,75,90", 2, 85), ("80,75,90", 5, None), ("80,75,90", -1, None), ("80,abc,90", 2, None)]
for input_str, n, expected in test_cases:
    result = process_student(input_str, n)
    print(f"process_student('{input_str}' and n={n}) = {result}, expected = {expected}\n")




