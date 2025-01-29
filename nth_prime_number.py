def nth_prime():
    n = int(input())
    prime_no = []
    num = 2
    #it keeps the loop till the prime_no list exceeds the n given
    while len(prime_no) < n:
        for i in prime_no:
            #if its a prime it wont divide by other prime numbers we are checking that
            if num % i == 0:
                break
        else:
            prime_no.append(num)
        num += 1

    print(prime_no)

nth_prime()
