# function findPreferredStartingCity(city_distances, fuel, mpg):
#     total_fuel = 0
#     current_fuel = 0
#     start_city = 0
    
#     for i from 0 to length(city_distances) - 1:
#         # Calculate the net fuel after traveling to the next city
#         current_fuel += fuel[i] * mpg - city_distances[i]
        
#         # Track the total fuel for verification
#         total_fuel += fuel[i] * mpg - city_distances[i]
        
#         # If we run out of fuel, reset the starting city
#         if current_fuel < 0:
#             start_city = i + 1
#             current_fuel = 0
    
#     # If total fuel is non-negative, there exists a valid starting city
#     if total_fuel >= 0:
#         return start_city
#     else:
#         return -1  # This case is theoretically impossible as per the problem description

# Traverse the cities, calculating the net fuel (gas gained from the station minus the distance traveled) after moving to the next city.
# Track the total fuel to ensure that the journey is possible.
# If at any point we run out of fuel, reset the starting city to the next city and continue.
# At the end of the loop, if the total fuel is non-negative, return the start city, otherwise return -1 (though the problem guarantees this won't happen).