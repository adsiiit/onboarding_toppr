##lists

#list = ["abcd",786, 2.23, "john"]
#tinylist = [123, "john"]
#print list
#print list[0]
#print list[1:3]
#print tinylist * 2
#print list + tinylist


##tuples

# tuple = ('acbd', 432, 2.23,534)
# tinytuple = (123, 'john')
# print tuple
# print tuple[2:]
# print tuple+tinytuple
# del tuple


## dictionary

# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
# tinydict = {'name': 'john', 'code': 6745, 'dept': 'sales'}

# print dict['one']
# print tinydict.keys()
# print tinydict.values()
# del dict


## conditional statements

# var = raw_input("Enter some value:")
# try:
#     var = int(var)
#     if ( var == 100 ):
#         print "Value  is 100"
#     elif ( var == 50 ):
#         print "Value is 50"
#     else:
#       print "Kuch bhi"
# except ValueError:
#     print("That's not an int!")


## strint format

# print "My name is %s and weight is %d kg!" %('Aman', 50)


## functions -- call by reference

# def changeme( mylist ):
#    "This changes a passed list into this function"
#    mylist.append([1,2,3,4]);
#    print "Values inside the function: ", mylist
#    return

# mylist = [10,20,30];
# changeme( mylist );
# print "Values outside the function: ", mylist


## Function -- variable length arguments

# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print "Output is: "
#    print arg1
#    for var in vartuple:
#       print var
#    return;

# printinfo( 10 )
# printinfo( 70, 60, 50 )


## lambda function

# sum = lambda arg1, arg2: arg1 + arg2;
# print "Value of total : ", sum( 10, 20 )


## namespace and scoping

# Money = 2000
# def AddMoney():
#    global Money
#    Money = Money + 1

# print Money
# AddMoney()
# print Money

## Package example
# import Phone

# Phone.Pots()
# Phone.Isdn()
# Phone.G3()


## Exception handling

# try:
#    fh = open("testfile", "r")
#    fh.write("This is my test file for exception handling!!")
# except IOError:
#    print "Error: can\'t find file or read data"
# else:
#    print "Written content in the file successfully"

# try:
#    fh = open("testfile", "w")
#    try:
#       fh.write("This is my test file for exception handling!!")
#    finally:
#       print "Going to close the file"
#       fh.close()
# except IOError:
#    print "Error: can\'t find file or read data"

## Raising and handling the exception

# def functionName( level ):
#     if level < 1:
#       raise OverflowError
#       # The code below to this would not be executed
#       # if we raise the exception
#     else:
#         print ( "Level is greater than 1" )
# try:
#     functionName(-5)
# except OverflowError:
#     print("Exception handling here...")
# else:
#    print("Rest of the code here...")


## User-defined exceptions
# class Networkerror(RuntimeError):
#    def __init__(self, arg):
#       self.args = arg
# try:
#    raise Networkerror("Bad hostname")
# except Networkerror,e:
#    print e.args



## Code as per PEP8 standards

# Python program to find the factorial of a number provided by the user.
 
# change the value for a different result
num = 7
 
# uncomment to take input from the user
#num = int(input("Enter a number: "))
 
factorial = 1
 
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)