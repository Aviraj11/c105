import csv
import math
with open("./data.csv", newline='') as f:
    CsvReader = csv.reader(f)
    file_data = list(CsvReader)
NewData = file_data[0]

def mean(NewData):
    n = len(NewData)
    total = 0
    for x in NewData:
        total += int(x)

    mean = total/n
    return mean

squareList = []
for number in NewData:
    a = int(number)-mean(NewData)
    a = a**2
    squareList.append(a)
sum = 0
for i in squareList:
    sum = sum + i
result = sum/(len(NewData) - 1)
standard_deviation = math.sqrt(result)
print(standard_deviation)