
fruit = 'banana'
letter = fruit[0] #the 0th element is the first of the string



length = len(fruit)
last = fruit[length-1] #the last letter is the 5th element one less than sixth
# fruit[-1] would also have worked
 

#While Loops'''

'''
index = len(fruit) -1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1
'''

#For Loops

'''
for cha in fruit:
    print(cha)
'''

#Slicing strings

'''
s = 'Monty Python'
print(s[6:])
'''

#Immutable Strings
'''
print(fruit)
newfruit = 'B' + fruit[1:] #conacination of strings
print(newfruit)
'''
#Looping and counting
'''
count = 0
for letter in fruit:
    if letter == 'a':
        count += 1

print("The number of a's in the word <", fruit, "> is", count)
'''
#in operator

'a' in 'banana' #is True
'q' in 'banana' #is False

#String Comparison
'''
word = 'Pineapple'
#All capital letters are before lowercases 
if word < 'banana':
    print('Your word, '+word+', comes before banana.')
elif word > 'banana':
    print('Your word, '+word+', comes after banana.')
else:
    print('All right, bananas.')
#Standard formats is used to get around this (all lowercase)
'''
#String methods
'''
print(fruit)
Fruit = fruit.capitalize()
FRUIT = fruit.upper()
print(Fruit)
print(FRUIT)

index  = fruit.find('na', 3)
print(index)
'''

#word.capitalize()      first letter capitalises 
#word.upper()           capialies all letters
#word.find('str')       returns index of postion within string, -1 if fails
#word.strip()           removes white space from beggining and end

#word.startswith('str') returns boolian (True/False) casesensitive
#word.lower().startswith('str')     lowercases all letters first

'''
count = fruit.count('a')
print(count)
'''

#Parsing string
'''
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos) #argumet: ('str'[, start[, end]])
print(sppos)

host = data[atpos+1:sppos]
#From one after the @ sign upto but not including the next space
print(host)
'''

#Format operator %
'''
camels = 42

print(camels)
print(type(camels))

camels = '%d' % camels #changes the integer 42 to the string 42

print(camels)
print(type(camels))

sent = 'I have spotted %d camels.' % camels

print(sent)

sent2 = 'In %d years I have spotted %g %s' % (3, 0.1, 'camels')
#use of a tuple, seqence must match
# %d integer
# %g float
# %s string

print(sent2)
'''

#Debugging 
'''
while True:
    line = input('> ')
    if len(line) > 0 and line[0]=='#'  :
        continue
    if line == 'done':
        break 
    print(line)
print('Done!')
'''

#Glossary
'''
Counter: a variable used to count something, starting at zero
Empty string: '', no characters, zero length
Format Operator: % 
'''

#Exercise

str = 'X-DSPMA-Confidence:0.8475'

start = str.find(':')+1


data = str[start:]
data = float(data)

print(data)
print(type(data))



