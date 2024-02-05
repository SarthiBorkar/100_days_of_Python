import re

def pass_strength_checker(password):
    if len(password) < 8:
        return "Weak: Password should be atleast 8 characters long."

    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return "Weak: Password should have both uppercase and lowercase letters."

    if not any(c.isdigit() for c in password):
        return "Weak: Password should contain at least one digit."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets all criteria."

if __name__ == "__main__":
    user_pass = input("Enter your password: ")

    result = pass_strength_checker(user_pass)
    print(result)
