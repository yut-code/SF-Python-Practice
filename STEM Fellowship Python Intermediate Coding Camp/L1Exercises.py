#LESSON 1

#Exercise 1: Translation. 
english2french = {"bread":"pain","flower":"fleur","computer":"l'ordinateur"}

#a) print all the keys in the dictionary
keys = english2french.keys()
print(keys)
#b) check if "bread" is a key in the dictionary
print(True) if 'bread' in keys else print(False)
#c) print the translation for the key "flower"
print(english2french['flower'])


#Exercise 2: Counting words.
words = ["cat","dog","fish","fish","dog","horse","cat","dog","pig"]

#TODO: make a dictionary that associates a word in words with a count of how many times that word occurs. Print your dictionary at the end.
keys = set(words)
dict = {}
# for i in keys:
#   value = 0
#   for j in words:
#     if i == j:
#       value+=1
#   dict[i] = value

for key in keys:
  value = words.count(key)
  dict[key] = value
print(dict)

#Exercise 3: Reading from a File. Open prideprejudice.txt with reading mode and then print its contents to console.
book = open('prideprejudice.txt', 'r')
bookText = book.read()
print(bookText)
book.close()

#Exercise 4: Writing to a File. Open output.txt with writing mode. Write the string "Hello World" to the file.
file = open('output.txt', 'w')
file.write('Hello World')
file.close()