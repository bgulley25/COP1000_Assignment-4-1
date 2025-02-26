"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# The minimum charge for all signs is $35.00
# There is an additional $4 charge for each additional character after the first 5 characters
# There is an additional $20 charge for signs made of oak
# There is an additional $15 charge for gold-leaf lettering

# Charge for this sign.
charge = 0.00
numChars = 18
color = "black"
woodType = "oak"

# Number of characters.
if numChars > 5: 
    charge = 35.00 + (numChars - 5) * 4.00
elif numChars > 0: 
    charge = 35.00

# Color of characters.
if color == "gold":
    charge += 15.00

# Type of wood.
if woodType == "oak":
    charge += 20.00

# Write assignment and if statements here as appropriate.

    

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
