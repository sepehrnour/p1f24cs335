# Joshua Lopez, Sepehr Nourbakhsh, Lynae Mercado
# function minSwapsToCouples(row): 
#     n = length(row) // 2  
#     position_map = [0] * (2 * n)
#     for i from 0 to 2*n - 1:
#         position_map[row[i]] = i
    
#     swaps = 0
#     for i from 0 to 2*n - 1 step 2:
#         partner = row[i] ^ 1  
#         if row[i+1] != partner:
#             partner_pos = position_map[partner]
#             swap(row[i+1], row[partner_pos])
#             position_map[row[partner_pos]] = partner_pos
#             position_map[row[i+1]] = i+1
#             swaps += 1
    
#     return swaps


# We iterate through the row array, examining pairs of adjacent seats.
# For each seat i, we calculate the ID of the person’s partner (using XOR with 1).
# If the partner is not already seated next to them, we find the partner's current position, swap them with the person next to the original seat, and update the seat indices.
# Count the number of swaps required to make all couples sit together.