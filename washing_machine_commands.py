def washing_machine_time(weight, water_level):
    if weight < 0:
        return "INVALID INPUT"
    if weight == 0:
        return "Time Estimated: 0 minutes"
    if weight > 7000:
        return "OVERLOADED"
    if water_level == "L": 
        if weight <= 2000:
            return "Time Estimated: 25 minutes"
    elif water_level == "M": 
        if 2001 <= weight <= 4000:
            return "Time Estimated: 35 minutes"
    elif water_level == "H": 
        if weight > 4000:
            return "Time Estimated: 45 minutes"
    
    return "INVALID INPUT"

weight = int(input("Enter the weight of clothes: "))
water_level = input("Enter the water level (L,M,H): ").strip().upper()

result = washing_machine_time(weight, water_level)
print(result)