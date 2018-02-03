'''
Created on Feb 3, 2018

@author: ITAUser
'''
'''
f = open("poem.txt", "r")
#print(f.read())
print(f.readline())
text = f.read()
Words = text.split()
print(Words)
print(len(Words))
f.close
#f.read(())

fw = open("new.txt", "W")
fw.write("pinneaple DOES go on pizza!")
'''
'''
filename = "number.txt"
numberfile=open("number.txt", "r+");

numberline = 0
numberwords = 0

for line in numberfile:
    words = line.split();
    
    numberline = numberline +1;
    numberwords = len(words);
    numberchar = len(line);
    
print(numberchar)
    '''

filename = "constituton.txt"
numberfile= open( filename, "r+");

numberwords = 0
for line in numberfile:
    words = line.split();
    numberwords = numberwords + len(words);
print(numberwords)
    
    
    
    
    
    
    