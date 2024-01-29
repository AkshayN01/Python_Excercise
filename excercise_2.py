def checkWeights(msg):
    bag_weight = int(input(msg))
    continue_loop = True
    while continue_loop:
        if(bag_weight > 15):
            print(f"Weight exceeds 15kg. Please remove atleast {bag_weight-15}kgs to reduce the weight.")
            bag_weight -= int(input("Enter the weight removed: "))
        else:
            print("Weight is within the limits")
            continue_loop = False

checkWeights("Enter the weight of your baggage: ")