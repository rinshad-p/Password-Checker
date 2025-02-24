# check_password.py
import re

def check_password_strength(password):
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    numbers = bool(re.search(r'[0-9]', password))
    special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = sum([length, uppercase, lowercase, numbers, special])
    
    if score == 5:
        return "Strong password! Well done."
    elif score >= 3:
        return "Moderate password. Consider adding more variety."
    else:
        return "Weak password!!!.\nUse at least 8 characters with a mix of uppercase, lowercase, numbers, and symbols."