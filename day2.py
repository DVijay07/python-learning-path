#Question:
#Ask the user to enter two city names, and check whether they are the same city or not (case sensitive).

city1= input("Enter the first city name:")
city2=input("Enter the second city name:")
if city1.lower()==city2.lower():
    print("Both are same city.")
else:
    print("Both are different cities.")

"""
Example Input:
Enter your age: 20  
Are you a citizen? (yes/no): yes

Expected Output:
You are eligible to vote.
"""
age = int(input("Enter your age:"))
citizen = input("Are you a citizen? (yes/no):")

if age >=18 and age <=100 and citizen.lower()=='yes':
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
######################################################
member = input("Are you a member? (Yes/No):")
amount =(float(input("Enter your bill amount:")))
if member.lower() == 'yes' or  amount >1000:
    print("Discount applicable")
else:
    print("no discount applicable")
######################################################
maths = (int(input("maths_mark:")))
science = (int(input("Science_mark:")))
avg = (maths + science)/2
average = int(avg)
print("Averag_mark:",average)

if maths >=60 and science >=50 and average >= 55:
    print("You are eligible for admissionyes")
else:
    print("You are not eligible for admiissionyes")
######################################################

weekend = input("It's a weekend? (yes/no):")
coupon = input("Do you have coupon (yes/no:)")
birthday = input("Is it your birthday (yes/no))")

if weekend.lower() == "yes" or coupon.lower() == "yes" or birthday.lower() =="yes":
    print("You get a special offer!")
else:
    print("Your not eligible to get a special offer!")

#job eligibility system

degree = input("Do you have a degree? (yes/no):")
experience = int(input("Enter your years of experience:"))
freshers = input("Are you a fresher? (yes/no):")

if degree.lower() == "yes" and experience >=2 and freshers.lower() =="no":
    print("Your qualified for the job.")
else:
    print("Your not qualified for the job.")

#loan approval system

income = input("Stable income ?(yes/np):")
credit_score = int(input("credit score:"))
guarantor =input("Do you have a guarantor? (yes/no):")

if income.lower() =="yes" and credit_score >=700 or guarantor.lower() =="yes":
    print("Loan approved")
else:
    print("Loan denied")

balance = 55800
deposit =float(input("Enter the amount to deposit:"))

updated_balance = balance + deposit  # blance += balance + deposit
print("current balance is :",updated_balance)

balance = 500
spend = int(input("Enter the amount to spend:"))
balance -=spend
print("Remaining balance is :",balance)
#######################################################

product_cost = 1200
product_cost -= product_cost * 0.15
print ("Discounted price is :",product_cost)

age = int(input("Enter your age:"))
citizen = input("Are you a citizen? (yes/no):")

# Operators arthimetic operators
amount = 1200
tax = amount * 0.18
total_amount  = amount+tax
print("Total amount including tax is:", total_amount)

if amount >1000:
    discount = total_amount * 0.10
    total_amount -=discount # total_amount_discounted  = total_amount - discount 
    print("Total amount after discount is:", total_amount) #  total_amount_discount

factory_unit= 500
for factory in range (1, 4):
    factory_unit *= 1.15
    print(f"Day {day}:{factory_unit:2f} units")