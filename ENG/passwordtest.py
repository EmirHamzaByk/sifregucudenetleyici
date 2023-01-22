import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak. Please use a password that contains at least 8 characters."
    elif not re.search("[a-z]", password):
        return "Weak. Please use a password that contains lowercase letters."
    elif not re.search("[A-Z]", password):
        return "Weak. Please use a password that contains uppercase letters."
    elif not re.search("[0-9]", password):
        return "Medium. Please use a password that contains numbers or special characters."
    elif not re.search("[!@#%&! @ # $ % ^ & * ( ) _ - + = { } [ ] \ | ; : '  , . < > / ?]", password):
        return "Medium. Please use a password that contains special characters or numbers."
    else:
        return "Strong"

while True:
    password = input("Please enter your password (type 'quit' to exit): ")
    if password == 'quit':
        break
    print("Your password is ", check_password_strength(password))
