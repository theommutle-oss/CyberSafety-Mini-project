password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password, add more characters.")
elif password.isalpha() or password.isdigit():
    print("Add both letters and numbers for stronger security.")
else:
    print("Strong password!")
