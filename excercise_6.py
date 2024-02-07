def getDivisors(n, num_list):
    for i in n:
        total = 0
        for j in num_list:
            if(i%j == 0):
                total += j
        print(f"Sum of multiples of {i} is {total}")

getDivisors([8,9],[1,2,3,4,5,6,7,8,9,10])