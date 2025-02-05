def calculate_simple_interest(P,R,T):
    SI = (P*R*T)/100
    print("The simple interest is:",SI)

P = float(input("Enter the principal amount(P): "))
R = float(input("Enter the rate of interest(R): "))
T = float(input("Enter the time period in years(T): "))

SI = calculate_simple_interest(P,R,T)