#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#I predicted that this would print out 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#predict that this will record an error - as the parameters required are missing

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#I predict that this will return the number 5 (the second return is not reached)

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

#I predict that this function will return 5 and then print it 
# - the print (10) is not accessible as the loop is closed/terminated by the return statement before it


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#I predict that this will print out 5 twice

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#this will likely give an error, as nothing is actually returned by the function - kind of like Null + Null

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#This function will turn argument input into it as strings concatenated to each other 
# -I predict that this will return "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#will print 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #This one will return & print 7 - since the 1st condition is met
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #This one will return & print 14 - since the 1st condition is NOT met
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))#This one will return & print the result of (7 + 14)



#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#This will return (3 + 5)


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#This will print 500 - then enters the function and prints 300 - then exits and prints 500 since the value b is not returned outside of the function


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#prints 500 then prints 500 again, then goes into function when called and prints 300 and returns 
# the value of b - 300, then it prints b - the variable outside of the function


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#prints 500, then prints 500 again, then b is reassigned to any value returned from 
# the function foobar() - in this case it is 300 - then it finally prints b (300)

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#first this goes through the function foo() - which prints out 1, then goes through
#  function bar which prints out the number 3, then continues into the 4th 
# line of the function foo() to print out 3


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

#This last set of lines calls assigns a variable y to the function foo(). The function is then
#  run and results of this function are then printed - first 1 will print, then x is assigned
# any returned values of the function bar() - and then x is printed - which will print out 3 as well as the returned value of 5
#function foo's final line returns the value 10 which will also be printed.