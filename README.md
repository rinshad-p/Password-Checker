# Password Checker

A Python-based tool to check the strength of your password and verify if it has been exposed in any known data breaches.

---

## Features

1. **Password Strength Checker**:
   - Evaluates the strength of your password based on:
     - Length (minimum 8 characters)
     - Presence of uppercase and lowercase letters
     - Inclusion of numbers
     - Use of special characters
   - Provides feedback on whether the password is **Strong**, **Moderate**, or **Weak**.

2. **Breach Checker**:
   - Uses the [Have I Been Pwned](https://haveibeenpwned.com/API/v3) API to check if your password has been exposed in any known data breaches.
   - Returns the number of times the password has been found in breaches or confirms its safety.

3. **User-Friendly Interface**:
   - Colored console output for better readability.
   - Interactive prompts for checking multiple passwords.

---

## Requirements

- Python 3.x
- `requests` library (for API calls)
- `colorama` library (for colored console output)

---
