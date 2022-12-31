string = "Practice Problems to Drill List Comprehension in Your Head"
nums = [i for i in range(1,1001)]

# Find all of the numbers from 1–1000 that are divisible by 8
divisible8 = [num for num in range(1, 1001) if num % 8 == 0]
q1_answer = [num for num in nums if num % 8 == 0]

# Find all of the numbers from 1–1000 that have a 6 in them
haveSix = [num for num in range(1, 1001) if '6' in str(num)]

# Count the number of spaces in a string (use string above)
spaces = []
for char in string:
  if char == " ":
    spaces.append(char)

spaces = len([char for char in string if char == ' '])

# Remove all of the vowels in a string (use string above)
consonants = [char for char in string if char not in 'aeiou']
consonants = ''.join(consonants)

# Find all of the words in a string that are less than 5 letters (use string above)
smallWords = [word for word in string.split(' ') if len(word) < 5]

# Use a dictionary comprehension to count the length of each word in a sentence (use string above)
dict = {}
words = string.split()
for item in words:
  dict[item] = len(item)

dictComp = {word: len(word) for word in words}
# dictionary = {key: value for vars in iterable}


# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
a = []
for divisor in range(2,10):
  for num in nums:
    if (num % divisor == 0):
      a.append(num)
# print(a)

nestedComp = [num for num in nums for digit in range(2, 10) if num % digit == 0]
# print(nestedComp)
q7_answer = [num for num in nums if True in [True for divisor in range(2,10) if num % divisor == 0]]
print(q7_answer)


# For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by
