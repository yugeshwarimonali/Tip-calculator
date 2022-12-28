# print("Welcome to tip Calculator.")
# bill = float(input("What was the total bill? $"))
# people = int(input("how many People to split the bill? "))
# total_bill = bill/people
# print(f"Each person should pay : ${total_bill}")

############## add percentage 
print("Welcome to tip Calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("how many People to split the bill? "))

persent = int(input("What percentage tip would you like to gib=ve ? 10,12, or 15? "))
percent_with_bill=(100/bill)*persent
add_percent_bill = percent_with_bill +bill

total_bill =round(add_percent_bill/people,2)

print(f"Each person should pay : ${total_bill}")