name = input("Enter your name: ")
age = int(input("Enter your age: "))
active_input = input("Are you an active user (True/False): ")

active_status = active_input == "True"

print(f"User {name} is {age} years old. Active status: {active_status}")
