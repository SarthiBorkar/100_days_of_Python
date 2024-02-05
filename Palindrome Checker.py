def palindrome_checker(s):
    s = s.lower().replace(" ", "")

    return s == s[::-1]

string =input("Enter text to check for palindrome:- ")
if palindrome_checker(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

