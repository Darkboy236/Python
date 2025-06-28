# Define a function called hotel_cost with one argument nights as input
def hotel_cost(nights):
    return 140*nights

# Define a function called plane_ride_cost with one argument city as input
def plane_ride_cost(city):
    if "charlotte" == city:
        return 183
    elif "London" == city:
        return 220
    elif "New York" == city:
        return 222
    elif "Los Angeles" == city:
        return 475

# Define a function called rental_car_cost with one argument days as input
def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days

# Define a function called trip_cost with two arguments city and days as input
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of car rental: ", rental_car_cost(5))

print("Cost of plane ride: ", plane_ride_cost("Los Angeles"))

print("Cost of hotel room: ", hotel_cost(7))

print("Total trip cost: ", trip_cost("Los Angeles", 7, 500))

print(trip_cost("Tampa", 6,500))