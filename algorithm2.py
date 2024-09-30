# Joshua Lopez, Sepehr Nourbakhsh, Lynae Mercado
def findCircularTripStart(cityDistances, gasStations, fuelEfficiency):
    accumulatedShortage = 0  # Tracks overall fuel shortage
    accumulatedSurplus = 0  # Tracks overall fuel surplus
    startCityIndex = 0  # Tracks the preferred starting city index
    
    # Iterate through each city in the circular route
    for currentCity in range(len(cityDistances)):
        # Calculate net fuel gain at the current city
        fuelGain = gasStations[currentCity] * fuelEfficiency - cityDistances[currentCity]
        
        # Update accumulated surplus with the fuel gain
        accumulatedSurplus += fuelGain
        
        # If the surplus becomes negative, update the starting city
        if accumulatedSurplus < 0:
            startCityIndex = currentCity + 1
            accumulatedShortage += accumulatedSurplus
            accumulatedSurplus = 0  # Reset surplus for the new starting point
    
    # Determine the valid starting city
    return startCityIndex if accumulatedShortage + accumulatedSurplus >= 0 else -1

# Example usage
cityDistances = list(map(int, input("Enter city distances (space-separated): ").split()))
gasStations = list(map(int, input("Enter fuel available at each city (space-separated): ").split()))
fuelEfficiency = int(input("Enter miles per gallon (MPG): "))
print("Preferred starting city:", findCircularTripStart(cityDistances, gasStations, fuelEfficiency))
