def find_first_negative(lst):
    """
    Task 1
    - Finds the first negative number in a list (lst).
    - Returns the first negative number if found, otherwise returns "No negatives".
    - Uses a while loop.
    """
    x = 0  # Initialize index counter
    
    while x < len(lst):  # Check while index is within list bounds
        if lst[x] < 0:
            return lst[x]  # Return first negative found
        x += 1  # Move to next index
    
    return "No negatives"  # Return if no negatives found


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

t1 = find_first_negative([3, 5, -1, 7, -2, 8])
#print(t1)
t2 = find_first_negative([2, 10, 7, 0])
#print(t2)
