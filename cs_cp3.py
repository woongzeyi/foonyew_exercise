"""Python CP. 3 - Practice"""
# Question 1 & 2
P = 10000
r = 0.02
t = 10
A = P * (1 + r)**t
print("Question 1: ")
print(int(A))
print()
print("Question 2: ")
print(round(A))
print()

# Question 3
print("Question 3: ")
MINUTES_IN_AN_HOUR = 60
MINUTES_IN_A_DAY = 1440
d = 384400
s = 250
t = d / s
t_in_days = int(t // MINUTES_IN_A_DAY)
t_in_hours = int(t % MINUTES_IN_A_DAY // MINUTES_IN_AN_HOUR)
t_in_minutes = int(t % MINUTES_IN_A_DAY % MINUTES_IN_AN_HOUR)
print(f"{t_in_days}d{t_in_hours}h{t_in_minutes}m")
print()

# Question 4
print("Question 4: ")
PI = 3.141592653589793
r = 5
print(int(PI * (r ** 2)))
print()



