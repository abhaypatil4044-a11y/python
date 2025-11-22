import re

password = "Pass@123"

pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

if re.match(pattern, password):
    print("Valid password")
else:
    print("Invalid password")
