# Joshua Lopez, Sepehr Nourbakhsh, Lynae Mercado
# function findPreferredStartingCity(city_distances, fuel, mpg):
#     total_fuel = 0
#     current_fuel = 0
#     start_city = 0
    
#     for i from 0 to length(city_distances) - 1:
#         current_fuel += fuel[i] * mpg - city_distances[i]
#         total_fuel += fuel[i] * mpg - city_distances[i]
#         if current_fuel < 0:
#             start_city = i + 1
#             current_fuel = 0
#     if total_fuel >= 0:
#         return start_city
#     else:
#         return -1  

# Traverse the cities, calculating the net fuel (gas gained from the station minus the distance traveled) after moving to the next city.
# Track the total fuel to ensure that the journey is possible.
# If at any point we run out of fuel, reset the starting city to the next city and continue.
# At the end of the loop, if the total fuel is non-negative, return the start city, otherwise return -1 (though the problem guarantees this won't happen).