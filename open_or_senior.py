data = [(16, 23),(73,1),(56, 20),(1, -1)]

results = []
for i in data:
    if i[0] >= 55 and i[1] > 7:
        result = "Senior"
        results.append(result)
    else:
        result = "Open"
        results.append(result)

print(results)

#Cool Solutions
# def openOrSenior(data):
#   return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
