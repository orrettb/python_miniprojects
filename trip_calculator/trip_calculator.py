"""
Receive the following arguments from the user:

- kilometers to drive
- liters-per-kilometer usage of the car
- price per liter of fuel
"""
kilo_to_drive = float(input("Enter the kilometers to drive for your trip:"))
liters_per_kilometer = float(input("Enter the liters per kilometer performance of your car:"))
price_per_liter = float(input("Enter the price per kilometer you pay for fuel:"))
#calculate the cost of the trip
trip_cost = (kilo_to_drive/liters_per_kilometer)*price_per_liter
#display results
print("It will cost you ${} for your trip".format(trip_cost))