def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    
    i = len(s) - 1
    
    newString = ""
    while i >= 0:
        newString = newString + s[i]
        i = i - 1
        
    return newString
    
# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

t1 = string_reverse("Hello World")
print (t1)

t2 = string_reverse("Python")
print (t2)
