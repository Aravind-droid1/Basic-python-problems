def reverse_number_optimized(n):
    return int(str(n)[::-1])

n = int(input("Enter a number: "))
print("Reversed number:", reverse_number_optimized(n))
