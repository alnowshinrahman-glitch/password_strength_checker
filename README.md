# Password Strength Checker 🔐

A Python program that evaluates the strength of a user-provided password and gives clear feedback on how to improve it.

This project was built to practice Python fundamentals, including:
- Strings
- Loops
- Conditionals
- Functions
- Boolean logic
- Git & GitHub workflow

---

## Features

- Checks password length (minimum 8 characters)
- Detects:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
- Provides specific feedback for missing requirements
- Classifies password strength as:
  - Strong
  - Medium
  - Weak

---

## How It Works

1. The user is prompted to enter a password.
2. The program analyzes the password character by character.
3. Missing requirements increase a `strength` counter.
4. Based on the total number of issues, the password is classified.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/alnowshinrahman-glitch/password_strength_checker.git
