import string

def check_strength(password):
    length = len(password) >= 8
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in string.punctuation for char in password)

    score = sum([length, lower, upper, special])

    if score <= 2:
        return "Weak "
    elif score == 3 or score ==4:
        return "Medium "
    else:
        return "Strong "
    
password = input("Enter your password : ")
Strength = check_strength(password)
print("Password Strength:", Strength)