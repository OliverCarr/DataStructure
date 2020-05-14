
#A list is a sequence

#A list is a sequence of values. 
#These values of any type are 'elements' or 'items'

#Some simple lists
[10, 20 ,30, 40]
['one', 'two', 'three']

#More complex, mixed lists
['spam', 2.0, 5, [10, 20]]

#A list within a list is nested

#an empty list can be creating with squre brackets
[]

cheese = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
#print(cheese, numbers, empty)

#Lists are mutable 

print(cheese[0])

numbers = [17, 123]
numbers[1] = 5 #Unlike strings lists are mutable 
print(numbers)
#This is mapping

#List indices work the same as string indices

#Any integer expression can be used as an index

#If you try to read or write an element that does not exist,
#you get an IndexError

#If an idex has a negative value,
#it counts backwards from the end of the list

print('Chalk' in cheese)
#The in operator also works

