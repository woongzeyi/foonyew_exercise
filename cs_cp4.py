# Question 1
print("Celsius to Fahrenheit Converter!")
print("Fahrenheit: %5.2f" % (float(input("Celsius: ")) * (9 / 5) + 32))

# Question 2
print("\nBMI Calculator!")
print("Your BMI: %4.1f" % (float(input("Your weight: ")) / (float(input("Your height: ")) ** 2) * 10000)) # 不乘个10000很奇怪

# Question 3
print("\nPersonal Information Collection!")
name = input("Name: ")
contact_number = input("Contact number: ")
email_address = input("Email address: ")
birth_date = input("Birth date: ")
print(f"Your name: {name} \nYour contact number: {contact_number} \nYour email address: {email_address} \nYour birthday: {birth_date}")


