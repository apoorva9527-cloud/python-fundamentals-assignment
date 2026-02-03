age = int(input("Enter your age: "))
has_id_input = input("Do you have an ID card? (True/False): ")

has_id = has_id_input == "True"

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
