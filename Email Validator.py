import re

def email_check(email):

    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    match = email_pattern.match(email)

    if match:
        return True
    else:
        return False

email_address = input("Enter an email address: ")
if email_check(email_address):
    print(f"{email_address} is a valid email address.")
else:
    print(f"{email_address} is not a valid email address.")

