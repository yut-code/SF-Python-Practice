#LESSON 2
import time

#Exercise 1: Timing a for loop. Write a for loop that counts to 999999 and time how long it takes. Print the time elapsed.
originalTime = time.time()

for i in range(999999):
   continue

timeNow = time.time()

timeElapsed = round(timeNow - originalTime, 3)
print(timeElapsed, 'secs')

#Exercise 2: Sleeping text. Print "Hello" and then "World" with three seconds elapsing between the two statements.
print('Hello')
time.sleep(3)
print('World')

#Exercise 3: Writing functions. Write the following functions and check your work by calling the function on the example input.
#3a) Write a function that takes two numbers (x and y) as input and returns 3x+y
def algebra(x, y):
  return 3*x+y

print('the answer is', algebra(x=1, y=3))


#3b) Write a function that takes a string as input and return the number of vowels in the string.
def vowels(string):
  count = 0
  for letter in string:
    if letter in 'aeiouAEIOU':
      count += 1
  return count

print('there are', vowels('goose'), 'vowels')

#3c) Write a function that takes two months and calculates the number of months between them. (ex. January and April have two months between them)
def btwnMonths(startMonth, endMonth):
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  start = months.index(startMonth)
  end = months.index(endMonth)
  if end < start:
    end += 12
  ans = end-start-1
  return ans
  
print('Months between:', btwnMonths('Apr', 'Jan'))

#3d) Write a function that takes a string "rock", "paper", or "scissors". Randomly pick the opponent's play (rock, paper, or scissors). Print both the opponent's play and who won the match
import random

# easy to understand way
def rockPaperScissors(string):
  play = ["rock", "paper", "scissors"]
  opp = random.choice(play)
  if string == opp:
    print('You tied')
  elif string == 'rock': 
    if opp == 'scissors':
      print('You won against', opp)
    else:
      print('You lost against', opp)
  elif string == 'paper':
    if opp == 'rock':
      print('You won against', opp)
    else:
      print('You lost against', opp)
  elif string == 'scissors':
    if opp == 'paper':
      print('You won against', opp)
    else:
      print('You lost against', opp)
  else:
    print('Error, enter a valid response')
rockPaperScissors('rock')

# shorter, used dict and tuple 
def rockPaperScissors1(yourPlay):
  win = {'rock': 'scissors', 'paper':'rock', 'scissors':'paper'}
  oppPlay = random.choice(("rock", "paper", "scissors"))
  if oppPlay == win[yourPlay]:
    print('You won against', oppPlay)
  elif oppPlay == yourPlay:
    print('You tied')
  else:
    print('You lost against', oppPlay)
rockPaperScissors1('scissors')

#Exercise 4: Exploring scope. Explain why x does not change to 10 even after calling func()?

x = 4
def func():
  x = 10
func()
print(x) #Shows 4

# because x = 10 only exists locally inside the function. outside of the function's code block, x = 4 because it is a global variable
