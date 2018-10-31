
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

var1, var2, var3 = input("enter three no seprated by comma:").split(",")
l=[var1,var2,var3]
print(l)
print(tuple(l))


#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
str=input("enter any sentance: ")
c1=0
c2=0
c3=0
for a in str:
    if (a.isupper()) == True:
        c1=c1+1
    elif(a.islower())==True:
        c2=c2+1
    elif(a.isspace())==True:
        c3=c3+1

print("uppercase:==>",c1)
print("lower case:==>",c2)
print("space:==>",c3)



#Define a function that can accept two strings as input and concatenate them and then print it in console.
def str():
    s1=input("enter 1st string:")
    s2=input("enter 2nd string:")
    s3=s1+s2
    print(s3)
    return
str()



#Create a program that asks the user to enter their name and their age.
#  Print out a message addressed to them that tells them the year that they will turn 100 years old.
name=input('enter your name')       #name input
age=int(input("enter your age"))
a=2018-age
b=a+100
print("hello {} sir".format(name))
print("your age is:",age)
print("And you will be 100 years old in {} ".format(b))




#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
for x in range(2000,3201):
    if x%7==0 and x%5!=0:
        print(x,end=',')




