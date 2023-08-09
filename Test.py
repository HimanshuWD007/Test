# Q 1 Countiong odd numbers

"""odd=0
while True:
    n=int(input("Enter your number ="))
    if n<0:
        break
    elif n%2==1:
        odd=odd+1
print(f"You've entered {odd} numbers")"""



# Q2 Number guessing game

"""import random
print("Welcome to the Number guessing game!!")
while True:
    n=int(input("Guess the number ="))
    guess_num=random.randint(1,100)
    if n==guess_num:
        print("Congrats you guessed the right number")
    elif n<guess_num:
        print("Your guess is too low")
    elif n>guess_num:
        print("Your guess is too high")"""


# Q1 ( Conditional statement )

"""n=int(input("Enter total marks of the student ="))
per=(n/500)*100
if per>=90:
    print("Congrats!! you got A grade")
elif per>=80 and per <90:
    print("You got B grade")
elif per>=70 and per<80:
    print("you got C grade")
elif per >=60 and per<70:
    print("you got D grade")
elif per<60:
    print("You got F grade")"""


# Q2 Odd or even

"""n=int(input("Enter your number ="))
if n%2==1:
    print("Its an odd  number")
else:
    print("Its an even number")"""

# Q3
"""
y=int(input("Enter the year ="))
if y%4==0 and y%4==0:
    print("Its a leap year")
else:
    print("Its a normal year")"""


# Q4 positive negitive zero

"""n=int(input("Enter your number ="))
if n<0:
    print("Its a negitive number")
elif n>0:
    print("Its a positive number")
else:
    print("Its zero")"""


# Q5 Triangle type

"""a=int(input("Enter first side of the triangle="))
b=int(input("Enter second side of the triangle="))
c=int(input("Enter third side of the triangle="))
if a==b==c:
    print("Its an equilateral triangle")
elif a==b and a!=c or b==c and b!=a :
    print("Its a isosceles triangle")
elif a!=b!=c:
    print("Its a scalene triangle")"""
