import mysql.connector

# Open the file in read mode
with open('data.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
    date=""

    x=""
    y=""
    # Display each line with its line number
    for i, line in enumerate(lines, start=1):
        if(i==5):
            date=line.split(":")[1]
       # print(f"Line {i}: {line.strip()}")
        if(i==24):
            x=line.strip()
        if (i == 25):
            y = line.strip()
    valuesX = [int(x) for x in x.split()]
    valuesY = [int(x) for x in y.split()]
print(date)
print(x)
print(valuesX)


print(y)
print(valuesY)