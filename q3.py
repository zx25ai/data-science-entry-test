def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    original_value = dct.get(key)
    if original_value is not None:  # Check if key exists
        print(original_value)      # Print before updating
        dct[key] = value           # Update the value

    return dct  # Return the updated dict
    
# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

#invocation 1 
t1 = update_dictionary({}, "name", "Alice")
#if t1 is not None:
#   		print (t1)

#invocation 1 
t2 = update_dictionary({"age": 25}, "age", 26)
#if t2 is not None:
#   		print (t2)