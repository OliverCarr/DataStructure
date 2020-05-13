
'''
fhand = open('mbox.txt')
print(fhand)

stuff = 'Hello\nWorld' 
#\n new line character in a string, counts as single character
print(stuff)

stuff = 'X\nY'
print(stuff)
print(len(stuff))
'''

#Reading Files
'''
fhand = open('mbox-short.txt')

print(fhand)

count = 0
for line in fhand:
    count += 1
print('Line Count:', count)

inp = fhand.read()
print(len(inp))

print(inp[:21])  #Each call to read exaustts the resorce
'''
#Searching through a file
'''
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip() #rstrip (right-strip) lstrip (left-strip)
    if line.find('@uct.ac.za') == -1: continue
    print(line)
'''

#Letting the user choose the file name
'''
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File not found')
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)
'''

#writing files
'''
fout = open('output.txt', 'w')
print(fout)
line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = "the emblem of our land.\n"
fout.write(line2)

fout.close()
'''

#Debugging
'''
s = '1 2\t 3\n 4'
print(s)

S = repr(s) #A string representation of an object for degugging purposes

print(S)
'''

#Exercise 1
#Write a program to read through a file and print the 
#contents of the file (line by line) all in upper case. 

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File not found')
    exit()

count = 0
for line in fhand:
    if count >= 5:
        break
    line = line.upper() 
    line = line.rstrip()
    count += 1
    print(line)

#Exercise 2
#Search for lines starting "X-DSPAM-Confidenc:"
#find the folowing floating point value 
#print the average value at the end

fname = input('Enter the file name: its called mbox.txt')
try:
    fhand = open(fname)
except:
    print('File not found did you read the instruction')
    print('Adding Lazer Eyes to find my data')
    print("and its missing somtheing")
    exit()

count = 0
for line in fhand:
    if line.find('X-DSPAM-Confidence:') == -1: continue
    count += 1
    line = line[20:]
    print(line)
