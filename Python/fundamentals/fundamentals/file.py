"""This is Danny's File and interpretation 
and explanation of the following lines of code"""

num1 = 42 #- variable declaration  - Initializing Number
num2 = 2.3   #- variable declaration  - Initializing Number
boolean = True    #- variable declaration  - Initializing Boolean
string = 'Hello World' #- variable declaration  - Initializing String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  
"""
Above, pizza_toppings makes a variable declaration  - Initializing a List/Array 
which holds various values that are composed of strings
"""

"""
Below, person, is a declared variable that initializes a dictionary with various 
key value pairs
"""

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}


fruit = ('blueberry', 'strawberry', 'banana') 
#fruit is a declared tuple variable. 
#it holds 3 string values

print(type(fruit)) #Logs the returned result of the function "type()" - in this case
# it returns the variable-type that 'fruit' is.

print(pizza_toppings[1]) #logs the indicated value of the list pizza-topping at 
#index location 1


pizza_toppings.append('Mushrooms') #concatonates the String "Mushrooms"
#to the variable 'pizza_toppings' - adding to it a new index value

print(person['name']) """given that this calls the variable 'person', a dictionary, with 
a string 'name' - this string acts as a possible key, which holds a corresponding 
value that is being accessed and will be logged by the print command 
***Because the dictionary holds 'name' as the key to the value 'John' - the value
will be logged
"""


person['name'] = 'George' """ the variable person - a dictionary - is called - 
at its key 'name' - and the value of this key is being assigned/changed 
to a new value of 'George' 
"""

person['eye_color'] = 'blue'   # the variable person - a dictionary - is called
#a key 'eye_color' is being assigned the value 'blue' - because this key does not 
#currently exist, it will be added to the dictionary


print(fruit[2]) #the variable fruit - a tuple- at it's index value of 2 (the
#value in the 3rd position of the tuple), will be logged

"""Below is a set of conditionals that log either a 
string 'It's greater' or the string 'It's lower' given whether the conditional
num1 > 45 proves true or false"""
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

"""Below is a set of conditionals including if, elif, or else 
that log different strings according to a parameter set based on the length of 
the variable "string"."""


if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

""" below is a for loop that logs the value of x as it loops through
a range of given values"""
for x in range(5):  #x is assigned the initial value of 0 and starts a sequence
    print(x)          #proceding to the statement which logs its value. 
                      #once this statement is completed, the for loop increments 
                      #the value of x until it is equal to value in the range()
                      #function - at which point the for loop breaks/terminates
for x in range(2,5): #this will log x as it begins at the value 2 and terminates
    print(x)        #when the value of x is incremented to 5 - not logging its 
                    #last value of 5.
for x in range(2,10,3):   #x's value will be logged beginning at 2, with the 
    print(x)            #for loop ending whenever x's value reaches 10 -
                        #the 3rd input in the range function tells this function
                        #to increment x's value by 3 at the beginning of each 
                        # of the loop's cycle. 

x = 0                   #x is a variable called and assigned the value of 0 
while(x < 5):           #a while loop is initiated with the conditional x<5
    print(x)            #which initiates a sequence of logging x and incrementing its
    x += 1              #value by 1 until the condition proves false - thereby stopping
                        #the loop/sequence

pizza_toppings.pop()   #the variable pizza (an array/list) is called and 
  #the function .pop() removes and calls while logging
                        #its final value 

pizza_toppings.pop(1) #when .pop() has a value - it removes and logs the value 
#in the list pizza_toppings at the index value given

print(person)   #logs the dictionary, 'person', and all its keys and value pairs
person.pop('eye_color') #.pop() logs and removes the key and value at person's key 'eye_color'
print(person) #this logs the keys and values of person - no longer displaying popped key values

for topping in pizza_toppings:   #this for loop assigns the variable 'topping' the values 
    if topping == 'Pepperoni':    # of each of pizza_toppings at each index value in incrementing fashion
        continue                        #2 conditional parameters are set, and if the first is met, 
    print('After 1st if statement')   #the continue statement returns the control to the beginning of the  
    if topping == 'Olives':             #for loop and incrementing to the next index value. When it meets the second condition
        break                            #and the value at the index is "Olives" the for loop breaks

def print_hello_ten_times():            #defines a function print_hello_ten_times()
    for num in range(10):           #when called, this function goes through a for 
                                  #loop it logs 'Hello' for each time it loops through 
                                  #10 times, since its starting value is 0 and the 
                                  #condition passes through 10 times until it needs to end

        print('Hello')              
print_hello_ten_times()

def print_hello_x_times(x):    #similarly to the function defined above, when called 
    for num in range(x):       #this function logs "Hello" as num loops from a value 
        print('Hello')          #of 0 until it stops at the input value of x(determined by input)

print_hello_x_times(4)          #prints 'Hello' 4 times

def print_hello_x_or_ten_times(x = 10):    #Similarly to above functions, this function
    for num in range(x):                #has an input which is currently assigned the variable x
        print('Hello')                  #with a value of 10 - however, 
                                        # given a different input, the input value is assigned
print_hello_x_or_ten_times()           #the for loop is given parameters to print 'Hello' either 
print_hello_x_or_ten_times(4)        #the original value of x (10) times or a new value as input


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)