#Initialize dictionary with default values

employees = ["Kelly", "Emma", "Joyhn"]
defaults = {"designation": "Application Developer", "salary": 8000}

newdict = dict.fromkeys(employees, defaults)
print(newdict)

#Bonus: show info for just Kelly
print(newdict["Kelly"])