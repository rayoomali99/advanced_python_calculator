# 🧮 Advanced Python Calculator

A modular, interactive calculator written in Python.  
Supports multiple arithmetic operations, safe error handling, and a live calculation history — perfect as a first portfolio project for Python and data roles.

---

## ✨ Overview

This project is a command-line calculator that lets the user:

- Perform basic arithmetic
- Calculate powers (x^y)
- See a complete history of all calculations done in the current session
- Exit safely without crashing on wrong inputs

It was built to practice **functions**, **loops**, **input validation**, and **exception handling** in a clean, readable way.

---

## ✅ Features

- **Arithmetic operations**
  - ➕ Add  
  - ➖ Subtract  
  - ✖ Multiply  
  - ➗ Divide *(with zero-division protection)*  
  - 🔼 Power (x^y)

- **History tracking**
  - Every calculation is stored as a formatted string  
  - User can display the full history at any time

- **Input safety**
  - Handles non-numeric inputs using `try / except`
  - Handles division by zero gracefully

- **User-friendly menu**
  - Simple text menu with numbered options
  - Loops until the user chooses to exit

---

## 🧠 Concepts Used

- Functions for each operation *(add, subtract, multiply, divide, power)*
- **While loop** for continuous program execution
- **List** for storing calculation history
- **try / except** for:
  - Non-numeric input
  - Division by zero
- **String formatting** for readable output

---

## 🧠 How it works

On every loop, the program shows this menu:

```text
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power (x^y)
6. Show History
7. Exit


The user chooses an option (1–7)

For operations 1–5, the user enters two numbers

The result is printed and saved in a history list, e.g:
10 + 5 = 15.0
3 ^ 4 = 81.0
20 / 4 = 5.0

Option 6 prints the full history

Option 7 prints a goodbye message and ends the program






