def getSumOfAllMultiples(num1, num2, num_list):
    total = 0
    for i in num_list:
        if ((i%num1 == 0) or (i%num2 == 0)):
            total += i

    return total

print(getSumOfAllMultiples(3,5,[1,2,3,4,5,6,7,8,9,10]))