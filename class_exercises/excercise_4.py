def getSumOfAllMultiples(num1, num2, limit):
    total = 0
    for i in range(limit):
        if (i%num1 == 0) or (i%num2 == 0):
            total += i

    return total

print(getSumOfAllMultiples(3,5,1000))