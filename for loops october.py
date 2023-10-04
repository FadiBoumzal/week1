age1=input("enter your age")
age1=int(age1)
if age1>=18:
    print("you can vote")
if age1==17:
    print("you can learn to drive")
if age1==16:
    print ("you can buy a lottery ticket")
    
    
number1=input("enter a number")
number1=int(number1)
if number1 < 10:
    print("too low")
if number1 >=10 and number1 <=20:
    print("correct")
else:
    print("too high")
    
number2=input("enter 1, 2 or 3")
number2=int(number2)
if number2 == 1:
    print("thank you")
elif number2==2:
    print("well done")
elif number2==3:
    print("corrects")
else:
    print("error message")
    
name=input("enter your name")

for name1 in range(0,3,1):
    print(name)