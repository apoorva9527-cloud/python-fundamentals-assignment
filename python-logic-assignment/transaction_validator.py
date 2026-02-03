balance = int(input("Enter your account balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
verified_input = input("Are you verified? (True/False): ")

verified = verified_input == "True"

if verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
