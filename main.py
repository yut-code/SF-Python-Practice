# exer 1
keys = ['ten', 'twenty','thirty']
values = [10,20,30]
dictionary = dict(zip(keys,values))
print(dictionary)


#exercise 2
dict1 = dictionary.copy()
dict2 = {'thirty': 30, 'fourty': 40, "fifty":50}

dict1.update(dict2)
print(dict1)

#exer 3
# The fromkeys() method returns a dictionary with the specified keys and the specified value.
# syntax: dict.fromkeys(keys, value)
employees = ['Kelly', 'Emma', 'John']
defaults = {'designation': 'application developer', 'salary':8000}

dict = dict.fromkeys(employees,defaults)
print(dict)
print(dict["Kelly"])


#exer 4
# dictionary comprehension?
# dictionary = {key: value for vars in iterable}
#https://www.programiz.com/python-programming/dictionary-comprehension

sampleDict = {
  'name':'Kelly',
  'age':25,
  'salary':8000,
  'city':'new york'
}

# #dict comprehension
keys = ['name', 'salary']
dict = {key: sampleDict[key] for key in keys}
print(dict)

# #using a for loop instead of dict comprehension
# d = {}
# for key in keys:
#   d[key] = sampleDict[key]
# print(d)

#exer 5
#min() return the value in the first value in sorted. key designate the way to sort the values. key=d.get means the list will be sorted by values of the dictionary.
#https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
sampleDict = {
  "physics": 82,
  "math": 65,
  "history": 75
}

worst = min(sampleDict, key=sampleDict.get)
print(worst)

# new ?????
s = {'b', 'a', 'r'} & set('qux')
print(s)

# - is difference() and ^ is symmetric_difference()
print({1, 2, 3, 4, 5} - {3, 4} ^ {5, 6, 7} )