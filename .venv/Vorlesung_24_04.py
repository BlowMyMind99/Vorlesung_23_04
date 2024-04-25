a = input()
A = 23
B = 12

cmdlet = "result = A" + a + " B"
exec(cmdlet)
print (result)

#lsit comprehension is a very powerfil tool in python to create and iterate
#lists essential in a list comprehemsion are
#   *the square brackets[]
#   *the expression to create the list
#   * the "for" keyword
#   *the variable to iterate over
# *the "in" keyword
#   *the iterabel to iterate over

#Create a list of the squares of the numbers from 0 to 9
squares = [x*x for x in range(10)]
print (squares)


#listcomprehension can be extended with if clauses
#this is a very powerful tool to filter lists
#Create a list of the squares of the numbers from 0 to 9 that are even
squares = [x*x for x in range(10) if x % 2 == 0]
print (squares)

#instead of doing the modulo operation, you could also call an own function
def is_even(x):
    return x % 2 == 0
evenSquares = [x*x for x in range(10) if is_even(x)]
print (evenSquares)

#an alternative to using the if clause for filterung is to use python filter
evenSquares = [x*x for x in filter(is_even, range(10))]
print(evenSquares)

#filter does not return a list, but a filter object
#to convert it to a list, you can use the list function
evenSquares = list(filter(is_even, range(10)))

#yield is a keyword that is used in generators
#generators are a way to create iterators


#the function name "is_even" hides what reallly happens. It seems a little bit
#overkill to define a function for such a simple operation. We can ise lambda
#functions to define a function in place

evenSquares = [x*x for x in filter(lambda x: x % 2 == 0, range(10))]
print(evenSquares)

#labda functions cans alsp be assigned with function names as "oneliner"
is_even = lambda x: x % 2 == 0

#above code is equivalent to the following code
def is_even(x):
    return x % 2 == 0


#list comprehension can be used to create dictionaries
#essential in a dictionary comprehension are
#   * the curly brackets {}#
#   * the key-value-pair
#   * the "for" keyword
#   * the variable to iterate over
#   * the "in" keyword
#   * the iterable to iterate over
squares = {x: x*x for x in range(10)}
print(squares)

