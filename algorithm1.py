# Joshua Lopez, Sepehr Nourbakhsh, Lynae Mercado
def minSwapsToCoupleShuffle(peopleRow): 
    # Function to find the root of the group containing the person
    def locateLeader(person):
        if leader[person] != person:
            leader[person] = locateLeader(leader[person])
        return leader[person]
    
    # Function to unify two groups containing different people
    def unifyGroups(personA, personB):
        rootA = locateLeader(personA)
        rootB = locateLeader(personB)
        if rootA != rootB:
            leader[rootB] = rootA

    halfSeats = len(peopleRow) // 2
    leader = list(range(halfSeats))  # Initialize each person as their own group leader
    swapCount = 0
    
    # Iterate through the row two seats at a time
    for seat in range(0, 2 * halfSeats, 2):
        firstPersonID = peopleRow[seat] // 2  # Determine group ID for the first person
        secondPersonID = peopleRow[seat + 1] // 2  # Determine group ID for the second person
        
        # If they aren't in the same group, unify them and count the swap
        if locateLeader(firstPersonID) != locateLeader(secondPersonID):
            unifyGroups(firstPersonID, secondPersonID)
            swapCount += 1
    
    return swapCount

# Example usage
peopleRow = list(map(int, input("Enter the row of people (space-separated): ").split()))
print("Minimum swaps needed:", minSwapsToCoupleShuffle(peopleRow))
