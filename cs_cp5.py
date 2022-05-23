# Question 1
print("Integer absoluter!")
val1 = int(input("Integer value: "))
if val1 < 0:
    val1 *= -1
print("Absolute integer value:", val1)

# Question 2
print("\nInteger reverser!")
val2 = int(input("Integer value: "))
print("Reversed integer value:", val2 * -1)

# Question 3
print("\nDisney ticket price calculator!")
age = int(input("Age: "))
ticket_price = 200
if (age <= 6) or (age >= 80):
    ticket_price *= 0.2
elif (age in range(7, 12 + 1)) or (age in range(60, 79 + 1)):
    ticket_price *= 0.5
print("Ticket price:", int(ticket_price))


