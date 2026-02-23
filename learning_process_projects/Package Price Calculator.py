p_weight = int(input("Enter weight of your package : "))

def calculate_price(weight):
    if weight >= 20:
        print("Packages which heavier than 20 kg is not allowed")
        return

    distance = float(input("Enter distance for delivery : "))

    if distance <= 50 and weight <= 5:
        print("Price is 20 dollars")
    elif distance > 50 or weight > 5:
        print("Price is 50 dollars")

calculate_price(p_weight)