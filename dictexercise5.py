#Get the key of a minimum value from the following dictionary

sampleDict = {
    "Physics": 82, 
    "Math": 65,
    "History": 75
}

print(min(sampleDict, key=sampleDict.get))