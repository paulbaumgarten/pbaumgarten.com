
def find_lowest_value( numbers ):
    # Start by treating the first value as the lowest
    lowest = numbers[0]
    # Inspect every value in our set of numbers
    for n in numbers:
        # If a particular value is lower than what we already found
        if n < lowest:
            # Save it as our new lowest value
            lowest = n
    # Return the lowest we found
    return lowest

# The problem
values = [6, 4, 3, 12, 7, 8, 2, 13, 5, 14, 10, 11, 9]
results = []

# While unsorted values remain
while len(values) > 0:

    # Find the lowest value
    lowest = find_lowest_value( values )

    # Add it to the sorted set
    results.append( lowest )

    # Remove it from the source set
    values.remove( lowest )
