def debug(tag, output_val):
    print(f'(tag):{output_val}')
    
x = 2
y = 2.4

print("the value of x is ", x)
print("the value of y is: " , y)

debug("value of x is : ", x)

name = "aaryan"
debug("name is :", name)

is_boolean = True
debug("is_boolean is: ", is_boolean)

# basic math operations

sum = x + y
debug("sum is: ", sum)

diff = x - y
debug("diff is :" , diff)

product = x*y
debug("product is : ", product)

quotient = x / y
debug("quotient", quotient) 

#typecasting - floating point number (decimal) to integer valuee

quotient_as_int = int(quotient)
debug("quotient as int", quotient_as_int)

remainder = 13 % 5
debug("remainder is : ", remainder)
print("remainder is :" , remainder)

#type casting - boolean to string

isAge = True
isString = str(isAge)
print("boolean converted to string", isString)
print("Type changed from ", type(isAge), "to :" , type(isString))


# control statements

#if statemeent


age = 90

if age >= 18 and age <= 65:
    print("You are an adult")
elif age >= 65:
    print("you are a senior ")
else:
    print("you are a minor")
    
# using and/or 

is_sunny = True
is_weekend = False

if is_sunny and is_weekend:
    print("Have a walk")
elif is_sunny or is_weekend:
    print("go home")
else:
    print("Have a good day")
    

# comparison operators

x = 10
y = 4

if x>y:
    print("{x} is greater than {y}")
elif x<y:
    print("{x} is less than {y}")
else:
    print("{x} is equal to {y}")

z = 6

# inverting booleans
is_teacher = True
is_inverted_teacher = not is_teacher
print("inverted boolean  value ", is_inverted_teacher)

#Data structures

# lists are ordered and they can contain duplicate , their content can be modified, similar to array

my_list = [1,2 ,3,4,5]
print("First item in lists",  my_list[0])

# last item of lists
print("last item of list", my_list[-1])

#append an item to the list
my_list.append(6)
print("appendede item in lists", my_list)

# get range of items
my_names = ['bob', 'jane','john']
print('get range', my_names[1:])

# remove dupes from list
my_list.append(1)
print("updated lists:", my_list)

unique_list = set(my_list) #set does not contain duplicate elements
print("unique list is : ", unique_list)

unique_list1 = list(set(my_list)) 
print("unique list1 is: ", unique_list1)

#tuples are ordered and can contain duplicates . They are immutable and contents cannot be modified 
my_tuple = (1, 2,3,4,5)
print("first item in the tuple",my_tuple[0])
print("first item in the tuple",my_tuple[-2]) #print second last element present in the tuple

# you cannot edit the contents of a tuple 

my_tuple_2 = (True, False, True, False)
print("boolean tuple" , my_tuple_2)

unique_tuple = tuple(set(my_tuple_2))
print("unique tuple now is ", unique_tuple)



# dictionaries have key - value pair enteries where the key is a unique value and value can be duplicated 

my_dict = {'name':'Aaryan', 'age': 22} 

print("dictionary is :", my_dict)
print("name is:", my_dict['name'])
print("age is :" , my_dict['age'])

# adding a new entry to the dictionary 
my_dict['country'] = 'India'
print("updated dictionary is ", my_dict)


#Loops 

#for loop

numbers = [12,3,23,23,45334]

for number in numbers:
    print("for loop", number)
    
    
# while loop 
count = 0

while(count < 5):
    print("while loop", count)
    count += 1
    
#FUnctions and modules

#functions with no parameters

def say_hello():
    print("Say hello function")
    
say_hello()

# function with parameters

def greet(time_of_day, name):
    print(f'Good {time_of_day} {name}')

greet('morning', 'Aaryan')
greet('afternoon', 'Aaryan')


#modules
import math
print("square root ",int(math.sqrt(25)))


#classes

# create class
class Human: 
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print("go out")
        
my_human = Human('Aaryan','22')
print(my_human.name)
my_human.eat()



#File Handling 
filename = 'example.txt'

# writing to a file
file = open(filename, 'w')
file.write("This is a text file")
file.close()


#reading entire file contents
with open(filename, 'r') as file:
    content = file.read()
    print("file content is ", content)
    

#exception handling 
try: 
    with open("file_does_not_exists.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")