#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
message = f"Last digit of {number} is"
if number > 5:
    message += f" {last_digit} and is greater than 5"
elif number == 0:
    message += f" {last_digit} and is 0"
else:
    last_digit = abs(number) % 10
    message += f" -{last_digit} and is less than 6 and not 0"
print(message)
