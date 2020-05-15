
#A list is a sequence

#A list is a sequence of values. 
#These values of any type are 'elements' or 'items'

#Some simple lists
[10, 20 ,30, 40]
['one', 'two', 'three']

#More complex, mixed lists
['spam', 2.0, 5, [10, 20]]

#A list within a list is nested,
#the nested list still counts as a songle element
#this list is length 4

#an empty list can be creating with squre brackets
[]

cheese = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
#print(cheese, numbers, empty)

#Lists are mutable 
'''
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
'''
#Traversing a list
'''
for i in cheese:   #The for loop is weird
    print(i)   


numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

for x in empty:
    print('This never happens.')
#there are no elements in empty so body is never executed
'''
#List operations
'''
a= [1,2,3]
b= [4,5,6]
c = a + b
print(c)

d = a*3
print(d)

#Addition and multiplication concatinate lists 
'''
#List slices
'''
t = ['a', 'b', 'c', 'd', 'e', 'f'] 
print(t[1:3])

print(t[:4])

print(t[3:])

t[1:3] = ['x', 'y']
print(t)
'''
#List methods
'''
t= ['a', 'b', 'c']
t.append('d')   #Stick an element on the end
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)   #Stick a list on the end
print(t1)

t = ['d','a','c','b','e']
t.sort()    #puts it in order
print(t)
'''
#Deleting elements
'''
t = ['a','b','c']
x = t.pop(1)    #'Pops out' one element and stores it
print(t)
print(x)


t = ['a','b','c']
del t[1]   #deletes one element without storeing it
print(t)

t = ['a','b','c']
t.remove('b')   #searthes the list and removes its argument
print(t)


t = ['a','b','c']
t.extend(['d', 'e', 'f'])
del t[1:5]      #upto, but not including, the second element
print(t)
'''
#Lists and Function
'''
nums = [3, 41, 12, 9, 74, 15]

print(len(nums))

print(max(nums))

print(min(nums))

print(sum(nums)) #Only works with values

print(sum(nums)/len(nums))  #Average
'''
#More average
'''
print('Average finder\nEnter a number and hit enter\nWhen you have finished write "done"')
total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    try:
        value = float(inp)
    except:
        print('Not a valid number')
        continue
        
        
    total = total + value
    count += 1

average = total/count
print('Average:', average)
'''
'''
numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
'''

#Lists and String
'''
s = 'spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()  
print(t)
print(t[2])

s = 'spam-spam-spam'
delimiter = '-'
s = s.split(delimiter)
print(s)

delimiter = ' '
t = delimiter.join(t)

print(t)
'''
#Parsing lines


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])