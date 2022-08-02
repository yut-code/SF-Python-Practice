#PROJECT: TYPE TEST
import time

#Print a paragraph and ask your user to copy it as quickly as possible. Give them a countdown before beginning your timer and letting them type. As soon as they press enter, stop their time. Report the number of mistakes they made and the time they took to type the paragraph in seconds.
para = "Dragons don't exist they said. They are the stuff of legend and people's imagination. Greg would have agreed with this assessment without a second thought 24 hours ago."

print("Welcome to the Type Test! Type the following as quickly as possible. I will give you a three second countdown before starting the clock:\n")
print(para)
time.sleep(1)
print('\nReady...')
time.sleep(1)
print('Set...')
time.sleep(1)

start = time.time()
userInput = input('Go! \n')
end = time.time()

print('\nIt took you {} seconds to type out the paragraph!'.format(round(end-start)))

errorCount = 0
for i in range(min(len(userInput), len(para))):
  if para[i] != userInput[i]:
    errorCount += 1
print('You had {} mistakes.'.format(errorCount))