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


# Q3  Password validation

"""import re
ve=0
while True:
    P=str(input("Enter your password ="))
    if len(P)==8:
        ve-=1
        break
    elif not re.search("[0-9]",P):
        ve-=1
        break
    elif not re.search("[A-Z]",P):
        ve-=1
        break
    elif not re.search("[a-z]",P):
        ve-=1
        break
    else :
        ve=0
        print("Valid password")
if ve==-1:
    print("Invalid password")"""

# Q1 Grade classifier ( Conditional statement )

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


"""def tri(first_side,second_side,third_side):
    print("Its an equilateral triangle") if first_side==second_side==third_side else print("Its a isosceles triangle") if first_side==second_side and first_side!=third_side or second_side==third_side and second_side!=first_side else print("Its a scalene triangle") if first_side!=second_side!=third_side else ""
tri(10,10,12)"""

# Q1  get even numbers ( Looping )

"""even_num=[i for i in range(1,21) if i%2==0]
print(even_num)"""

# Q2 Get factorial

"""def facto(n):
    fac=1
    for i in range(n,1,-1):
        fac=fac*i
    print(f"Factorial of {n} is {fac}")
facto(3)"""


# Q3 Table

"""def tab
    for i in range(n+1):
        print(f"{n} * {i} = {n*i}")
table(10)"""

# Q 4 sum of digits

"""def sum_digits(n):
    sum=0
    for i in str(n):
        sum=sum+int(i)
    print(f"Sum of the digits of given number is {sum}")
sum_digits(334)"""

"""def get_faninocci(num):
    fab=[0,1]
    if num<0:
        print("There is no fabinocci series for negitive number")
    elif num<0 and num>2:
        print(f"Fabinocci series for {n} is {fab}")
    else:
        for i in range(num):
            if num>2:
                fab.append(fab[i-1]+fab[i-2])
        print(f"Fabinocci series for {num} is {fab}")
get_faninocci(10)"""


# Q5 Right triangle number patern

"""n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()"""



