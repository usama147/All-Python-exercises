myNames = []
count = 1
while count != 0:
        name = input("Please enter a name: ")
        myNames.append(name)
        count -= 1
count = len(myNames)
i = 0
while i < count:
        print(myNames[i])
        i += 1
