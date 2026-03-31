# Password Strength Checker

import re

def check_password_strength(password):
    strength = 0

    # Conditions
    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&*!]", password):
        strength += 1

    # Result
    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Medium"
    else:
        return "Strong"


# Test input
password = input("Enter password: ")
result = check_password_strength(password)

print("Password Strength:", result)

Enter_password: Abc123
Password_Strength: Medium

Enter_password: Abc@12345
Password_Strength: Strong