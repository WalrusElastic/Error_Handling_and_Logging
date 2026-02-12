# Error Handling and Logging

## Table of Contents
1. [Introduction](#introduction)
2. [Error Handling](#error-handling)
3. [Introduction to Logging](#introduction-to-logging)
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

#### try/except

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

#### The Exception Hierarchy

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

## Introduction to Logging

Logging is the practice of writing structured messages about what your program is doing. Unlike ad‑hoc `print` statements, logging can be sent to files, filtered by severity, and controlled from one place (e.g. the logging module configuration).

### Why use logging?

- **Levels**: Use DEBUG, INFO, WARNING, ERROR so you can turn detail up or down without changing code
- **Persistence**: Write to a file for later inspection or auditing
- **Context**: Include timestamps, module names, and severity automatically

### Basic usage

Use the standard library `logging` module and prefer logging functions over `print` for operational messages.

**✓ Good:**
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting processing.")
logger.warning("Low disk space.")
logger.error("Failed to connect to server.")
```

**✗ Bad:**
```python
print("Starting processing.")   # No levels, no timestamps, hard to redirect
print("Something went wrong!")
```

### Log levels (brief)

| Level   | Typical use                          |
|---------|--------------------------------------|
| DEBUG   | Detailed diagnostic information      |
| INFO    | General progress or key events       |
| WARNING | Something unexpected but not fatal   |
| ERROR   | A failure that affects the operation |

### Logging exceptions

Use `logger.exception()` in an except block to automatically include the traceback.

**✓ Good:**
```python
try:
    risky_operation()
except OSError as e:
    logger.exception("Operation failed: %s", e)
```

---

## Summary

- **Error handling**: Use `try`/`except` to catch specific exceptions, raise exceptions when your code detects invalid state, and use `finally` (and optionally `else`) for cleanup and follow‑up logic.
- **Logging**: Use the `logging` module with appropriate levels (INFO, WARNING, ERROR) instead of `print` for operational messages, and use `logger.exception()` when logging inside an except block.

Together, error handling and logging make your programs easier to run, debug, and maintain.
