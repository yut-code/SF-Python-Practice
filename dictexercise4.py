#Create a new dictionary by extracting the following keys from a dictionary

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)

