# Error Handling and Logging

## Table of Contents
1. [Introduction](#introduction)
2. [Error Handling](#error-handling)
   - [Why handle errors?](#why-handle-errors)
   - [Error Handling in Python](#error-handling-in-python)
   - [Catching Specific Exceptions](#catching-specific-exceptions)
   - [Exception Hierarchy](#the-exception-hierarchy)
   - [Raising Exceptions](#raising-exceptions)
   - [Exception Propagation](#exception-propagation)
   - [Error Handling Best Practices](#error-handling-best-practices)
3. [Introduction to Logging](#introduction-to-logging)
   - [Why use logging?](#why-use-logging)
   - [Logging in Python](#logging-in-python)
   - [Basic Usage](#basic-usage)
   - [Logging Levels](#logging-levels)
   - [Logging Exceptions](#logging-exceptions)
   - [Configuring Logging](#configuring-logging)
   - [Best Practices](#best-practices-for-logging)
4. [Summary](#summary)

---

## Introduction

Welcome to the module on error handling and logging. Once your programs grow beyond simple scripts, you need reliable ways to deal with failures and to record what your code is doing. This guide introduces two related skills: **handling errors** so your program can recover or fail safely and predictably, and **logging** so you can trace behaviour and debug issues.

This guide consists of **2 main sections**:

- **Error Handling**: How to catch, raise, and respond to exceptions in Python
- **Introduction to Logging**: How to record events and messages instead of (or in addition to) using `print`

---

## Error Handling

Error handling lets you control what happens when something goes wrong in a program instead of letting it crash. This helps you build code that is robust and reliable, and responds well to unexpected issues.

---

### Introduction to Error Handling

In this folder, you should find the video **Error_Handling_Introduction**. Watch it for an introduction to error handling.

---

### Why handle errors?

Errors are unavoidable in programs. Although we employ defensive programming to mitigate them, bad inputs, missing resources and unexpected states will occur in real systems. Without proper error handling, even minor issues can cause unpredictable behaviour.

Some key benefits of error handling are:

- **Makes Programs More Robust**: Enables programs to continue working despite errors
- **Improves Debugging**: Shows a clear error message instead of an error traceback
- **Graceful Shutdown**: Enables the system to be left in a valid/clean state even after an error occurs

---

### Error Handling in Python

---

#### Introduction

In this folder, you should find the video **Error_Handling_in_Python**. Watch it for an introduction to handling errors in Python.

---

#### try/except/finally

In Python, `try`, `except` and `finally` are the core mechanisms Python uses to handle errors. They function similarly to `if/else` statements.

The `try` block contains code that may raise an exception (fail during execution). Python executes this block normally until an error occurs. If no error occurs, the program continues as usual. If an error occurs, Python immediately stops the try block and looks for a matching `except`.

The `except` block defines how the program should respond when a specific error occurs. It prevents the program from crashing and allows controlled handling of the failure.

The `finally` block contains code that always runs, regardless of whether an error occurred or not. It is primarily used for cleanup to ensure the system remains in a valid state.

**✗ Bad:**
```python
# No handling—program crashes with a long traceback if file is missing
f = open("data.txt")
```

**✓ Good:**
```python
try:
    f = open("data.txt")
except FileNotFoundError:  # Handles specifically the FileNotFound error
    print("File not found.")
finally:  # Executes regardless of whether an error was found
    print("Execution complete.")
    if 'f' in dir() and not f.closed:
        f.close()
```

---

#### Catching Specific Exceptions

When handling errors, you should always catch specific, expected exceptions rather than using a general or bare `except`. This ensures that your program only handles errors it understands, while unexpected bugs are still exposed and can be fixed properly.

Catching overly broad exceptions can hide real problems, make debugging difficult, and lead to silent failures.

**✓ Good:**
```python
try:
    value = int(user_input)
except ValueError:
    print("Please enter a valid number.")
```

**✗ Bad:**
```python
try:
    value = int(user_input)
except Exception:  # Too broad; catches everything
    print("Something went wrong.")
```

---

##### The Exception Hierarchy

Python exceptions are organised in a class hierarchy. Most runtime errors inherit from the base class `Exception`. The simplified structure is as follows:

```
BaseException
 ├── Exception
 │    ├── ValueError
 │    ├── TypeError
 │    ├── IndexError
 │    ├── KeyError
 │    ├── FileNotFoundError
 │    └── RuntimeError
 ├── SystemExit
 ├── KeyboardInterrupt
 └── GeneratorExit
```

Errors such as `ValueError` and `TypeError` derive from `Exception`. As a result, catching `Exception` will also catch these errors, since they are subclasses within the exception hierarchy.

However, when designing programs, you should catch the most specific applicable exception rather than a broad parent class. Catching overly general exceptions can unintentionally hide unrelated errors, making bugs harder to detect and diagnose.

---

#### Raising Exceptions

In addition to handling errors, programs must sometimes **raise exceptions intentionally**. Raising an exception stops normal execution and signals that something has gone wrong or an invalid condition has been detected. This prevents the program from continuing in a corrupted or unpredictable state.

Raising exceptions is a key part of writing **safe, predictable, and maintainable** code.

The basic syntax for raising errors is as shown:

```python
raise Exception("Something went wrong")
```

The exception class refers to the type of exception raised, while the string is text used to provide a human-readable error description of the error which occurred.

You should always raise the most appropriate built-in exceptions where possible, to make debugging and handling easier.

**✓ Good:**
```python
def load_dataset(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)
```
---

#### Exception Propagation

When an exception is raised in Python, it does not have to be handled immediately. If the current block of code does not catch the exception, it is automatically passed upward through the call stack. This process is known as **exception propagation**.

Propagation allows lower-level functions to signal failures, while higher-level code — which has more context about the overall program — can then decide whether to recover, retry, log, or terminate safely.

##### How Propagation Works

When an error occurs:

1. Python checks the current `try/except` block for a matching handler.
2. If none exists, the exception moves up one level to the caller.
3. This continues until:
   - A matching handler is found, or
   - The program terminates with a traceback

**Example:**

```python
def read_number(text):
    try:
        return int(text)
    except ValueError:
        raise  # Raises this error upwards


def process(text):
    try:
        value = read_number(text)
        return value * 2
    except ValueError:
        raise  # Raises this error upwards


try:
    result = process("abc")
except ValueError:
    print("Invalid number provided.")  # Error is handled at this step
```

Here:

- `ValueError` occurs inside `read_number`
- It propagates through `process`
- It reaches the outer `try/except`, where it is caught and handled

---

### Error Handling Best Practices

To write robust, maintainable code, follow these key principles when handling errors:

1. **Catch Specific Exceptions** - Catch exceptions specifically, to prevent masking unexpected errors
2. **Raise Meaningful Messages** - Provide clear context to aid in debugging
3. **Fail Fast and Loudly** - Catch invalid states early to simplify debugging
4. **Use `finally` for Cleanup** - Ensure graceful shutdown if exceptions occur

---

### Error Handling practice

In the `Practices` folder, you will find the Python file **`Error_Handling_Practice.py`**, contains several exercises on implementing error handling.

**Your task**: Refactor each section to utilise error handling accordingly. 

---

## Logging

Logging is the practice of writing structured messages about what your program is doing. Unlike ad‑hoc `print` statements, logging can be sent to files, filtered by severity, and controlled from one place (e.g. the logging module configuration).

### Why use logging?

- **Levels**: Use DEBUG, INFO, WARNING, ERROR to indicate the type of information produced by the script
- **Persistence**: Write to a file for later inspection or auditing
- **Context**: Include timestamps, module names, and severity automatically

### Logging in Python

#### Introduction

In this folder, you will find the video `Logging_in_Python.mp4`. Watch it for an introduction to logging information in Python.

---

#### Basic Usage

Logging is implemented using Python's standard library `logging` module. Instead of using `print()` statements, you use logging functions to record events at different severity levels.

To use it, the `logging` module must first be imported, and basicConfig() must be called as per below

**✗ Bad (using print):**
```python
print("Starting processing.")   # No levels, no timestamps, hard to redirect
print("Something went wrong!")
```

**✓ Good (using logging):**
```python
import logging # importing logging module

logging.basicConfig(level=logging.INFO) # sets minimum level at which information will be logged

logger.info("Starting processing.") # logs information at different levels
logger.error("Something went wrong!")
```

---

#### Logging Levels

Python's logging module provides **five standard severity levels** that allow you to control verbosity without modifying code:

| Level | Numeric Value | Typical Use |
|-------|---------------|------------|
| DEBUG | 10 | Detailed diagnostic information for developers |
| INFO | 20 | General informational messages about program progress |
| WARNING | 30 | Warning messages for potentially problematic situations (default) |
| ERROR | 40 | Error messages for serious problems that need attention |
| CRITICAL | 50 | Critical errors that may cause program termination |

When you set a logging level, all messages at that level and above are recorded. For example, setting level to `WARNING` will log WARNING, ERROR, and CRITICAL messages, but not DEBUG or INFO.

**Level Usage Examples:**

```python
import logging

logger = logging.getLogger(__name__)

# DEBUG: Detailed info for diagnosing issues
logger.debug("User login attempt with ID: 12345")
logger.debug("Database query took 0.5 seconds")

# INFO: Confirmations that things are working
logger.info("Application started successfully")
logger.info("Processing batch of 100 records")

# WARNING: Something unexpected but not critical
logger.warning("Configuration file not found, using defaults")
logger.warning("Memory usage above 80%")

# ERROR: A serious problem occurred
logger.error("Failed to connect to database")
logger.error("Invalid user credentials provided")

# CRITICAL: Very serious, program may not continue
logger.critical("Disk is full - cannot write data")
logger.critical("Fatal configuration error detected")
```

---

#### Logging Exceptions

When an error occurs in an `except` block, you should use **`logger.exception()`** to automatically capture the full traceback. This provides crucial context for debugging.

`logger.exception()` is equivalent to `logger.error()` but automatically appends the current exception traceback to the log message.

**✗ Bad:**
```python
import logging

logger = logging.getLogger(__name__)

user_input = "p"
try:
    result = int(user_input)
except ValueError:
    logger.error("Conversion failed")  # No traceback info
```

**✓ Good:**
```python
import logging

logger = logging.getLogger(__name__)

user_input = "p"
try:
    result = int(user_input)
except ValueError:
    logger.exception("Failed to convert user input")  # Includes full traceback
```
---

#### Configuring Logging

You can configure logging at the start of your program to control output format, level, and destination:

```python
import logging

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # Format of the log messages
    handlers=[
        logging.FileHandler("app.log"),      # Write to file
        logging.StreamHandler()              # Also write to console
    ]
)

logger = logging.getLogger(__name__) # Creates/ Loads a specific logger instance for this file
```

The **format** string can include various fields:
- `%(asctime)s` - Timestamp
- `%(name)s` - Logger name (usually `__name__`)
- `%(levelname)s` - Log level (DEBUG, INFO, WARNING, etc.)
- `%(message)s` - The log message
- `%(filename)s` - Source filename
- `%(funcName)s` - Function name
- `%(lineno)d` - Line number

---

#### Best Practices for Logging

1. **Use named loggers** - Always use `logger = logging.getLogger(__name__)`
2. **Configure at program start** - Set up logging once in your main entry point
3. **Use appropriate levels** - Don't log everything as ERROR; use DEBUG/INFO for normal operations
4. **Use `logger.exception()` in except blocks** - Captures the full traceback for debugging
5. **Include context** - Log relevant variables and state to help diagnose issues


---

### Logging Handling practice

In the `Practices` folder, you will find the Python file **`Logging_Practice.py`**, contains several exercises on implementing logging.

**Your task**: Refactor each section to utilise logging accordingly. 

---

## Error Handling and Logging Practice

In the `Practices` folder, you will find the Python file **`Final_Exercise.py`**, containing a script as robust as a house of cards, writen by your master trainer 3SG Master_B8. 

**Your task**: Refactor the script. Good Luck.

## Summary

Error handling and logging are complementary tools:

- **Error handling** decides how the program responds to errors (continue, retry, exit gracefully)
- **Logging** records what happened so you can investigate and debug issues later

A complete error handling strategy includes logging:

```python
try:
    risky_operation()
except SpecificException as e:
    logger.exception("Risky operation failed:")  # Logs the traceback
    # Handle the error gracefully
except AnotherException as e:
    logger.error(f"Unexpected error: {e}")
    raise  # Re-raise if you can't handle it
finally:
    cleanup()  # Always cleanup
```


Together, error handling and logging make your programs **robust, maintainable, and easier to debug**. Use them consistently throughout your codebase to build production-quality Python applications.
