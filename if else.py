age= 17
if age >= 18:
    print("eligible to vote")
else:
  print("not eligible to vote")



  temperature = 20

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's warm.")
elif temperature > 10:
    print("It's cool.")
else:
    print("It's cold.")

grade = 85
attendance = 90

if grade >= 60:
    if attendance >= 75:
        print("Pass")
    else:
        print("Fail due to low attendance")
else:
    print("Fail due to low grades")


    # Predefined credentials
correct_username = "admin"
correct_password = "1234"

# User input
username = input("abhay: ")
password = input("patil: ")

# Check username
if username == correct_username:
    # Nested check for password
    if password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")


p=10
q=20
print("p is greater than q"if p > q else "q is greater than p")



