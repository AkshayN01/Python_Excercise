def getDivisors(n, num_list):
    total = 0
    i = 1
    while i <= n :
        if n%i == 0 and i in num_list:
            total += i
        i = i + 1

    return total

print(getDivisors(9,[1,2,3,4,5,6,7,8,9,10]))