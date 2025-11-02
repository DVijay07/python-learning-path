"""
a=10
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)

"""
#Area of rectangle

length =10
width = 5
area = length*width

print(area)

#calculate the final price

original_price=1000
discount=original_price*0.20
final_price = original_price - discount
print(final_price)

total_minutes = 130
hours=total_minutes //60
minutes = total_minutes %60

print("hour's:",hours)
print("minutes:",minutes)

# calculate simple intrest

principal = 10000        #initial amount
interest_rate = 0.10     #10%
time = 5                 #in years

simple_intrest = principal * interest_rate * time
print(simple_intrest)

#calculate compound intrest
p=10000
r=0.10
t=5
n=1

compound_interest = p * (1 + r/n)**(n*t) - p
print(compound_interest)

#calculating BMI(body mass index)

weight_kg = 70
height_m = 1.75

bmi = weight_kg//(height_m**2)
print(bmi)

# COMPARISON OPERATORS

# write a program , whether  first number is greater than second number

num1 = input("Enter the first number:")
num2 = input("Enter te second number:")

if num1 > num2:
    print(num1,"is greater than",num2)
elif num1== num2:
    print(num1,"is equal to",num2)
else:
    print(num1,"is smaller than",num2)


"""
Question:
Ask the user to enter their exam score (out of 100).
If the score is:
50 or above → “Pass”
Below 50 → “Fail”
"""
score = (int(input("Enter your score:")))

if score >=50:
    print("Pass")
else:
    print("Fail")

#Ask the user to enter the ages of three people, and determine who is the oldest.
age1 = int(input("Enter the age of first person:"))
age2 = int(input("Enter the age of second p" \
"erson:"))
age3 = int(input("Enter the age of third person:"))
if age1 > age2 and age1 > age3:
    print("First person is the oldest.")
elif age2 > age1 and age2 > age3:
    print("Second person is the oldest.")
else:
    print("Third person is the oldest.")
    
"""Question:
Write a Python program that asks the user to enter the current temperature in Celsius.
If the temperature is greater than or equal to 30, print "It's a hot day!",
otherwise print "It's a pleasant day.
"""
temperature =float(input("Enter the current temperaturein celsius:"))
if temperature >=30:
    print("it a hot day..!!")
else:
    print("have a good day..!!")

