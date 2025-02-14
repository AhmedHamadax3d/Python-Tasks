# Create a Boolean variable named x
x=True 

#  Create an integer variable named y
y=10

#  Create a float variable named z
z=3.2

#  Create a string variable names s
s='Ahmed'

# Convert the int variable to float
print(float(y))

# Can we convert the str to int ?>>>>>no 

# Create a list of numbers from 1 to 5
numbers=[1,2,3,4,5]
numbers=(list(range(1,6)))


#  Create a tuple from 10 to 15
t=(1,2,'Ahmed',False)

# Convert the list to tuple
print(tuple(numbers))


#  Create a dict of 3 values
students={1:'Ahmed',2:'Ali',3:'Amir'}

#  Can we use semi colon ; with python>>>>>yes

# Python is interpreted or compiled ?>>>>> is interpreted.

# What is the differences between low level & high level>>>>
# **Low-level languages are closer to the machine's hardware and architecture.
# **High-level languages are designed to be more user-friendly and abstracted from hardware details.

# What is the differences between = , ==
# **= (Assignment Operator)
# **==  compare two values

# What do we mean by using !=
# It is used to compare two values or expressions.
# It returns True if the values are not equal and False if they are equal.

# What is the operator precedence?
# Operator precedence determines the order in which operators are evaluated in an expression when multiple operators are present.
# Operators with higher precedence are evaluated before those with lower precedence. 
#If operators have the same precedence, their evaluation order is determined by their associativity (left-to-right or right-to-left)

# Create a variable x with value of 10 
x=10

# Increase x value by 15 using assignment operators
x+=15

# Divide the x value by 5 using assignment operators
x/=5 

# Multiply the x value by 10 using assignment operator
x*=10

# Get module of x on 3 using assignment operators
x%=3 

# Using python print the module of 11 to 4
print(11%4)

# Print the exponent of 2,3
print(2**3)

# Divide 11 by 3 using python division
print(11/3)
print(11//3)

# Can we divide 11 by 3 and get an integer number ?
x=int(11/3)
print(x)

# Check if 10 is bigger than 15 or not
# If 10 is not bigger than15 print x is smaller than 15
x=10
if x>15 :
    print(f'{x} is bigger than 15')
else :
    print(f'{x} is less than 15')

# What is the differences between all , and
# all works on iterables and checks if all elements satisfy a condition.
# and works on two boolean expressions and checks if both are True.

# What is the differences between any , or
# any works on iterables and checks if any element satisfies a condition.
# or works on two boolean expressions and checks if at least one is True

# If we need all the conditions to be true we will use ….>>>and ,all 

# What is the differences between if , elif
# Use if when you want to check a standalone condition or the first condition in a series.
# Use elif when you want to check additional conditions that should only be evaluated if the previous conditions are False.

# What is the differences between elif else
# Use elif to check additional conditions.
# Use else as a fallback when no conditions are True.
# Both are optional, but else must come after all if and elif statements.

# Can we use more than one elif>>>yes

# Can we use more than one else>>>no

# write s simple ternary operator>>>True condition False
name='Ali'
print('Welcome') if name =='Ahmed' else print('who are you')

# in elif , python will check all the conditions no matter what ?
# In elif, Python does not check all conditions no matter what. It stops evaluating as soon as it finds a True condition.
# This behavior is called short-circuiting and makes elif efficient for handling multiple conditions.

#  in elif we use else for end condition ?

# if we have this list [2,4,6,8,10] :
#  ○ check to see if 4 in this list or not
#  ○ check to see if 4 and 6 in this list or not
#  ○ check to see if 3 or 6 in this list
#  ○ check to see if 2 , 4 and 5 in this list

L=[2,4,6,8,10]

if 4 in L :
    print('4 is exist')
else :
    print ('not exist')

if 4 and 6 in L :
    print('4 and 6 is exist')
else :
    print('not exist')

if 3 or 6 in L :
    print('3 or 6 is exist')
else :
    print('not exist')

if 2 or 4 and 6 in L :
    print('There exist')
else :
    print('no exist')
#End .......................................................