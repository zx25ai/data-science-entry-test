def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Searches for all occurrences of `find_val` in `lst` and replaces them with `replace_val`.
    - `lst` must be a list. Returns -1 if not.
    - Returns the modified list.
    """
    if not isinstance(lst, list):  # Check if input is a list
        return -1

    for i in range(len(lst)):  # Iterate through the list
        if lst[i] == find_val:
            lst[i] = replace_val  # Replace if match found

    return lst  # Return the modified list

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

# 1st invocation
l1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
#print(l1)

# 2nd invocation
l2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
#print(l2)