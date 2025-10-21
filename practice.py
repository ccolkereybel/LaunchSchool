# funcs = []
# for i in [1, 2]:
#     funcs.append(lambda: i)

# print([f() for f in funcs])

# '''
# Explain how you can use closure to create multiple independent 'counter" functions that returna n integer when invoked? The integer should increment by 1 at each invocation.
# '''

# #Solution


# x = make_counter('first_counter')
# y = make_counter('second_counter')

# x()   # first counter = 1
# x()   # first counter = 2
# y()   # second_counter = 1


# def logger(status, time, message):
#     return(f"{status.ljust(10)} | {time.ljust(7)} >>> {message}")

# #Your solution here

# #tests

# print(warning('12:30', 'Unfortunate incident') ==
#       "WARNING!   | 12:30   >>> Unfortunate incident")

# print(info('17:00', "It's five oclock!!!") ==
#       "Info       | 17:00   >>> It's five oclock!!!")

# print(test('01:23', 'Does this make my nose look big?') ==
#       "<test>     | 01:23   >>> Does this make my nose look big?")

#what is a closure?

"""
A closure is a function that remembers variables in its lexical scope. so it will
be able to access variables from an outer function, even after it has finished
exectuing. 
"""

"""
Use closure to create multiple independent counter functions that return an int
when involked. integer should increment by 1 at each invocation
"""

# def my_counter(name):
#     counter = 0
#     def increment_counter():
#         nonlocal counter
#         counter += 1
#         print(f'{name} has been envoked {counter} times')
#     return increment_counter

# counter1 = my_counter('counter1')
# counter2 = my_counter('counter2')

# counter1()
# counter1()
# counter2()

# print(counter1.__closure__)
# print(counter2.__closure__)

# #the closure is created when counter1() is called?

# def logger(status, time, message):
#      return(f"{status.ljust(10)} | {time.ljust(7)} >>> {message}")

# #Your solution here
# def define_status(status):
#      def create_log(time, message):
#           return logger(status, time, message)
     
#      return create_log

# warning = define_status('WARNING!')
# info = define_status('Info')
# test = define_status('<test>')

# #tests

# print(warning('12:30', 'Unfortunate incident') ==
#       "WARNING!   | 12:30   >>> Unfortunate incident")

# print(info('17:00', "It's five oclock!!!") ==
#       "Info       | 17:00   >>> It's five oclock!!!")

# print(test('01:23', 'Does this make my nose look big?') ==
#       "<test>     | 01:23   >>> Does this make my nose look big?")

# def prefix(my_prefix):
#     def func(text):
#         return my_prefix + text
#     my_prefix = 'Goodbye'
#     return func

# x = prefix('Hello ')
# print(x('World!'))

# funcs = []
# for i in [1,2]:
#     funcs.append(lambda i=i: i)
#     print(i)

# print([f() for f in funcs])

"""
Four steps of running a test are:
1. Setup
2. Execute
3. Assertions
4. Tear down

Define:
1. Test suite:
    -all the tests you are running on your code
2. Test/Spec
    -an indivdial function you are running to
    check the functionality of one of part of the code.
3. Assertion/Expectation
    -checking whether the value you expected when you ran
    the code was produced or not

An iterator is how you are going through an iterable. Do you want each item? Odd items, 
etc. And an iterable is an object that allows you to go through each
of its components. A generator is an iterable, that productes items lazily.
A generator expression produces an iterable.


"""

# def count_up_to(max_count):
#     count = 1
#     while count <= max_count:
#         yield count
#         count += 1

# counter = count_up_to(5)

# print(next(counter))
# print(next(counter))

"""
A lazy sequece produces the value when called up, it doesn't 
produce all values at once, so it is more memory efficient than
a list.
"""

# my_range = range(1,5)

# for num in my_range:
#     print(num)

# for num in my_range:
#     print(num)

"""
A first class object can be passed into a function, returned by a fucntion, or assigned
as a variable. 

A higher order function takes a function as its input, or returns it .
"""
# def greeting(func):
#     result = func()
#     return f'greeting is {result}'

# def say_hello():
#     return 'Hello'

# print(greeting(say_hello))

# def square_function(value):
#     return value ** 2

# def higher(do_something, value):
#     return do_something(value)


# print(higher(square_function, 3))

# def get_greeting(greeting):
#     def format_greeting():
#         print(f'This is your greeting: {greeting}')
#     return format_greeting



# my_greeting = get_greeting('hello')
# my_greeting()

# print(my_greeting.__closure__)

"""
A closure is when a function references a free variable in its lexical scope,
even after the function to which the variable was local
is done executing. The inner function "remembers" this
variable. 
"""

#Example

# def outer():
#     greeting = 'hello'
#     def inner():
#         print(greeting)

#     return inner


# my_func = outer()
# my_func()

# def arg_inspector(a, b=2, *args, **kwargs):
#         print(f"a: {a}") #1
#         print(f"b: {b}") #3
#         print(f"args: {args}") #(4,5)
#         print(f"kwargs: {kwargs}") #{name: 'Alice', age: 30}
#         return len(args) + len(kwargs) #2, #2

# result = arg_inspector(1, 3, 4, 5, name="Alice", age=30)
# print(f"Result: {result}")

"""
a: 1
b: 3
args: (4,5)
kwargs: {name: 'Alice', age: 30}
Result: 4

"""

"""
Advanced​: Write a decorator named log_activity.
This decorator should take a function as an argument.
When the decorated function is called, the decorator should
first print a message like Calling function: [function_name],
then execute the function, and finally print another message
like Function [function_name] returned: [return_value].
The decorator must also return the value that the original
function returned.
   For example:
   
    @log_activity
    def add(x, y):
        return x + y

    add(5, 3)

    # Expected output:
    # Calling function: add
    # Function add returned: 8
"""
# def log_activity(func):
#     def wrapper(*args, **kwargs):
#         print(f'Calling function: {func.__name__}')
#         return_value = func(*args, **kwargs)
#         print(f'Function {func.__name__} returned {return_value}')
#         return return_value
#     return wrapper

# @log_activity
# def greeting(string):
#     return string

#greeting = log_activity(greeting)
#greeting = wrapper
#greeting('hello')

# def log_activity(func):
#     def inner(*args, **kwargs):
#         print(f'The name of your function is {func.__name__}')
#         result = func(*args, **kwargs)
#         print(f'The result of {func.__name__} is {result}')
#         return result
#     return inner

# @log_activity
# def add(x, y):
#     return x + y

# add(5,3)

"""
​Intermediate​: Create a function named find_person that accepts
any number of keyword arguments where each key is a person's
name and the value is their profession.
The function should not accept any positional arguments.
It should check if the key "Antonina" exists.
If it does, print a message showing Antonina's profession.
Otherwise, it should print "Antonina not found".
"""
# def find_person(**kwargs):
#     if 'Antonina' in kwargs:
#         print(f"Antonina's profession is {kwargs['Antonina']}")
#     else:
#         print('Antonina not found')

    

# find_person(John="Engineer", Antonina="Software Engineer")
#     # Expected output: Antonina's profession is Software Engineer

# find_person(John="Engineer", Ginni="Software Engineer")
#     # Expected output: Antonina not found
"""
Intermediate​: Consider the two Python functions below.
Which one is a pure function and which one has side effects?
Explain your reasoning with precision, making sure to define what a side effect is.
   
    
    

"""

# # Function A
# def add_to_list(a_list, item):
#     a_list.append(item)
#     return a_list

# # Function B
# some_list = [1, 2, 3]
# new_list = add_to_list(some_list, 4)
# print(some_list) # What does this print?

#     # ---

#     # Function C
# def create_new_list(a_list, item):
#     return a_list + [item]

#     # Function D
# another_list = [1, 2, 3]
# newer_list = create_new_list(another_list, 4)
# print(newer_list)
# print(another_list) # What does this print?

"""
 ​Advanced​: Write a function named later2
 that takes two arguments: a function func, and an argument for that function,
 first_arg. The return value should be a new function that takes its own argument,
 second_arg. This new function should call the original func with both first_arg
 and second_arg.   

"""
# def later2(func, first_arg):
#     def new_func(second_arg):
#         func(first_arg, second_arg)
#     return new_func
        

# def notify(message, when):
#         print(f"{message} in {when} minutes!")

# shutdown_warning = later2(notify, "The system is shutting down")
# shutdown_warning(30) # Expected output: The system is shutting down in 30 minutes!


# def odd_numbers(start):
#     while True:
#         if start % 2 != 0:
#             yield start
#         start += 1

# my_func = odd_numbers(6)
# print(next(my_func))
# print(next(my_func))

# def func(a, b, /, c, *, d):
#     print("success")

# func(1, 2, 3, d=4)

# def calculate(arg1, arg2, arg3, *args, operation='sum'):
#     if type(arg1) != int or type(arg2) != int or type(arg3) != int:
#         raise TypeError("All positional arguments must be integers.")
    
#     if operation != "sum" or operation != "multiply":
#         raise TypeError("The operation must be 'sum' or 'multiply'")
    
#     if operation == 'sum':
#         sum_of_args = sum(args)
#         return sum([arg1, arg2, arg3, sum_of_args])
    
#     if operation == 'multiply':
#         result = 1
#         for arg in args:
#             result *= arg
#         result *= arg1
#         result *= arg2
#         result *= arg3
#         return result
    
    


# print(calculate(2, 3, 4))                        # 9
# print(calculate(2, 3, 4, 5))                     # 14
# print(calculate(2, 3, 4, operation="sum"))       # 9
# print(calculate(2, 3, 4, operation="multiply"))  # 24

# try:
#     calculate(1, 2)
# except TypeError as e:
#     print(e)
#     # calculate() missing 1 required positional argument: 'num3'

# try:
#     calculate(1, 2, "3", operation="sum")
# except TypeError as e:
#     print(e)
#     # All positional arguments must be integers.

# try:
#     calculate(1, 2, 3, operation="divide")
# except TypeError as e:
#     print(e)
#     # The operation must be 'sum' or 'multiply'.

# def string_sandwich(string1, string2=None):
#     if string2 != None:
#         return f'{string1}{string2}{string1}'
#     else:
#         def inner(string2):
#             return f'{string1}{string2}{string1}'
#         return inner

# print(string_sandwich("ab", "cd") == "abcdab");              # True
# print(string_sandwich("bread", "meat") == "breadmeatbread"); # True
# print(string_sandwich("cba", "") == "cbacba");               # True

# foo_sandwich = string_sandwich("foo")
# print(foo_sandwich("bar") == "foobarfoo");                   # True
# print(foo_sandwich("xyzzy") == "fooxyzzyfoo");               # True


# def combine_data(data_entries, /, **kwargs):
#     if type(data_entries) != list:
#         raise TypeError("data_entries must be a list.")
#     for item in data_entries:
#         if type(item) != dict:
#             raise TypeError("All entries must be dictionaries.")
#     for record in data_entries:
#         for key, value in kwargs.items():
#             record[key] = value
#     return data_entries

# records = [{'name': 'Jane', 'age': 30}, {'name': 'Jake', 'age': 25}]
# updated_records = combine_data(records, location='New York', age=35)
# print(updated_records)
# # Pretty printed for clarity; your code can print everything
# # on one long line.
# # [
# #     {'name': 'Jane', 'age': 35, 'location': 'New York'},
# #     {'name': 'Jake', 'age': 35, 'location': 'New York'},
# # ]
        
# try:
#     combine_data("not a list", name='Charlie')
# except TypeError as e:
#     print(e) # data_entries must be a list.

# try:
#     combine_data([{'name': 'Alice', 'age': 30}, 'not a dictionary'],
#                  location='New York')
# except TypeError as e:
#     print(e) # All entries must be dictionaries.

# message = "Please join us"

# def make_inviter(message):
#     def invitation(name):
#         print(f"{message}, {name}.")

#     return invitation

# invite = make_inviter(message)

# message = "Come along now"
# invite("Michelle")

# invite2= make_inviter(message)
# invite2("Cara")

def say_hello(func):
    def inner1(name):
        result = func(name)
        return (f'Hello and {result}')

    return inner1
   

def say_goodbye(func):
    def inner2(name):
        result = func(name)
        return (f'Goodbye {result}')
    return inner2

@say_hello
@say_goodbye
def my_name(name):
    return name

print(my_name('Cara'))



# def decorator_a(func):
#     def wrapper():
#         print("Decorator A: Before")
#         func()
#         print("Decorator A: After")
#     return wrapper

# def decorator_b(func):
#     def wrapper():
#         print("Decorator B: Before")
#         func()
#         print("Decorator B: After")
#     return wrapper

# @decorator_a
# @decorator_b
# def say_hello():
#     print("Hello!")

# say_hello()