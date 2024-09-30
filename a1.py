# function minSwapsToCouples(row):
#     n = length(row) // 2  # Number of couples (or n = len(row) // 2)
    
#     # Create a mapping of person to their seat index
#     position_map = [0] * (2 * n)
#     for i from 0 to 2*n - 1:
#         position_map[row[i]] = i
    
#     swaps = 0
    
#     # Iterate through each seat
#     for i from 0 to 2*n - 1 step 2:
#         # Find the partner for the person sitting at row[i]
#         partner = row[i] ^ 1  # Partner of person row[i] is row[i] XOR 1
        
#         # If the partner is not already sitting next to them
#         if row[i+1] != partner:
#             # Find the current position of the partner
#             partner_pos = position_map[partner]
            
#             # Swap the person sitting in seat i+1 with the partner
#             swap(row[i+1], row[partner_pos])
            
#             # Update the position map after the swap
#             position_map[row[partner_pos]] = partner_pos
#             position_map[row[i+1]] = i+1
            
#             # Increment swap count
#             swaps += 1
    
#     return swaps


# We iterate through the row array, examining pairs of adjacent seats.
# For each seat i, we calculate the ID of the person’s partner (using XOR with 1).
# If the partner is not already seated next to them, we find the partner's current position, swap them with the person next to the original seat, and update the seat indices.
# Count the number of swaps required to make all couples sit together.