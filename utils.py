def validate_numbers(*args):
    """
    Validate that all arguments are numbers (int or float)
    Returns tuple of (is_valid, error_message)
    """
    for arg in args:
        if not isinstance(arg, (int, float)):
            return False, "Error: All inputs must be numbers"
    return True, ""

def validate_non_zero_divisor(divisor):
    """
    Validate that the divisor is not zero
    Returns tuple of (is_valid, error_message)
    """
    if divisor == 0:
        return False, "Error: Division by zero is not allowed"
    return True, ""

def format_result(result):
    """
    Format the result to remove trailing zeros after decimal point if possible
    """
    if isinstance(result, float):
        # Convert to integer if the float is a whole number
        if result.is_integer():
            return int(result)
    return result