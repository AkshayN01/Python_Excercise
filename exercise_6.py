def getDivisors(n, num_list):
    total = 0
    for i in num_list:
        if(n%i == 0):
            total += i

    return total

print(getDivisors(9,[1,2,3,4,5,6,7,8,9,10]))