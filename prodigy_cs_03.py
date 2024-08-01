# -*- coding: utf-8 -*-
"""prodigy_CS_03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wB-UrCO3OWFpoaZUr4yzCQe8_kPPoL6E
"""

import re

def password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    criteria_met = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    if criteria_met == 5:
        return "Very Strong", criteria_met
    elif criteria_met == 4:
        return "Strong", criteria_met
    elif criteria_met == 3:
        return "Moderate", criteria_met
    elif criteria_met == 2:
        return "Weak", criteria_met
    else:
        return "Very Weak", criteria_met

def main():
    while True:
        password = input("Enter a password to assess its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break
        strength, criteria_met = password_strength(password)
        print(f"Password Strength: {strength}")
        print(f"Criteria Met: {criteria_met}/5")
        print("Feedback:")
        if len(password) < 8:
            print("- Password should be at least 8 characters long.")
        if not re.search(r'[A-Z]', password):
            print("- Password should contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            print("- Password should contain at least one lowercase letter.")
        if not re.search(r'\d', password):
            print("- Password should contain at least one digit.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("- Password should contain at least one special character.")

if __name__ == "__main__":
    main()