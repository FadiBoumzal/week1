name = input("enter a name ")
print(name,"has now been invited")
count=0
count = count + 1

inv = input("do you want to invite anyone else y/n ")
while inv == "y":
    otherinv = input("enter another name ")
    count = count + 1
    
    inv = input("would you like to invite anyone else y/n ")
print(count,"people have been invited")


compnum=50
compnum = int(compnum)
numberguessed = 0
attempts = 0
number= input("Enter a number ")
number = int(number)
attempts = attempts + 1
while numberguessed < 1 :
    if number > compnum:
        print("too high.")
        number = input("enter another number. ")
        number = int(number)
        attempts = attempts + 1
    elif number < compnum:
        print("too low.")
        number = input("enter another number. ")
        number = int(number)
        attempts = attempts + 1
    elif number == compnum:
        numberguessed = numberguessed + 1


print("correcc, you took",attempts,"attempts to guess the number")





