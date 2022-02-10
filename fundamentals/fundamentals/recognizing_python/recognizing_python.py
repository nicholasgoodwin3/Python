num1 = 42 # declared variable, initialized number
num2 = 2.3# declared variable, used float to initalize
boolean = True# declared variable, set to boolean
string = 'Hello World'# declared variable, set to string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']# variable declaration with a list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}# variable declaration with a dictionary
fruit = ('blueberry', 'strawberry', 'banana')# variable declared with a tuple.
print(type(fruit))# printing to console, type check
print(pizza_toppings[1])# printing to console, list value
pizza_toppings.append('Mushrooms')# adding item to list
print(person['name'])# printing to console, dictionary value
person['name'] = 'George'# dictionary value change
person['eye_color'] = 'blue'# dictionary value change
print(fruit[2])

if num1 > 45: # if else statement that prints to console based on conditional
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:# if elif else statement that prints to console
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):# for loop for 0-5
    print(x)
for x in range(2,5):# for loop for 2-5
    print(x)
for x in range(2,10,3):#for loop for 2-10
    print(x)
x = 0 # variblae declartaion inside for loop
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() # list deletion value
pizza_toppings.pop(1)# list deletion at index

print(person) # print from dicitionary 
person.pop('eye_color')# delete from dictionary
print(person)# print from dictionary

for topping in pizza_toppings:# for loop containing conditional
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break# stops the loop

def print_hello_ten_times():# for loop 0-10 with a declared function
    for num in range(10):
        print('Hello')

print_hello_ten_times()# calling function

def print_hello_x_times(x):# for loop 0-10 that prints hello world
    for num in range(x):
        print('Hello')

print_hello_x_times(4)# printing the statement * 4

def print_hello_x_or_ten_times(x = 10):# for loop that prints hello world to console until x
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()# calling this function until a default perameter
print_hello_x_or_ten_times(4)# calling this function to 4


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