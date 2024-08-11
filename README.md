# Code Review Project

## Overview

This project is focused on conducting a secure code review for Python applications. 
The goal is to identify and address potential security vulnerabilities in the code. 
The project uses the [Bandit](https://bandit.readthedocs.io/en/latest/) tool to scan Python files for common security issues.

## Purpose

The purpose of this project is to demonstrate how to perform a secure code review using a Python script. 
The script automates the process of running Bandit, a security linter for Python, on specified files or directories. 
This helps developers ensure their code is following best practices and is free from common security vulnerabilities.

## Files in the Project

- **`runpy`**: This Python script checks the provided file or directory path and runs Bandit on it to identify security issues.
- **`insecure.py`**: A sample Python file containing intentional security flaws, used to demonstrate how Bandit detects issues.
- - **`secure.py`**: A sample Python file containing the issues secured and cleared.

## Prerequisites

Before running the code review script, make sure you have the following installed on your system:

- **Python 3.x**: Required to run the Python scripts.
- **pip**: Python's package installer.
- **Bandit**: The security linter tool used in this project.

You can install Bandit using pip:
pip install bandit
