# Streaming Log Analyzer

A Python project focused on processing and analyzing large log files efficiently without loading the entire file into memory.

## About the Project

This project was built as part of my intermediate Python practice, with a focus on writing cleaner, more structured, and maintainable Python code.

The analyzer processes log files using **iterators and generators**, allowing data to be handled lazily as it is read. It supports filtering log entries and performing basic statistical analysis while keeping memory usage low, which is useful when working with large log files.

The project also focuses on practical Python development patterns rather than just getting the program to work. It uses **decorators, context managers, dataclasses, and type hints**, with the code organized into separate packages and modules.

## What It Does

* Processes large log files using lazy iteration
* Filters log entries based on different conditions
* Performs basic log statistics and analysis
* Uses generators to avoid unnecessary memory usage
* Uses dataclasses for structured log data
* Uses context managers for safe resource handling
* Uses type hints for clearer and more reliable code
* Includes automated tests with `pytest`
* Uses `mypy` for static type checking
* Follows a package-based project structure

## What I Learned

Through this project, I practiced:

* Iterators and generators
* Decorators and context managers
* Dataclasses and type hints
* File handling and lazy processing
* Writing reusable Python modules
* Structuring a Python project as packages
* Unit testing with `pytest`
* Static type checking with `mypy`
* Designing code that is easier to maintain and extend

## Tech Stack

* **Language:** Python
* **Testing:** pytest
* **Type Checking:** mypy
* **Project Structure:** Python packages and modules
* **Core Concepts:** Iterators, generators, decorators, context managers, dataclasses, type hints

## Purpose

The main goal of this project was to move beyond basic Python syntax and practice how Python is used in a more realistic software development workflow, especially when working with large amounts of data and code that needs to remain organized and testable.
