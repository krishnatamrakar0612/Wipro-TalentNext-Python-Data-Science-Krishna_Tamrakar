travel_distance = float(input("How far would you like to travel in miles? "))

if travel_distance < 3:
    transport = "Bicycle"
elif travel_distance < 300:
    transport = "Motor-Cycle"
else:
    transport = "Super-Car"

print(f"I suggest {transport} to your destination")