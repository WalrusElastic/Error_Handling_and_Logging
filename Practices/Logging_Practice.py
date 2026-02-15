# This file demonstrates logging fundamentals for Python.
# Complete each exercise by implementing the functions according to the requirements.
# Refer to Error_Handling_and_Logging.md for concepts and best practices.

import logging
import json
import sys
from typing import Any, List, Dict

# Exercise 1: Basic logging setup
# Problem: The function below uses print statements instead of logging. Refactor the function to use the logging module instead, and configure the logger to display messages at the INFO level

users_dict = {
    1111: {"name": "Alice", "age": 30},
    6767: {"name": "Bob", "age": 25},
    9999: {"name": "Charlie", "age": 35}
}

def extract_user_info(user_id: int) -> Dict[str, Any]:
    """
    Extract user information from the users_dict.
    """
    print(f"Extracting user info for ID {user_id}")
    user_info = users_dict[user_id]
    print(f"Extracted user info for ID {user_id}: {user_info}")
    return user_info
    pass
for user_id in users_dict.keys():
    extract_user_info(user_id)


# Exercise 2: Logging levels
# Problem: The function below performs some operations and logs messages, but all at the same level. Refactor the function to use appropriate logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) based on the context of each message.

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def reciprocal(value):
    logger.info(f"Processing value: {value}")

    if not isinstance(value, (int, float)):
        logger.info(f"Error: Value '{value}' is not a number.")
        return None

    if value < 0:
        logger.info(f"Negative value received: {value}, continuing.")

    if value == 0:
        logger.info("Error: Division by zero attempted.")
        return None

    result = 1 / value
    logger.info(f"Successfully computed reciprocal of {value}: {result}")

    return result


numbers = [10, -5, 0, "hello", 25]

for num in numbers:
    output = reciprocal(num)
    print(f"Reciprocal of {num}: {output}\n")


# Exercise 3: Logging exceptions with traceback
# Problem: The function below all exceptions broadly but does not log the traceback, making it difficult to debug. Refactor the function to capture each exception and logging a message and a traceback of the corresponding exception when it occurs.


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def safe_divide(a, b):
    try:
        numerator = float(a)
        denominator = float(b)
        result = numerator / denominator
        logger.info(f"Successfully computed division: {numerator} / {denominator} = {result}")
        return result

    except Exception:
        logger.error(f"Error occurred while dividing {a} by {b}.")
        return None

values = [(10, "2"), (5, 0), ("x", 3), (8, 4)]

for a, b in values:
    safe_divide(a, b)
