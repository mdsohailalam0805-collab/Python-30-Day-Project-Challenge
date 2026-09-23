name = input("Enter your name: ")

balance = 1000

print("\nWelcome,", name)
print("Your current balance is:", balance)

deposit = int(input("\nEnter deposit amount: "))
balance = balance + deposit

print("Balance after deposit:", balance)

withdraw = int(input("\nEnter withdrawal amount: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal successful!")
else:
    print("Insufficient balance!")

print("\n----- Account Summary -----")
print("Name:", name)
print("Final Balance:", balance)