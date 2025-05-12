def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):    
        return False
    
    if divisor == 0:
            return False

    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

t1 = check_divisibility(10,2)
#print(t1)

t2 = check_divisibility(7,3)
#print(t2)