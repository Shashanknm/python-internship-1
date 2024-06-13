def move_elevator(cf, tf):
    if tf < 0 or tf > num_floors:
        return "Invalid target floor. Choose a floor between 0 and " + str(num_floors)
    if cf < 0 or cf > num_floors:
        return "Invalid current floor. Choose a floor between 0 and " + str(num_floors)
    if tf == cf:
        return "Already on Floor " + str(tf)
    result = ""
    while cf != tf:
        if tf > cf:
            
            result += "Floor " + str(cf) + " Departure " + " Floor " + str(cf + 1) + " Arrival\n"
            
            cf += 1
        elif tf < cf:
            
            result += "Floor " + str(cf) + " Departure " + " Floor " + str(cf - 1) + " Arrival\n"
            
            cf -= 1
          
    return result.strip()  

num_floors = 4  
while True:
    cf = int(input("Enter the current floor (0 to " + str(num_floors) + "): "))
    if cf < 0 or cf > num_floors:
        print("Invalid current floor. Choose a floor between 0 and " + str(num_floors))
        continue  
    tf = int(input("Enter the target floor (0 to " + str(num_floors) + "): "))

    result = move_elevator(cf, tf)
    print(result)
